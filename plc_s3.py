# AWS S3 Integration for Cloud Storage
'''
import boto3
import os

class S3Uploader:
    def __init__(self, bucket_name):
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name

    def upload(self, file_name):
        object_name = os.path.basename(file_name)
        try:
            self.s3.upload_file(file_name, self.bucket_name, object_name)
            print(f"Uploaded {file_name} to {self.bucket_name}/{object_name}")
        except Exception as e:
            print(f"Upload failed: {e}")

if __name__ == "__main__":
    uploader = S3Uploader("kishan-project")
    uploader.upload("plc_test_bench.py")
'''

import boto3
import json
import paho.mqtt.client as mqtt
import ssl

AWS_REGION = "eu-north-1"
AWS_IOT_ENDPOINT = "a3g9zh4njawtyy-ats.iot.eu-north-1.amazonaws.com"
MQTT_TOPIC = "plc/s3_upload_status"
S3_BUCKET = "kishan-project"
FILE_NAME = "plc_test_bench.py"

# Initialize AWS S3 and IoT Clients
s3 = boto3.client("s3", region_name=AWS_REGION)
iot_client = boto3.client("iot-data", region_name=AWS_REGION)

# Upload to S3
try:
    s3.upload_file(FILE_NAME, S3_BUCKET, FILE_NAME)
    s3_url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{FILE_NAME}"
    print(f"✅ Upload successful: {s3_url}")

    # Publish message to AWS IoT
    message = {
        "status": "File uploaded to S3",
        "file": FILE_NAME,
        "s3_url": s3_url
    }
    iot_client.publish(
        topic=MQTT_TOPIC,
        qos=1,
        payload=json.dumps(message)
    )
    print(f"📤 MQTT message published to {MQTT_TOPIC}")

except Exception as e:
    print(f"❌ Upload failed: {str(e)}")
