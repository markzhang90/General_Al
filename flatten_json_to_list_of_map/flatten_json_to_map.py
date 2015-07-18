__author__ = 'mark'

json = {
    "uuid": "abc",
    "properties": {
        "sessionName": "Test session name",
        "waypoints": [
            {"uuid": "def", "properties": {"latitude": 3}}
        ]
    }
}

output = [

    {"uuid": "abc", "properties": {"sessionName": "Test session name", "waypoints": ["def"]}},

    {"uuid": "def", "properties": {"latitude": 3}}

]


def json_to_map(json, out):
    if isinstance(json, dict):
        dic_f = {}
        if "uuid" and "properties" in json:

            dic_s = {}
            dic_f["uuid"] = json.get('uuid')
            for key, value in json.get('properties').iteritems():
                list_level_t = []
                if isinstance(value, list):
                    for one_record in value:
                        if "uuid" and "properties" in json:
                            list_level_t.append(one_record.get('uuid'))
                            json_to_map(one_record, out)
                    dic_s[key] = list_level_t
                else:
                    dic_s[key] = value
            dic_f['properties'] = dic_s
            out.append(dic_f)

        return out
    return None


out = []
print(json_to_map(json, out))
