import sys
import uuid

from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError


def main(topic):
    config = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': uuid.uuid4(),
        'schema.registry.url': 'http://127.0.0.1:8081',
        'auto.offset.reset': 'earliest'}
    consumer = AvroConsumer(config)
    consumer.subscribe([topic])
    while True:
        try:
            msg = consumer.poll(10)

        except SerializerError as e:
            print("Message deserialization failed for {}: {}".format(msg, e))
            break
        except KeyboardInterrupt:
            break

        if msg is None:
            continue

        if msg.error():
            print("AvroConsumer error: {}".format(msg.error()))
            continue

        print('Message Value - ', msg.value())
        print('Message Key - ', msg.key())
        print('Topic - ', msg.topic())
        print('Pattition - ', msg.partition())
        print('Offset - ', msg.offset())

    consumer.close()


if __name__ == '__main__':
    main(sys.argv[1])
