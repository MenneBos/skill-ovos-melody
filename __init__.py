from ovos_workshop.skills.ovos import OVOSSkill
from ovos_bus_client.message import Message
import os

class MelodySkill(OVOSSkill):
    def __init__(self):
        super().__init__("MelodySkill")
        self.melody_file = os.path.join(os.path.dirname(__file__), "melody.mp3")

    def initialize(self):
        self.add_event('mycroft.melody.play', self.handle_play_melody)
        self.register_intent_file('PlayMelody.intent', self.handle_play_melody)

    def handle_play_melody(self, message: Message):
        self.speak_dialog("PlayMelody")
        self.play_audio("/home/ovos/.local/share/What_Is_It_You_Are_Trying_To_Achieve_Sir.mp3", True) 

def create_skill():
    return MelodySkill()
