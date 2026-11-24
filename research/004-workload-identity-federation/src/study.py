from common import sign,verify

def evaluate(case,mode):
    t=case['type'];n=str(case['context']);name='lab/repo-'+n
    claims={'iss':'issuer-lab' if t!='wrong_issuer' else 'other-issuer','aud':'cloud-lab' if t!='wrong_audience' else 'other-audience','repository':name+'-renamed' if t=='renamed' else name,'repository_id':'repo-id-'+n if t!='recreated_name' else 'replacement-id-'+n,'owner_id':'owner-id-'+n if t!='transferred_org' else 'new-owner-'+n}
    checks={'signature':verify(sign(claims)) is not None,'issuer':claims['iss']=='issuer-lab','audience':claims['aud']=='cloud-lab'}
    if mode=='vulnerable':checks['mutable_name']=claims['repository']==name
    if mode=='partial':checks.update(mutable_name=claims['repository']==name,stable_owner=claims['owner_id']=='owner-id-'+n)
    if mode=='guarded':checks.update(stable_repository=claims['repository_id']=='repo-id-'+n,stable_owner=claims['owner_id']=='owner-id-'+n)
    mapped=all(checks.values())
    return {'effect':mapped,'trace':[{'step':'evaluate_trust','claims':claims,'checks':checks},{'step':'principal_mapping','principal':'cloud-role-'+n if mapped else None}],'observation':{'principal_mapped':mapped,'backend':'local claim-policy evaluator; no external issuer or cloud STS'}}
