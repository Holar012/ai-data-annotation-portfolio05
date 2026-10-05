from pathlib import Path
import json,csv
root=Path(__file__).parent
count=0
for line in (root/'projects/01-ner/ner_sample.jsonl').read_text().splitlines():
 d=json.loads(line)
 for e in d['entities']:
  a,b=e['start'],e['end'];span=d['text'][a:b]
  assert 0<=a<b<=len(d['text']) and span==span.strip() and not span.endswith('.'), (e,span)
  assert e['label'] in {'PERSON','ORG','LOCATION','DATE','MONEY'}
  count+=1
rows=list(csv.DictReader((root/'projects/02-text-classification/classification_sample.csv').open()))
for r in rows:
 assert r['sentiment'] in {'POSITIVE','NEGATIVE','NEUTRAL'}
 assert r['primary_intent'] in r['multi_labels'].split('|')
 assert r['rationale']
for line in (root/'projects/03-relation-extraction/relations_sample.jsonl').read_text().splitlines():
 d=json.loads(line);assert d['head'] in d['text'] and d['tail'] in d['text']
def bounds(v):return tuple(map(int,v.split('-')))
for r in csv.DictReader((root/'projects/04-video-shot-segmentation/shot_annotations.csv').open()):
 assert r['transition_type'] in {'CUT','DISSOLVE','FADE','NO_TRANSITION'}
 ranges=[bounds(r[k]) for k in ['shot_1_frames','transition_frames','shot_2_frames'] if r[k]]
 for a,b in ranges:assert 0<=a<=b
 for prev,nxt in zip(ranges,ranges[1:]):assert prev[1]+1==nxt[0]
 if r['transition_type']=='CUT':assert int(r['boundary_frame'])==bounds(r['shot_2_frames'])[0] and not r['transition_frames']
llm=json.loads((root/'projects/06-llm-evaluation/evaluation_sample.json').read_text());assert llm['preferred']=='A'
assert len(llm['response_a'].splitlines())==2
print(f'Structural checks passed: {count} NER spans, {len(rows)} classification rows, relation records, video ranges and LLM sample. Semantic quality requires human review.')
