1. install OVOS op Raspberry PI 4B

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

nu werk het goed.....


2. installeren ovos-skill-melody
Plaats mp3 file in ./local/share
update pip
pip install git+....

nu werkt de uitgesproken tekst en audio file goed...

3. Download Jarvis voice records with sftp
on windows a ssh client is running
use sftp op ovos@raspOVOS
gebruikt ls for folder on service linux en lls for local op windows
gebruikt cd for service en lcd for windows
verander melody met Jarvis what is it you are trying

4. Bouw in melody een get request 
    url = f"https://api.open-meteo.com/v1/forecast"
    data = sliced(requests.get(url, params=args).json())
    return WeatherReport(data)

Backlog: verander I'm ready text in Jarvis startup mp3
Backlog: verander alarm met Jarvis wakeup
Backlog: bij licht commando jarvis as you wish
Backlog: Verander foute tekst in Jarvis impossible to synthesize
Backlog: Verander who are you in jarvis start up
Backlog: Gebruikt XTTS2 om Jarvis stem te klonen
