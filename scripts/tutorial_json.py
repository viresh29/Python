import json
import pandas as pd
import numpy as np

ps_1 = '''
{
    "people" : [
        {
            "name" : "John Smith",
            "phone" : "222-111-0000",
            "emails" : ["johnsmith@bogusemail.com", "john-smith@work-place.com"],
            "has_license" : false
        },
        {
            "name" : "Jane Doe",
            "phone" : "267-131-0054",
            "emails" : null,
            "has_license" : true
        }
    ]
}
'''


ps_2 = '''
{
    "people" : [
        {
            "name" : "John Smith",
            "phone" : "222-111-0000",
            "emails" : ["johnsmith@bogusemail.com", "john-smith@work-place.com"],
            "has_license" : false
        },
        {
            "name" : "Jane Doe",
            "phone" : "267-131-0054",
            "emails" : "jdoe@email.com",
            "has_license" : true
        }
    ]
}
'''

l1 = ps_1.split()
l2 = ps_2.split()
print(set(l1) - set(l2))
print(set(l2) - set(l1))

ps1 = json.loads(ps_1)
ps2 = json.loads(ps_2)

df1 = pd.json_normalize(ps1['people'])
df2 = pd.json_normalize(ps2['people'])

print(df1)

print(df1 == df2)


a = json.dumps(ps1, sort_keys=True)
b = json.dumps(ps2, sort_keys=True)

print(a == b)
