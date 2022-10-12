import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {rc}')

def on_message(client, userdata, msg):
    print(f'topic: {msg.topic}, message: {msg.payload}')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('broker.hivemq.com', 1883, 60)

client.subscribe('waltz/test')

client.loop_forever()

# subscribe.callback(on_message, "waltz/test", hostname="broker.hivemq.com")
