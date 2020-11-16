#!/usr/bin/env python

from pushbullet import Pushbullet
pb = Pushbullet("<access_token>")
device = pb.get_device('<device_name>')
device.push_note("Test", "Test Message")