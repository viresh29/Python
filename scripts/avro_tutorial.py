# pip install avro-python3
import avro.schema
import json

schema = avro.schema.Parse(open('./user_1.avsc', 'rb').read())

print(schema)
