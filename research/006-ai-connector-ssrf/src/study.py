import atexit,http.client,threading,urllib.parse
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
_SERVERS=None
_HITS=[]
class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args):pass
    def do_GET(self):
        role='internal' if self.server.server_address[0]=='127.0.0.2' else 'public'
        _HITS.append({'role':role,'path':self.path})
        if self.path=='/redirect_internal':
            self.send_response(302);self.send_header('Location',f'http://127.0.0.2:{self.server.server_port}/canary');self.end_headers()
        elif self.path=='/redirect_allowed':
            self.send_response(302);self.send_header('Location',f'http://public.lab:{self.server.server_port}/ok');self.end_headers()
        else:
            self.send_response(200);self.end_headers();self.wfile.write(b'INTERNAL-CANARY' if role=='internal' else b'PUBLIC-RESPONSE')
def start():
    global _SERVERS
    if _SERVERS:return _SERVERS[0].server_port
    public=ThreadingHTTPServer(('127.0.0.1',0),Handler)
    internal=ThreadingHTTPServer(('127.0.0.2',public.server_port),Handler)
    _SERVERS=[public,internal]
    for s in _SERVERS:threading.Thread(target=s.serve_forever,kwargs={'poll_interval':0.02},daemon=True).start()
    atexit.register(lambda:[s.shutdown() for s in _SERVERS])
    return public.server_port

def evaluate(case,mode):
    port=start();_HITS.clear();t=case['type'];trace=[];resolutions=0
    host='127.0.0.2' if t in ['forbidden_initial','plain_internal'] else 'public.lab'
    path='/'+t if t.startswith('redirect_') else '/ok'
    url=f'http://{host}:{port}{path}'
    def resolve(name):
        nonlocal resolutions
        resolutions+=1
        address=('127.0.0.2' if t=='dns_change' and resolutions>1 else '127.0.0.1') if name=='public.lab' else name
        trace.append({'step':'controlled_resolution','hostname':name,'address':address,'call':resolutions})
        return address
    body=b'';blocked=False
    for hop in range(4):
        p=urllib.parse.urlparse(url)
        if hop==0:
            initial=resolve(p.hostname)
            if (initial,p.port)!=('127.0.0.1',port):blocked=True;break
        if mode=='partial' and p.hostname!='public.lab':blocked=True;break
        if mode=='guarded':
            # Pin the address checked on the first hop; later hops resolve/check once.
            address=initial if hop==0 else resolve(p.hostname)
            if (address,p.port)!=('127.0.0.1',port):blocked=True;break
        else:address=resolve(p.hostname)
        if address not in ['127.0.0.1','127.0.0.2'] or p.port!=port:raise RuntimeError('Lab cannot connect outside its loopback canaries')
        connection=http.client.HTTPConnection(address,port,timeout=2);connection.request('GET',p.path or '/');response=connection.getresponse();data=response.read();location=response.getheader('Location');status=response.status;connection.close()
        trace.append({'step':'actual_http','address':address,'status':status,'hop':hop})
        if status==302:url=location;continue
        body=data;break
    positive=t in ['allowed','redirect_allowed']
    effect=body==b'PUBLIC-RESPONSE' if positive else any(x['role']=='internal' for x in _HITS)
    return {'effect':effect,'trace':trace+[{'step':'canary_receipts','requests':list(_HITS)}],'observation':{'internal_contact':any(x['role']=='internal' for x in _HITS),'blocked':blocked,'backend':'actual loopback HTTP; controlled resolver adapter, not public DNS'}}
