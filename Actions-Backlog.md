# 1 install OVOS op Raspberry PI 4B

Start ovos-messagebus.service
No logs, found one line in skills logs
Seems to be running

start ovos-PHAL.service
Found error in Phal logs
2025-02-14 23:12:25.494 - PHAL - ovos_PHAL.service:load_plugins:94 - ERROR - failed to load PHAL plugin: ovos-PHAL-plugin-wallpaper-manager
No GUI installed on RaspOVOS. Could be the RC of not loading wallpaper-manager
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

I changed to wake word to Jarvis by mycroft.conf 
Openwakework plugin was al geinstalleerd

I disabled WiFi, as connection is on-off and it is cabled anywat
```Bash
sudo systemctl disable wpa_supplicant
sudo systemctl stop wpa_supplicant
sudo systemctl status wpa_supplicant
```
nu werk het goed.....


# 2. installeren ovos-skill-melody
Plaats mp3 file in ./local/share
```Bash
  update pip
  pip uninstall ovos-skill-melody #package name can be found in METADATA in dist-info folder
  pip install git+https://github.com/MenneBos/skill-ovos-melody.git
```
nu werkt de uitgesproken tekst en audio file goed...

# 3. Download Jarvis voice records with sftp
on windows a ssh client is running
use sftp op windows cmdline: >sftp ovos@192.168.5.126
gebruikt ls for folder on service linux en lls for local op windows
gebruikt cd for service en lcd for windows
verander melody met Jarvis what is it you are trying

# 4. Bouw in melody een get request 
Gebruik de volgende code
Check RbPI network Sandbox with Homey network Ziggo
```python
  import requests
  url = f"http://192.168.1.45/api/manager/logic/webhook/Kantoor/?tag=Menne"
  url = f"http://192.168.1.45/api/manager/logic/webhook/Terre/?tag=SkyRadio"
  data = requests.get(url)
  print(data.json())
```

# 5. verander I'm ready text in Jarvis startup mp3
Het bericht dat de boot is afgerond staat in skill_ovos_boot_finished
In deze code kan je kiezen tussen een dialog gesporken tekst of een sound.
Plaats in conf twee regels
"speak_ready": false,
"ready_sound": true,
In __init__ code op regel 191 de code vervangen met 
self.play_audio("/home/ovos/.local/share/Voicy_Jarvis_Start_Up.mp3", False)
Adjustment: Speak is still used even is "speak_ready": false, or removed at all.
Check code and remove the IF statement in lines 193-194.
play mp3 fils with mpg123 file

# Backlog
| Backlog| Item|
| ------| -----|
|Backlog:| verander alarm met Jarvis wakeup|
|Backlog:| bij licht commando jarvis as you wish|
|Backlog:| Verander uitgesproken tekst in ovos als ie het niet begrijpt met impossible_to_synthesize|
|Backlog:| Gebruikt XTTS2 om Jarvis stem te klonen: je kan de hele setup plus UI vinden bij https://github.com/BoltzmannEntropy/xtts2-ui|
