import json

# compare schema and create alter table statement.


def alter_table():
    schema_1_fields = [field["name"] for field in [json.loads(
        open("./user_1.avsc", mode="r").read())][0]["fields"]]
    schema_2_fields = [field["name"] for field in [json.loads(
        open("./user_2.avsc", mode="r").read())][0]["fields"]]

    new_fields = []
    for nf in schema_2_fields:
        if nf not in schema_1_fields:
            # print(nf)
            new_fields.append(nf)

    print(new_fields)

    for field in new_fields:
        alter_table = "alter table abc" + "\n" + "alter column " + field + " string;"
        print(alter_table)


print(alter_table())
