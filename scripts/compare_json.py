import json
import difflib

schema_1 = json.load(open('./user_1.avsc', mode='r'))
schema_2 = json.load(open('./user_2.avsc', mode='r'))

# compare 2 json files
print(schema_1 == schema_2)


def print_cross(s1set, s2set, message):
    for s in s1set:
        if not s in s2set:
            print(message % s)


s1names = set([field['name'] for field in schema_1['fields']])
s2names = set([field['name'] for field in schema_2['fields']])

print_cross(s1names, s2names,
            'Field "%s" exists in table1 and does not exist in table2')
print_cross(s2names, s1names,
            'Field "%s" exists in table2 and does not exist in table1')


def print_cross2(s1dict, s2dict, message):
    for s in s1dict:
        if s in s2dict:
            if s1dict[s] != s2dict[s]:
                print(message % (s, s1dict[s], s2dict[s]))


s1types = dict(zip([field['name'] for field in schema_1['fields']],  [
               str(field['type']) for field in schema_1['fields']]))
s2types = dict(zip([field['name'] for field in schema_2['fields']],  [
               str(field['type']) for field in schema_2['fields']]))


print_cross2(s1types, s2types,
             'Field "%s" has type "%s" in table1 and type "%s" in table2')
