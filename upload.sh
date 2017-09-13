#!/bin/sh
ampy --port /dev/ttyUSB0 put ../micropython-dfplayer/dfplayer.py
ampy --port /dev/ttyUSB0 put ../micropython-dfplayer/scanplayer.py
ampy --port /dev/ttyUSB0 put ../micropython-mcp230xx/mcp.py
ampy --port /dev/ttyUSB0 put main.py

