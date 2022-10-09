from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka.schema_registry import SchemaRegistryClient

FILE_PATH = r"C:\Users\manish dogra\Desktop\KAFKA\restaurant_orders.csv"
columns=['Order Number','Order Date','Item Name','Quantity','Product Price','Total products']

API_KEY = 'DOOTQ3UIR7WJMEYA'
ENDPOINT_SCHEMA_URL  = 'https://psrc-vn38j.us-east-2.aws.confluent.cloud'
API_SECRET_KEY = 'xbPiEHty3lQmPySMMnhC9FAjljGjnxitCLq+Zz8OhhGDuQjE7ddrtEkT7ETO0Vwk'
BOOTSTRAP_SERVER = 'pkc-ymrq7.us-east-2.aws.confluent.cloud:9092'
SECURITY_PROTOCOL = 'SASL_SSL'
SSL_MACHENISM = 'PLAIN'
SCHEMA_REGISTRY_API_KEY = 'VQ7AGI4EJNE4CPDI'
SCHEMA_REGISTRY_API_SECRET = 'xBT/EutusYLM748f7h4demQkyJhsH8y+S0d9Wylb1D+wPCImbOtullnBXBIFwYXc'

def schema_config():
    # {'url':ENDPOINT_SCHEMA_URL,'basic.auth.user.info':{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}}
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"
    
    }
      
if __name__ == '__main__':

    
    schema_registry_conf = schema_config()
    topic = 'restaurent-take-away-data'
    consumer_conf = {'sasl.mechanism': SSL_MACHENISM,
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
                
                
    # configuration for schema registery client
    
    # creating object for schema regitry client()
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)
    val_schema = schema_registry_client.get_latest_version(subject_name='restaurent-take-away-data-value')
    schema_str = val_schema.schema.schema_str
    
    json_deserializer = JSONDeserializer(schema_str)

    consumer_conf.update({
                     'group.id': 'group1',
                     'auto.offset.reset': "earliest"})

    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])


    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            restaurent = json_deserializer(msg.value(), SerializationContext(msg.topic(), MessageField.VALUE))

            if restaurent is not None:
                print("User record {}: restaurent: {}\n"
                      .format(msg.key(), restaurent))
        except KeyboardInterrupt:
            break

    consumer.close()