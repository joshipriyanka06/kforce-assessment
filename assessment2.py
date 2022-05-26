import json

def remove_elementJson(s):
    f = open('test_payload.json')
    data = json.load(f) #reads json string into directory 
    # print(data.keys())
    # print(data)
    # del data[s]
    # print(data)
    for key in data:
        print(key)
        print(data[key])
        if s != key:

            if type(data[key]) is dict:
                data[key].pop(s, None)
                break
            
        else:
            data.pop(s,None)
            break

    print(data)
    with open('modified_json.json', 'w') as f:
        json.dump(data,f)
    
remove_elementJson('appdate')    