# MQTT Integration for AWS IoT (Updated for Latest API)
import paho.mqtt.client as mqtt
import ssl
import json
from plc_test_bench import MotorTestBench

'''import boto3
client = boto3.client('iot-data', region_name='eu-north-1')

response = client.publish(
    topic='plc/testbench',
    qos=1,
    payload='{"message": "AWS SDK test"}'
)

print(response)
'''
'''
AWS_IOT_ENDPOINT = "a3g9zh4njawtyy-ats.iot.eu-north-1.amazonaws.com"
MQTT_TOPIC = "plc/testbench"

CERTIFICATE_PATH = "/Users/kishan/Desktop/Kishan/aws_certs/device.pem.crt"
PRIVATE_KEY_PATH = "/Users/kishan/Desktop/Kishan/aws_certs/private.pem.key"
ROOT_CA_PATH = "/Users/kishan/Desktop/Kishan/aws_certs/AmazonRootCA1.pem"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to AWS IoT Core!")
    else:
        print(f"❌ Connection failed! Error Code: {rc}")

def on_publish(client, userdata, mid):
    print(f"📤 Message {mid} published successfully!")

def on_log(client, userdata, level, buf):
    print(f"📜 MQTT Log: {buf}")

class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.on_connect = on_connect
        self.client.on_publish = on_publish
        self.client.on_log = on_log  # Enable debugging logs

        self.client.tls_set(
            ROOT_CA_PATH, 
            certfile=CERTIFICATE_PATH, 
            keyfile=PRIVATE_KEY_PATH, 
            tls_version=ssl.PROTOCOL_TLSv1_2
        )
        self.client.connect(AWS_IOT_ENDPOINT, 8883, 60)
        self.client.loop_start()  # Ensures MQTT loop is running

    def publish(self, data):
        payload = json.dumps(data)
        print(f"📤 Publishing MQTT Message: {payload}")
        #self.client.publish(MQTT_TOPIC, payload, qos=1)
        result = self.client.publish(MQTT_TOPIC, payload, qos=1)  # Set QoS to 1
        print(f"🔎 Publish Result: {result.rc}")

if __name__ == "__main__":
    test_bench = MotorTestBench()
    mqtt_client = MQTTClient()

    test_bench.start_motor()
    test_bench.monitor_temperature()
    mqtt_client.publish(test_bench.log_data())
'''

import boto3
import json
from plc_test_bench import MotorTestBench

AWS_REGION = "eu-north-1"  # Replace with your AWS region
AWS_IOT_ENDPOINT = "https://a3g9zh4njawtyy-ats.iot.eu-north-1.amazonaws.com"
MQTT_TOPIC = "plc/testbench"

# Initialize AWS IoT Data Client
client = boto3.client("iot-data", region_name=AWS_REGION)

def publish_message(data):
    payload = json.dumps(data)
    print(f"📤 Publishing MQTT Message using AWS SDK: {payload}")

    response = client.publish(
        topic=MQTT_TOPIC,
        qos=1,
        payload=payload
    )

    print(f"✅ AWS SDK Publish Response: {response}")

if __name__ == "__main__":
    test_bench = MotorTestBench()

    test_bench.start_motor()
    test_bench.monitor_temperature()

    # Publish using AWS SDK
    publish_message(test_bench.log_data())
