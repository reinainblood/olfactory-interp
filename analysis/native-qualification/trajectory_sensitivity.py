"""Post-hoc descriptive first-divergence check; technical canaries only, no model calls."""
import json
import numpy as np
from pathlib import Path
from hashlib import sha256
Q=Path(__file__).resolve().parent
def main():
    rows=[]
    for node in ('primary','b','c'):
        for cp in sorted((Q/node).glob('*-clean/response.json')):
            clean=json.loads(cp.read_text())
            for arm in ('zero_receipt','one_ulp'):
                other=cp.parent.with_name(cp.parent.name[:-5]+arm)/'response.json'
                if not other.exists():continue
                edit=json.loads(other.read_text());x=clean['output_ids'];y=edit['output_ids']
                if clean['input_ids']!=edit['input_ids'] or clean['sample']['seed']!=edit['sample']['seed']:raise ValueError('not a matched case')
                j=next((i for i,(a,b) in enumerate(zip(x,y)) if a!=b),None)
                changed={}
                if j is not None:
                    for token in (str(x[j]),str(y[j])):
                        a=(clean['output_logprobs'][j] or {}).get(token,{}).get('logprob'); b=(edit['output_logprobs'][j] or {}).get(token,{}).get('logprob')
                        changed[token]={'clean_logp':a,'edit_logp':b,'difference':b-a if a is not None and b is not None else None}
                layers={}
                xcap=cp.parent/'captures.npz';ycap=other.parent/'captures.npz'
                if xcap.exists() and ycap.exists():
                    with np.load(xcap,allow_pickle=False) as aa, np.load(ycap,allow_pickle=False) as bb:
                        for layer in (47,51):
                            xa=aa[f'L{layer}'].astype('float64');ya=bb[f'L{layer}'].astype('float64')
                            delta=ya-xa;norm=float(np.linalg.norm(delta))
                            layers[str(layer)]={'changed_dimensions':int(np.count_nonzero(delta)),'total_dimensions':len(xa),
                                'max_absolute_change':float(np.max(np.abs(delta))),'delta_norm':norm,
                                'fraction_of_clean_norm':norm/float(np.linalg.norm(xa))}
                rows.append({'node':node,'base':cp.parent.name,'arm':arm,'seed':clean['sample']['seed'],'equal_prompt':True,
                             'same_cue_token_layers':layers,
                             'clean_output_n':len(x),'edited_output_n':len(y),'first_different_output_offset':j,
                             'first_divergence_logprob':changed,'identical_tokens':x==y,
                             'clean_answer':clean['message']['content'],'edited_answer':edit['message']['content'],
                             'raw_sha256':[sha256(cp.read_bytes()).hexdigest(),sha256(other.read_bytes()).hexdigest()]})
    (Q/'trajectory-sensitivity.json').write_text(json.dumps({'scope':'Post-hoc technical sensitivity on two named development cases; same prefix up to first divergence only. No assertion of odor identity or welfare.','comparisons':rows},indent=2)+'\n')
    print('paired complete comparisons',len(rows))
if __name__=='__main__':main()
