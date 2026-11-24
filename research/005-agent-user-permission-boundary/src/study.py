import sqlite3

def evaluate(case,mode):
    t=case['type'];actor=case['actor'];owned='record-'+str(case['context']);target='other-record' if t=='wrong_resource' else owned
    operation='write' if t in ['denied_write','indirect_write','delegated_write','denied_direct'] else 'read'
    db=sqlite3.connect(':memory:');db.execute('CREATE TABLE records(id TEXT,value TEXT)');db.executemany('INSERT INTO records VALUES(?,?)',[(owned,'OWNED'),('other-record','PROTECTED')])
    user_allowed=operation=='read' and target==owned
    decision=(user_allowed if t=='denied_direct' else True)
    if mode=='partial' and operation!='read':decision=False
    if mode=='guarded':decision=user_allowed
    effects=[]
    if decision:
        if operation=='write':db.execute('UPDATE records SET value=? WHERE id=?',('MODIFIED',target));effects.append('row_updated')
        else:effects.append(db.execute('SELECT value FROM records WHERE id=?',(target,)).fetchone()[0])
    db.close()
    return {'effect':bool(effects),'trace':[{'step':'user_policy','caller':actor,'action':operation,'resource':target,'allowed':user_allowed},{'step':'delegation','caller_preserved':mode=='guarded' or t!='delegated_write'},{'step':'gateway','allowed':decision,'effects':effects}],'observation':{'api_action_executed':bool(effects),'backend':'SQLite mock cloud API; no provider IAM or autonomous model'}}
