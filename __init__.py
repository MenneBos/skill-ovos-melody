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
        self.play_audio("melody.mp3")
        #self.play_audio(self.melody_file)

def create_skill():
    return MelodySkill()
