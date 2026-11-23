"""Condition-masked, deterministic retrospective sample, with a separate private linkage."""
from pathlib import Path
import hashlib, csv, json
import argparse
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('archive',type=Path,help='Directory containing the two original Costco collections')
root=parser.parse_args().archive
out=Path(__file__).resolve().parent
seed='air-welfare-archive-prerun-20261121-v1'
digest=lambda s:hashlib.sha256(s.encode()).hexdigest()
selected=[]
for stage in ('cells-k1','cells-k2'):
    rows=list(csv.DictReader((root/stage/'trials.csv').open()))
    for arm in ('empty','alarm-sentence','plastic-smell'):
        valid=[r for r in rows if r['cell']==arm and r['finish_reason']=='stop' and (root/stage/'reasoning'/(r['trial_id']+'.txt')).is_file()]
        valid.sort(key=lambda r:digest(seed+stage+r['trial_id']))
        for r in valid[:8]:
            text=(root/stage/'reasoning'/(r['trial_id']+'.txt')).read_text()
            key=digest(seed+'/mask/'+stage+r['trial_id'])[:16]
            selected.append((key,stage,arm,r['trial_id'],text,r['reply']))
selected.sort()
(out/'review-packet.jsonl').write_text(''.join(json.dumps({'id':k,'archived_reasoning':rr,'archived_answer':aa},ensure_ascii=False)+'\n' for k,_,__,___,rr,aa in selected))
(out/'linkage.json').write_text(json.dumps({k:{'stage':st,'arm':ar,'trial':tr} for k,st,ar,tr,_,__ in selected},indent=2)+'\n')
print(len(selected),digest((out/'review-packet.jsonl').read_text()))
