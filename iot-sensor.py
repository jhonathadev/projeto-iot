from pickle import TRUE
import random
import time

from paho.mqtt import client as mqtt_client


broker = '127.0.0.1'
port = 1883
topic_human = "iothon/entrance/human"
topic_cat = "iothon/entrance/cat"
topic_mosquitto= "iothon/entrance/mosquitto"
topic_count = "iothon/entrance/count"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'mqttuser'
password = 'mqttpassword'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    #gato = 0
    #mosquito  = 0
    while(True):
        time.sleep(1)
        msg = random.randint(1,4)
        if(msg == 1): # Gato
            result = client.publish(topic_cat, msg)
            msg_count += 1
            client.publish(topic_count, msg_count)
            # result: [0, 1]
            status = result[0]
            if (status == 0):
                print("Gato capturado!")
        elif(msg == 2 ): # Mosquito
            result = client.publish(topic_mosquitto, msg)
            msg_count += 1
            client.publish(topic_count, msg_count)
            # result: [0, 1]
            status = result[0]
            if (status == 0):
                print("Mosquito capturado!")
        else: # Humano
            result = client.publish(topic_human, msg)
            msg_count += 1
            client.publish(topic_count, msg_count)
            # result: [0, 1]
            status = result[0]
            if (status == 0):
                print("Humano capturado!")
    #print(gato, mosquito)

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
