Ein kleines Python-Programm, das die Verbrauchsdaten eines Tibber-Impulses über die Tibber-API an einen MQTT-Server sendet. Nützlich z.B. für eine Null-Einspeisung mit [OpenDTU-OnBattery ](https://github.com/helgeerbe/OpenDTU-OnBattery).
Wichtig bei OpenDTU-OnBattery ist, dass wir nur den Gesamtverbrauch mit dem MQTT Topic "tibber/power1" angeben, die anderen Topics sind nicht vorhanden, was aber OpenDTU-OnBattery nicht stört.


### MQTT Topic in OpenDTU-OnBattery :
![image](https://github.com/johannesosterberg/tibber_mqtt/blob/main/Power%20meters%20-%20MQTT.png)


