import json, glob, os, statistics as st

contributor_json_list = glob.glob(os.path.join('./contributors', '*.json'))
top_contributor_list = dict()

for contributor_file in contributor_json_list:
    with open(contributor_file) as f: json_obj = json.loads(f.read())
    if(len(json_obj) == 0 or type(json_obj[0]) != dict): continue
    top_contributor = sorted(json_obj, key=lambda user: -user['contributions'])[0]
    top_contributor_list[contributor_file] = top_contributor
print(top_contributor_list)
