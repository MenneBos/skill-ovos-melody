from ovos_workshop.skills.ovos import OVOSSkill
from ovos_bus_client.message import Message
import os
import requests

class MelodySkill(OVOSSkill):
    def __init__(self):
        super().__init__("MelodySkill")
        self.melody_file = os.path.join(os.path.dirname(__file__), "melody.mp3")

    def initialize(self):
        self.add_event('mycroft.melody.play', self.handle_play_melody)
        self.register_intent_file('PlayMelody.intent', self.handle_play_melody)

    def handle_play_melody(self, message: Message):
        # wait=True will block the message bus until the dialog is finished
        self.speak_dialog("hello.world", wait=True)
        # this will speak the string without translation
        self.speak("hello english folks")
        url = f"http://192.168.1.45/api/manager/logic/webhook/Terre/?tag=SkyRadio"
        data = requests.get(url)
        print(data.json())
        self.play_audio("/home/ovos/.venvs/ovos/lib/python3.11/site-packages/skill_ovos_melody/soundbytes/As_You_Wish.mp3", False) 

def create_skill():
    return MelodySkill()
