from ovos_workshop.skills.ovos import OVOSSkill
from ovos_bus_client.message import Message
import os
import requests

class MelodySkill(OVOSSkill):
    def __init__(self):
        super().__init__("MelodySkill")

    def initialize(self):
        self.add_event('mycroft.melody.play', self.handle_play_melody)
        self.register_intent_file('PlayMelody.intent', self.handle_play_melody)

    def handle_play_melody(self, message: Message):
        # wait=True will block the message bus until the dialog is finished
        self.speak_dialog("Here is a melody", wait=True)
        # this will speak the string without translation
        self.speak("Listen to the melody")

        self.play_audio("/home/ovos/.venvs/ovos/lib/python3.11/site-packages/skill_ovos_melody/soundbytes/What_Is_It_You_Are_Trying_To_Achieve_Sir.mp3", False) 

def create_skill():
    return MelodySkill()
