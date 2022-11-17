#! /bin/bash
#start this shit - start the microwave-scrips

sudo python3 microwave0.py &
sudo python3 microwave1.py &
sudo python3 microwave2.py &
sudo python3 mqtt-to-json.py &
sudo python3 discord_bot.py &

