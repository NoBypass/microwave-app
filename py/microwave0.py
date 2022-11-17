import paho.mqtt.client as mqtt
import json
import datetime

microwaves = 3


MQTT_IP_ADDRESS = '10.0.103.157'
MQTT_USER = "ioeuser"
MQTT_PASSWORD = "MQQT.LoremIpsum"


def on_connect(client, userdata, flags, rc):
    for i in range(microwaves):
        client.subscribe("microwaves/nr" + str(i))


done = []
def add(msg):
    if len(done) == microwaves:
        push(done)
        done.clear()
    else:
        toPush = {
            "microwave": msg[0]["measurement"],
            "date": str(msg[0]["time"]),
            "on": numToBoolean(msg[0]["fields"]["boolean"])
        }
        if validate(toPush): done.append(toPush)
        else: return


def validate(args):
    for i in range(len(done)):
        mic = done[i]['microwave']
        if mic == args['microwave']: return False
    return True


def push(msg):
    print(msg)
    with open('../microwave-app/src/db.json') as fp:
        list = json.load(fp)
    list.append(msg)
    with open('../microwave-app/src/db.json', 'w') as json_file:
        json.dump(list, json_file, indent=4, separators=(',', ': '))


def numToBoolean(num):
    if num == 0: return True
    else: return False


def on_message(client, userdata, msg):
    msg_decoded = msg.payload.decode("utf-8")
    msg_json = json.loads(msg_decoded)
    timestamp = datetime.datetime.utcnow()
    body = [
        {
            "measurement": int(msg_json["name"]),
            "time": timestamp,
            "fields": {
                "boolean": int(msg_json["running"])
            }
        }
    ]
    add(body)



MQTT_CLIENT = mqtt.Client("MQTT_PYTHON")
MQTT_CLIENT.on_connect = on_connect
MQTT_CLIENT.on_message = on_message
MQTT_CLIENT.username_pw_set(username=MQTT_USER, password=MQTT_PASSWORD)
MQTT_CLIENT.connect(MQTT_IP_ADDRESS, 1883, 60)
MQTT_CLIENT.loop_forever()
