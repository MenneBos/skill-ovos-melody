# 1 install OVOS op Raspberry PI 4B

Start ovos-messagebus.service\
No logs, found one line in skills logs\
Seems to be running

start ovos-PHAL.service
Found error in Phal logs\
2025-02-14 23:12:25.494 - PHAL - ovos_PHAL.service:load_plugins:94 - ERROR - failed to load PHAL plugin: ovos-PHAL-plugin-wallpaper-manager\
No GUI installed on RaspOVOS. Could be the RC of not loading wallpaper-manager\
ovos-phal.service in running

Start ovos-audio.service
No major issue found in audio logs

Start ovos-listener
Found error in listener logs
PermissionError: [Errno 13] Permission denied: '/home/ovos/.local/share'
RC is there is no share folder at all

Start ovos-core.service
ovos-core continue to restart due to missing folder.
this is shown on journalctl --user | grep ovos

I created a folder ~/.local/share and changed the owner and group name to ovos

I change the STT driver to chromium door mycroft.conf aan te passen
Chromium plugin was al geinstalleerd

I changed to wake word to Jarvis by mycroft.conf \
Openwakework plugin was al geinstalleerd
```
  "listener": {
    "wake_word": "hey_jarvis",
    "VAD": {
      "module": "ovos-vad-plugin-silero"
    }
  },
  "hotwords": {
    "hey_mycroft": {
        "module": "ovos-ww-plugin-openwakeword"
    },
    "hey_jarvis": {
        "module": "ovos-ww-plugin-openwakeword"
    }
  },
```
Dit werkt goed

I disabled WiFi, as connection is on-off and it is cabled anywat
```Bash
sudo systemctl disable wpa_supplicant
sudo systemctl stop wpa_supplicant
sudo systemctl status wpa_supplicant
```
this doesn't seems to avoid WiFi to satrt at reboot
I used 
```
sudo rfkill block wifi
```
Dit werkt goed.....


# 2. installeren ovos-skill-melody
Plaats mp3 file in ./local/share
```Bash
  update pip
  pip uninstall ovos-skill-melody #package name can be found in METADATA in dist-info folder
  pip install git+https://github.com/MenneBos/skill-ovos-melody.git
```
play mp3 files with mpg123 file
nu werkt de uitgesproken tekst en audio file goed...

# 3. Download Jarvis voice records with sftp
Ik heb de soundbytes folder in GitHub toegevoegd. In deze folder staan de genormaliseerde jarvis soundclips (wav and mp3)\
Bij een pip install komen die in ~/.venvs/ovos/lib/python3.11/site-packages/ovos_skill_melody/soundbytes\
Update config file met juiste pad, update ovos-skill-boot-finished, deze __init.py__\
Include MANIFEST.in file met path naar sound bytes files

Dit werkt goed

__Open Point\
Sound volume low after break of alarm with reamp up volume. Top ramping up\
Set in config to false, still not stopping and bleep is still the standard\
Possible solution is to alter the defaults if mycroft.conf is not read. Look at ovos-skill-alert util folder and config.py
__

Alternative solution to put mp3 on RaspberryPI:\
on windows a ssh client is running. Use sftp op windows cmdline: >sftp ovos@192.168.5.126. Gebruikt ls for folder on service linux en lls for local op windows\
Gebruikt cd for service en lcd for windows. Verander melody met Jarvis what is it you are trying/


# 4. Bouw in melody een get request 
Gebruik de volgende code\
Check RbPI network Sandbox with Homey network Ziggo\
Add in Securty tab of UniFi to block ip rage 192.168.1.1 -192.168.1.44 & 192.168.1.46-192.168.255.255
```python
  import requests
  url = f"http://192.168.1.45/api/manager/logic/webhook/Kantoor/?tag=Menne"
  url = f"http://192.168.1.45/api/manager/logic/webhook/Terre/?tag=SkyRadio"
  data = requests.get(url)
  print(data.json())
```
Dit werkt goed

# 5. verander I'm ready text in Jarvis startup mp3
Het bericht dat de boot is afgerond staat in skill_ovos_boot_finished\
In deze code kan je kiezen tussen een dialog gesporken tekst of een sound.\
Plaats in conf twee regels\
"speak_ready": false,\
"ready_sound": true,\
In __init__ code op regel 191 de code vervangen met \
self.play_audio("/home/ovos/.local/share/Voicy_Jarvis_Start_Up.mp3", False)\
Adjustment: Speak is still used even is "speak_ready": false\
empty the speak.dialog file\

Dit werkt goed

# 6. geluid normaliseren tussen speak and sound
Ik heb de Jarvis soundbits genormailseerd met Audacity
Open geluidsfile en selecteer met ctl-a
Tab "effects" en dan geluid en normaliseer
Experteer audiobestand als mp3 of wav

# 7. verander de alarm geluid
OVOS gebruikt ovos-skill-alerts\
In de config file heb ik de volgende configuratie geplaatst\
```
  "sound_alarm": "/home/ovos/.venvs/ovos/lib/python3.11/site-packages/skill_ovos_melody/soundbytes/Clearly_You_Dont_Want_To_Get_Up.mp3",
  "sound_timer": "/home/ovos/.venvs/ovos/lib/python3.11/site-packages/skill_ovos_melody/soundbytes/Clearly_You_Dont_Want_To_Get_Up.mp3",
  "escalate_volume": false,
  "speak_alarm": false,
  "speak_timer": false,
```
Lijkt niet te werken, de beep sound wordt nog steeds default uitgevoerd. Ook langzaam opvoeren geluid met false werkt ook niet
Check of de config wel gevinden wordt.


# Backlog
| Backlog| Item|
| ------| -----|
|Backlog:| Verander uitgesproken tekst in ovos als ie het niet begrijpt met impossible_to_synthesize|
|Backlog:| Gebruikt XTTS2 om Jarvis stem te klonen: je kan de hele setup plus UI vinden bij https://github.com/BoltzmannEntropy/xtts2-ui|
