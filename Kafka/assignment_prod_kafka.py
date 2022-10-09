
from uuid import uuid4
from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
import pandas as pd


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

"""
def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

producer.produce(topic, key="key", value="value", callback=acked)

# Wait up to 1 second for events. Callbacks will be invoked during
# this method call if the message is acknowledged.
producer.poll(1)

"""
def get_car_instance(file_path):
    df=pd.read_csv(file_path)
    df=df.iloc[:,:]
    for data in df.values:
        data_in_dict = dict(zip(columns,data))
        yield data_in_dict
        

def to_dict(obj,ctx):
    return dict(obj)

def delivery_report(err, msg):
    """
    Reports the success or failure of a message delivery.
    Args:
        err (KafkaError): The error that occurred on None on success.
        msg (Message): The message that was produced or failed.
    """

    if err is not None:
        print("Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    print('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))

        
if __name__ == '__main__':
    
    # configuration for schema registery client
    schema_registry_conf = schema_config()
    # creating object for schema regitry client()
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)
    # get the latest version for value schema in registery 
    val_schema = schema_registry_client.get_latest_version(subject_name='restaurent-take-away-data-value')
    schema_str = val_schema.schema.schema_str
    # creating string serializer object for keys
    string_serializer = StringSerializer('utf_8')
    # creating json serializer object to serialize the values and we need to register this into schema registery
    json_serializer = JSONSerializer(schema_str, schema_registry_client, to_dict=None, conf=None)
    
    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
                
    producer = Producer(sasl_conf)
    topic = 'restaurent-take-away-data'
    
    print("Producing user records to topic {}. ^C to exit.".format(topic))
    #while True:
        # Serve on_delivery callbacks from previous calls to produce()
    producer.poll(0.0)
    try:
        cnt = 0
        for car in get_car_instance(file_path=FILE_PATH):
            
            print(car)
            producer.produce(topic=topic,
                            key=string_serializer(str(uuid4()), to_dict),
                            value=json_serializer(car, SerializationContext(topic, MessageField.VALUE)),
                            on_delivery=delivery_report)
            
            if (cnt == 2): break
            cnt += 1
            
    except KeyboardInterrupt:
        pass
    except ValueError:
        print("Invalid input, discarding record...")
        pass

    print("\nFlushing records...")
    producer.flush()
    # print(schema_registry_client.get_schema(100003))
    # print(schema_registry_client.get_subjects())
    
    
    
    