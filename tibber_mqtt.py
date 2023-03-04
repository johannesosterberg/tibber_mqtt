#python 3.9
#Tibber lib tibber.py https://github.com/BeatsuDev/tibber.py
import time
import tibber
from paho.mqtt import client as mqtt_client

#Tibber API Token find unnder https://developer.tibber.com/
ACCESS_TOKEN = ""

#MQTT Broker Settings
broker = "ipadress"
port = 1883
client_id = 'Tibber_MQTT'
username = "change"
password = "change"


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
    
account = tibber.Account(ACCESS_TOKEN)
home = account.homes[0]   
@home.event("live_measurement") 
async def process_data(data):
  print("consumption:",data.power, "Wh")
  print("Timestamp:",data.timestamp)
  #timestamp = time.mktime(time.strptime(data.timestamp, '%Y-%m-%dT%H:%M:%S.000+01:00'))

  tibberpower = client.publish(topic='tibber/power1',payload=data.power,qos=1)
  tibberpower.wait_for_publish()
  print("MQTT is send:",tibberpower.is_published())
  last_update = time.strftime("%H:%M:%S %d.%m.%Y",  time.localtime())
  print("Last update:",last_update)
    
def when_to_stop(data):
  return True


client = connect_mqtt()
client.loop_start()

while True:
  home.start_live_feed(user_agent = "UserAgent/0.0.1", exit_condition = when_to_stop)
  time.sleep(5)
