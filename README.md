### Raspberry Pi Passive-Infrared-Sensor-driven sound player

To play sounds through the headphone jack ('1'), rather than via HDMI:
```
sudo amixer cset numid=3 1
```

See http://www.raspberrypi.org/learning/parent-detector/worksheet for a similar use of PIR sensors.
