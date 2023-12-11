import json

simple_json = '{"name": "Tejaswi","languages": [ "Java", "Python"]}'
#'loads' - for plain json, 'load'- for external json file
json_dict = json.loads(simple_json)
print(json_dict.get("languages")[1])

#parsing external json file
with open('json_data/data.json') as json_file:
    external_json_file_data = json.load(json_file)
    # getting batter_list from the external json
    batter_list = external_json_file_data.get('batters').get('batter')
    for batter in batter_list:
        if batter.get('id') == '1003':
            print(batter.get('type'))
            assert batter.get('type') == "Blueberry"

#comparing two dicts
#used same data.json but chnged few values and saved as data2.json
with open('json_data/data2.json') as diff_json:
    diff_json_data = json.load(diff_json)
    assert  not diff_json_data == external_json_file_data