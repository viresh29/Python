from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError
from confluent_kafka import OFFSET_INVALID, Consumer, TopicPartition

from confluent_kafka.avro.cached_schema_registry_client import \
    CachedSchemaRegistryClient

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

topic = ''
config = {
    'bootstrap.servers': "",
    'group.id': '',
    'schema.registry.url': ""
}


class MicroBatchAvroConsumer(Consumer):
    def __init__(self, config, topic, timeout=10, timeout_counter=3, timeout_sleep=10, consumer_number=1, consumer_id=1):
        self.topic = topic
        self.timeout = timeout
        self.timeout_counter = timeout_counter
        self.timeout_sleep = timeout_sleep
        self.unread_partition_offset = OFFSET_INVALID
        self.consumer_number = consumer_number
        self.consumer_id = consumer_id

        sr_conf = {key.replace("schema.registry.", ""): value
                   for key, value in config.items() if key.startswith("schema.registry")}

        if sr_conf.get("basic.auth.credentials.source") == 'SASL_INHERIT':
            sr_conf['sasl.mechanisms'] = config.get('sasl.mechanisms', '')
            sr_conf['sasl.username'] = config.get('sasl.username', '')
            sr_conf['sasl.password'] = config.get('sasl.password', '')

        ap_conf = {key: value
                   for key, value in config.items() if not key.startswith("schema.registry")}
        url = sr_conf.get('url')
        schema_registry = CachedSchemaRegistryClient(url)

        super(MicroBatchAvroConsumer, self).__init__(ap_conf)
        # self._serializer = SDPMessageSerializer(
        #     schema_registry)

    def _get_topic_partitions(self):
        print(1111)
        cluster_metadata = self.list_topics(self.topic, timeout=10)
        print(2222)
        topic_metadata = cluster_metadata.topics[self.topic]
        return [partition.id for partition in topic_metadata.partitions.values()]

    def get_events(self):
        partitions_list = self._get_topic_partitions()
        print(partitions_list)

    def __call__(self):
        self.get_events()


def kafka_issue_working():
    print('Starting consumer')
    c = AvroConsumer(config)
    print(c.list_topics().topics.keys())
    print('everything went OKAY!')


def kafka_issue_nt_working():
    consumer = MicroBatchAvroConsumer(config=config, topic=topic)
    print('Starting consumer')
    consumer()
    print('everything went OKAY!')


with DAG('kafka_issue', max_active_runs=3, schedule_interval=timedelta(minutes=5), default_args=default_args) as dag:
    t1 = PythonOperator(task_id='kafka_consumer_working',
                        python_callable=kafka_issue_working)
    t2 = PythonOperator(task_id='kafka_consumer_not_working',
                        python_callable=kafka_issue_nt_working)
