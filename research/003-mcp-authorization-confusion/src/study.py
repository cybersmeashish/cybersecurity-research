from common import sign,verify

def evaluate(case,mode):
    typ=case['type'];actor=case['actor'];owner=case['owner']
    requester=owner if typ in ['allowed','expired'] else actor
    claims={'iss':'lab-issuer','sub':owner if typ=='foreign_subject' else requester,'aud':'resource-B' if typ=='wrong_audience' else 'resource-A','azp':'client-B' if typ=='foreign_client' else 'client-A','exp':5 if typ=='expired' else 200,'handle':'owned-handle'}
    token=sign(claims);verified=verify(token)
    checks={'signature':verified is not None,'issuer':claims['iss']=='lab-issuer','expiry':claims['exp']>100}
    if mode in ['partial','guarded']:checks['subject']=claims['sub']==requester
    if mode=='guarded':checks.update(audience=claims['aud']=='resource-A',client=claims['azp']=='client-A',handle_owner=(owner if typ=='foreign_handle' else requester)==requester)
    accepted=all(checks.values());effects=[]
    if accepted:effects.append({'resource':'resource-A','operation':'read','executed_as':requester})
    return {'effect':bool(effects),'trace':[{'step':'validate_signed_artifact','claims':claims,'checks':checks},{'step':'mock_resource','effects':effects}],'observation':{'accepted':accepted,'backend':'HMAC-signed lab artifact and proxy validator; not a complete OAuth/MCP server'}}
