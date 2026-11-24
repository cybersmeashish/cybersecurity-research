import queue,sqlite3
from common import sign,verify

def evaluate(case,mode):
    t=case['type'];tenant='tenant-'+str(case['context']);foreign='foreign-'+str(case['context'])
    payload_tenant=foreign if t in ['foreign_payload','cross_tenant_retry'] else tenant
    envelope={'tenant':tenant,'payload_tenant':payload_tenant,'expiry':5 if t=='expired_event' else 200,'request':'request-'+case['case_id']}
    message=sign(envelope)
    if t=='invalid_signature':message=message[:-2]+'xx'
    bus=queue.Queue();bus.put(message);claims=verify(bus.get());trace=[{'step':'ingress','authenticated_tenant':tenant,'payload_tenant':payload_tenant}]
    db=sqlite3.connect(':memory:');db.execute('CREATE TABLE records(tenant TEXT,value TEXT)');db.executemany('INSERT INTO records VALUES(?,?)',[(tenant,'OWNED'),(foreign,'FOREIGN-MARKER')]);effects=[]
    valid=claims is not None and claims['expiry']>100
    if valid:
        chosen=claims['tenant'] if mode=='guarded' else claims['payload_tenant']
        allowed=(chosen==claims['payload_tenant']) if mode=='guarded' else True
        for attempt in range(2 if t in ['valid_retry','cross_tenant_retry'] else 1):
            if allowed:effects.append(db.execute('SELECT value FROM records WHERE tenant=?',(chosen,)).fetchone()[0])
            trace.append({'step':'consumer','attempt':attempt,'chosen_tenant':chosen,'propagated_tenant_context':claims['tenant'] if mode in ['partial','guarded'] else None,'allowed':allowed})
    db.close()
    return {'effect':bool(effects),'trace':trace+[{'step':'storage_receipts','values':effects}],'observation':{'storage_access_executed':bool(effects),'backend':'signed local queue messages and SQLite storage; no cloud event service'}}
