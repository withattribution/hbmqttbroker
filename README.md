# hbmqttbroker

basic setup for automatically configuring ip from a sanely set up beaglebone black debian 8.8 4.4.62-ti-r105 jessie

```
pip install hbmqtt netifaces
```

included service file should be installed 

```
/lib/systemd/system/hbmqttbroker.service
```

then 

```
systemctl enable hbmqttbroker.service
systemctl daemon-reload
systemctl start hbmqttbroker.service
```
