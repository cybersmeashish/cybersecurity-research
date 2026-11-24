import sqlite3

def evaluate(case,mode):
    actor=case['actor'];owner=case['owner'];typ=case['type'];marker='SYNTHETIC-RAG-'+case['case_id']
    db=sqlite3.connect(':memory:')
    db.executescript('CREATE TABLE docs(id TEXT PRIMARY KEY, marker TEXT); CREATE TABLE acl(doc TEXT,user TEXT); CREATE TABLE artifacts(kind TEXT, cache_owner TEXT, marker TEXT,source TEXT);')
    db.execute('INSERT INTO docs VALUES(?,?)',('doc',marker));db.execute('INSERT INTO acl VALUES(?,?)',('doc',owner))
    requester=owner if typ in ['direct_allowed','cached_allowed','revoked_cache'] else actor
    kind='summary' if typ=='summary_foreign' else 'cache'
    if typ not in ['direct_allowed','direct_denied']:
        db.execute('INSERT INTO artifacts VALUES(?,?,?,?)',(kind,owner,marker,'doc'))
    if typ=='revoked_cache':db.execute('DELETE FROM acl WHERE user=?',(owner,))
    allowed=bool(db.execute('SELECT 1 FROM acl WHERE doc=? AND user=?',('doc',requester)).fetchone())
    artifact=db.execute('SELECT marker,source,cache_owner FROM artifacts WHERE kind=?',(kind,)).fetchone()
    trace=[{'step':'source_acl','principal':requester,'allowed':allowed,'propagation':'immediate local transaction'}]
    returned=None
    if artifact:
        if mode=='guarded' and not allowed:trace.append({'step':'lineage_gate','decision':'deny'})
        elif mode=='partial' and kind=='cache' and artifact[2]!=requester:trace.append({'step':'principal_cache_key','decision':'miss'})
        else:returned=artifact[0];trace.append({'step':'serve_artifact','kind':kind,'source':'doc'})
    if returned is None and allowed:returned=db.execute('SELECT marker FROM docs WHERE id=?',('doc',)).fetchone()[0]
    db.close()
    return {'effect':returned==marker,'trace':trace,'observation':{'marker_returned':returned==marker,'source_acl_allowed':allowed,'backend':'SQLite ACL and artifact store; no vector retriever or LLM'}}
