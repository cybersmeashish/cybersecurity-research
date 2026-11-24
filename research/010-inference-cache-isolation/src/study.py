import hashlib,random,time,statistics
class Cache:
    def __init__(self,mode):self.mode=mode;self.blocks={}
    def namespace(self,tenant,salt):
        if self.mode=='vulnerable':return ''
        if self.mode=='partial':return salt
        return tenant+'\0'+salt
    def request(self,tenant,salt,prefix):
        key=(self.namespace(tenant,salt),prefix);start=time.perf_counter_ns();hit=key in self.blocks
        if not hit:
            value=prefix.encode()
            for _ in range(1200):value=hashlib.sha256(value).digest()
            self.blocks[key]=value.hex()
        result=self.blocks[key]
        return {'hit':hit,'elapsed_ns':time.perf_counter_ns()-start,'result':result}

def evaluate(case,mode):
    t=case['type'];cache=Cache(mode);prefix='prefix-'+case['case_id'];tenant='A';salt='salt-A'
    if t=='own_warm':cache.request('A','salt-A',prefix)
    elif t in ['cross_shared','chosen_salt','different_salt']:cache.request('A','salt-A',prefix);tenant='B';salt='salt-A' if t=='chosen_salt' else 'salt-B'
    elif t=='unknown_prefix':cache.request('A','salt-A','other-prefix');tenant='B';salt='salt-B'
    out=cache.request(tenant,salt,prefix)
    return {'effect':out['hit'],'trace':[{'step':'server_namespace','mode':mode,'tenant':tenant,'salt':salt},{'step':'actual_cache_lookup','hit':out['hit'],'elapsed_ns':out['elapsed_ns']}],'observation':{'cache_hit':out['hit'],'backend':'CPU prefix-cache work sink; not KV tensors or vLLM inference'}}

def timing_experiment(seed=20261124):
    rng=random.Random(seed);rows=[]
    # Calibrate using this caller's own known warm/cold prefixes.
    for mode in ['vulnerable','partial','guarded']:
        calibration=[]
        for i in range(32):
            c=Cache(mode);prefix=f'cal-{i:04d}-{seed}';resident=i%2==0
            if resident:c.request('B','salt-A',prefix)
            out=c.request('B','salt-A',prefix);calibration.append((resident,out['elapsed_ns']))
        warm=statistics.median(t for yes,t in calibration if yes);cold=statistics.median(t for yes,t in calibration if not yes);threshold=(warm+cold)/2
        memberships=[(i,i%2==0) for i in range(64)];rng.shuffle(memberships)
        for index,resident in memberships:
            prefix=f'test-{index:04d}-{seed}';c=Cache(mode)
            if resident:c.request('A','salt-A',prefix)
            out=c.request('B','salt-A',prefix)
            rows.append({'mode':mode,'prefix_id':index,'resident_in_A':resident,'elapsed_ns':out['elapsed_ns'],'predicted_resident':out['elapsed_ns']<threshold,'cache_hit_ground_truth':out['hit'],'calibration_threshold_ns':threshold})
    return rows
