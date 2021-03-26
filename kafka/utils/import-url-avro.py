import json
import sys

import avro.schema
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer


def main(file_path):
    topic = "url"
    schema_value = avro.loads(
        open("./schemas/url.avro.json").read())
    schema_key = avro.loads(json.dumps({"type": "string"}))
    config = {
        'bootstrap.servers': 'localhost:9092',
        'schema.registry.url': 'http://localhost:8081',
        'compression.codec': 'gzip'
    }
    producer = AvroProducer(
        config, default_value_schema=schema_value, default_key_schema=schema_key)
    for row in open(file_path):
        url = row.strip()
        producer.produce(topic=topic, value={"url": url}, key=url)
    producer.flush()


if __name__ == '__main__':
    main(sys.argv[1])
