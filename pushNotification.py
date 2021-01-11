#!/usr/bin/python3

from pushbullet import Pushbullet
import yaml
import sys

class PushNotification:
    def __init__(self):
        with open("/home/payam/Workspace/piNotification/settings.yaml", 'r') as stream:
            try:
                self.settings = yaml.safe_load(stream)
                self.pushbullet = Pushbullet(self.settings['access_token'])
                self.device = self.pushbullet.get_device(self.settings['device_name'])
            except yaml.YAMLError as exc:
                print(exc)
    
    def notify(self, notificationType, message):
        self.device.push_note(notificationType, message)

pushNotification = PushNotification()
pushNotification.notify(sys.argv[1], sys.argv[2])