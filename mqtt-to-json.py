import json
import paho.mqtt.client as mqtt

MQTT_IP_ADDRESS = '127.0.0.1'
MQTT_USER = "ioeuser"
MQTT_PASSWORD = "MQQT.LoremIpsum"
microwaves = [0, 0, 0]
def on_connect(client, userdata, flags, rc):
    client.subscribe("microwaves/nr0")
    client.subscribe("microwaves/nr1")
    client.subscribe("microwaves/nr2")

def on_message(client, userdata, msg):
    msg_decoded = msg.payload.decode("utf-8")
    msg_json = json.loads(msg_decoded)
    microwaves[int(msg_json["name"])] = int(msg_json["running"])
    print(microwaves)
    free = {"free":3}
    for micro in microwaves:
        free["free"] = free["free"] - micro
    outFile = open("free.json", "w")
    outFile.write(json.dumps(free))
    outFile.close()
    
    

MQTT_CLIENT = mqtt.Client("MQTT_PYTHON7")
MQTT_CLIENT.on_connect = on_connect
MQTT_CLIENT.on_message = on_message
MQTT_CLIENT.username_pw_set(username=MQTT_USER, password=MQTT_PASSWORD)
MQTT_CLIENT.connect(MQTT_IP_ADDRESS, 1883, 60)
MQTT_CLIENT.loop_forever()
client.run(TOKEN)