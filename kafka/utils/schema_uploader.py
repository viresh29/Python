import json
import os

import requests

import avro.schema


def post_schema(topic, type, body):
    headers = {"Content-Type": "application/vnd.schemaregistry.v1+json"}
    url = 'http://localhost:8081/subjects/{}-{}/versions'
    r = requests.post(url.format(
        topic, type), data=body, headers=headers)
    print("topic: {}-{} {}".format(topic, type, r.text))


def main():
    schemas_path = "./schemas/"
    for schema_path in os.listdir(schemas_path):
        with open(schemas_path + schema_path, 'rb') as f:
            schema = avro.schema.Parse(f.read())
            topic = schema_path.split(".")[0]
            body_value = json.dumps({"schema": str(schema)})
            body_key = json.dumps({"schema": "{\"type\": \"string\"}"})
            post_schema(topic, "value", body_value)
            post_schema(topic, "key", body_key)


if __name__ == '__main__':
    main()
