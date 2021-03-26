import json
import sys

from kafka import KafkaConsumer


def main():
    topic = sys.argv[1]
    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092',
                             auto_offset_reset='latest', group_id='tesat',
                             enable_auto_commit=False,
                             )
    for msg in consumer:
        print(msg.value, msg.partition, msg.offset)


if __name__ == '__main__':
    main()
