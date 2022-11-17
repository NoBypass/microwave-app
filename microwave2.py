import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import json
import datetime

MQTT_IP_ADDRESS = '127.0.0.1'
MQTT_USER = "ioeuser"
MQTT_PASSWORD = "MQQT.LoremIpsum"

INFLUXDB_IP_ADDRESS = '127.0.0.1'
INFLUXDB_PORT = 8086
INFLUXDB_HTTP = 'http://'
INFLUXDB_USER = 'admin'
INFLUXDB_PASSWORD = 'Influx.LoremIpsum'
INFLUXDB_DATABASE = 'ioe'
INFLUXDB_CLIENT = InfluxDBClient(INFLUXDB_IP_ADDRESS, INFLUXDB_PORT, INFLUXDB_USER, INFLUXDB_PASSWORD, INFLUXDB_DATABASE)

def on_connect(client, userdata, flags, rc):
    client.subscribe("microwaves/nr2")

def on_message(client, userdata, msg):
    msg_decoded = msg.payload.decode("utf-8")
    msg_json = json.loads(msg_decoded)
    timestamp = datetime.datetime.utcnow()
    body = [
        {
            "measurement": "microwave2",
            "time": timestamp,
            "fields": {
                "boolean": int(msg_json["running"])
            }
        }
    ]
    print(body)
    INFLUXDB_CLIENT.write_points(body)


MQTT_CLIENT = mqtt.Client("MQTT_PYTHON")
MQTT_CLIENT.on_connect = on_connect
MQTT_CLIENT.on_message = on_message
MQTT_CLIENT.username_pw_set(username=MQTT_USER, password=MQTT_PASSWORD)
MQTT_CLIENT.connect(MQTT_IP_ADDRESS, 1883, 60)
MQTT_CLIENT.loop_forever()
