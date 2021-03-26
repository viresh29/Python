import json
import sys

from kafka import KafkaProducer


def main(file_path, topic):
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092', client_id='url-importer',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'), compression_type='gzip')
    for row in open(file_path):
        producer.send(topic, {"url": row.strip()})

    producer.flush()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
