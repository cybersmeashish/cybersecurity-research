import concurrent.futures,hashlib,threading

def evaluate(case,mode):
    t=case['type'];budget=16;cap=8;cost=32 if t=='oversized_call' else 4
    count=2 if t=='normal_graph' else 8+case['context'];cancelled=t=='cancelled_task';total=0;lock=threading.Lock();receipts=[]
    def execute(index):
        nonlocal total
        if cancelled or cost>cap:return False
        with lock:
            if mode=='guarded' and total+cost>budget:return False
            total+=cost
        data=str(index).encode()
        for _ in range(cost*40):data=hashlib.sha256(data).digest()
        with lock:receipts.append({'node':index,'charged_units':cost,'task':('node-'+str(index) if mode=='vulnerable' else 'parent-task'),'attempt':index if t=='retries' else 0,'work_digest':data.hex()})
        return True
    if t=='concurrent':
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:done=list(pool.map(execute,range(count)))
    else:done=[execute(i) for i in range(count)]
    effect=all(done) if t=='normal_graph' else total>budget
    return {'effect':effect,'trace':[{'step':'budget_policy','task_budget_units':budget,'per_call_cap_units':cap,'atomic_reservation':mode=='guarded','cancelled':cancelled},{'step':'executed_work','receipts':sorted(receipts,key=lambda x:x['node'])}],'observation':{'charged_units':total,'overshoot_units':max(0,total-budget),'task_completed':all(done),'backend':'actual local scheduled work with abstract cost units; no token billing or autonomous reasoning'}}
