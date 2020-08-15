import json, glob, os, statistics as st

history_json_list = glob.glob(os.path.join('./dependencies_history', '*.json'))
oldest_version_list = dict()
for history_file in history_json_list:
    with open(history_file) as f: json_obj = json.loads(f.read())
    version_commit_time  = list(map(lambda version: (version, json_obj[version]['commit_time']), json_obj))
    oldest_version = sorted(version_commit_time, key=lambda tup: tup[0])[-1]
    oldest_version_list[history_file] = oldest_version
print(oldest_version_list)
