"""
Input : ["foo", {"bar":["baz",null,1.0,2]}]
Output :
[
    "foo",
    {
        "bar":
        [
            "baz",
            null,
            1.0,
            2
        ]
    }
]
"""
import json


def pretty_json(json_object, space_unit=4):
    json_str = json.dumps(json_object)
    print 'json_str: ', json_str
    spaces = space_unit
    final_json = [json_str[0]]
    n = len(json_str)
    index = 0
    while(index < n-1):
        index += 1
        # ignore spaces
        if json_str[index] == ' ':
            continue
        if json_str[index] in ['{', '[']:
            final_json.append(' '*spaces+json_str[index])
            spaces += space_unit
            continue
        elif json_str[index] in ['}', ']']:
            spaces -= space_unit
            final_json.append(' '*spaces+json_str[index])
            continue
        cur_line = ''
        while(index < n-1 and json_str[index] not in [',', '{', '[', ']', '}']):
            if json_str[index] != ' ':
                cur_line += json_str[index]
            index += 1
        if json_str[index] in ['{', '[', '}', ']']:
            index -= 1
    if len(cur_line) == 0:
        final_json[-1] += json_str[index]
    else:
        cur_line = ' '*spaces+cur_line+json_str[index]
        final_json.append(cur_line)
    return final_json


if __name__ == '__main__':
    json_object = {'foo', {'bar': ('baz', None, 1.0, 2)}}
    json_object = {"c": 0, "b": 0, "a": 0}
    json_object = {1,2,3,{'4': 5, '6': 7}}
    json_object = {"id": "0001","type": "donut","name": "Cake","ppu": 0.55, "batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" }]}
    json_object = {"id":100,"firstName":"Jack","lastName":"Jones","age":12}
    json_object = {'A':'B','C':{'D':'E','F':{'G':'H','I':'J'}}}
    # json_object = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"

    for each in pretty_json(json_object):
        print each
