"""
"""
import json


def pretty_json(json_object, space_unit='\t'):
    json_str = json.dumps(json_object)
    json_str = '{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":None,"State":None},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":None,"Ads":None},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}'
    # Todo: Put commas inthe same line as closing braces
    spaces ,final_json, index = [], [], 0
    cur_line = []
    while(index < (len(json_str))):
        if json_str[index] in ['{', '[']:
            # Add the cur_line first and then increase the spaces indent
            if any(any(char != '\t' for char in str) for str in cur_line):
                final_json.append(''.join(cur_line))
            final_json.append(''.join(spaces)+json_str[index])
            spaces.append(space_unit)
            cur_line = [''.join(spaces)]
        elif json_str[index] in ['}', ']']:
            # b'coz closed paran is always on next line with decreased spaces
            # don't print this line if this is all spaces
            if any(any(char != '\t' for char in str) for str in cur_line):
                final_json.append(''.join(cur_line))
            spaces.pop()
            final_json.append(''.join(spaces)+json_str[index])
            cur_line = [''.join(spaces)]
        elif json_str[index] == ',':
            final_json.append(''.join(cur_line)+',')
            cur_line = [''.join(spaces)]
        elif json_str[index] != ' ':
            # if cur char is a normal char
            cur_line.append(json_str[index])
        index += 1
    return final_json


if __name__ == '__main__':
    # json_object = {'foo', {'bar': ('baz', None, 1.0, 2)}}
    # json_object = {"c": 0, "b": 0, "a": 0}
    # json_object = {1,2,3,{'4': 5, '6': 7}}
    json_object = {"id": "0001","type": "donut","name": "Cake","ppu": 0.55, "batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" }]}
    # json_object = {"id":100,"firstName":"Jack","lastName":"Jones","age":12}
    # json_object = {'A':'B','C':{'D':'E','F':{'G':'H','I':'J'}}}
    json_object = {"A":"B","C":{"D":"E","F":{"G":"H","I":"J"}}}

    print 'json_str: ', json_object
    for each in pretty_json(json_object):
        print each
