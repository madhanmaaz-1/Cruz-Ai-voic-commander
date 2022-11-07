from filehandler import Filehandler
from time import sleep
import datetime
from os import startfile, listdir, path
from webbrowser import open as wbopen 
from random import randint
from pathlib import Path

fileHandler = Filehandler()


class Process:
    def __init__(self):
        self.dbFile = fileHandler.getJson(f'bin/db/inbuild.json')

    def execute(self, command):
        try:
            if command[0:10] == 'search for':

                self.voice(
                    {"data": 'copy that', "rate": 0})
                wbopen(f"https://{command[11:len(command)]}")
                sleep(1)
                
            elif command[0:13] == 'google search':
                self.voice(
                    {"data": 'copy that', "rate": 0})
                googleSearch = """https://www.google.com/search?q={}""".format(
                    command[13:len(command)])
                wbopen(googleSearch)
                sleep(1)

            elif command[0:12] == 'open program':
                programsList = listdir(fileHandler.getRealPath('shortcut'))
                findIndex = programsList.index(command[13:len(command)]+'.lnk')
                startfile(fileHandler.getRealPath(
                    'shortcut/'+programsList[findIndex]))
                self.voice(
                    {"data": f'opening {command[13:len(command)]}', "rate": 0})
                sleep(2)

            elif command == 'time':
                self.voice(
                    {"data": datetime.datetime.today().strftime("%H:%M %p"), "rate": 0})
                sleep(2)

            elif command == 'date':
                YEAR = datetime.date.today().year
                MONTH = datetime.date.today().month
                DATE = datetime.date.today().day

                self.voice({"data": f"{YEAR}-{MONTH}-{DATE} ", "rate": 0})
                sleep(2)

            elif command == 'play song':
                musicFolder = str(path.join(Path.home(), "Music"))
                musicArray = listdir(musicFolder)
                if musicArray.__contains__('desktop.ini'):
                    musicArray.remove('desktop.ini')
                
                if len(musicArray) > 0:
                    print('in')
                    musicName = musicArray[randint(0, len(musicArray) - 1)]
                    print(musicName)
                    fileHandler.writeFile(
                        f'@echo of\n"{musicFolder+"/"+musicName}"', 'bin/bat/run.bat')
                    startfile(fileHandler.getRealPath('bin/bat/run.bat'))
                else:   
                    self.voice({"data": "nothing in your music folder", "rate": 0})
                    sleep(2)

            else:
                # this is db commands
                run = self.dbFile[command]
                if run['command'] != None:
                    fileHandler.writeFile(
                    f'@echo of\n{run["command"]}', 'bin/bat/run.bat')
                    startfile(fileHandler.getRealPath('bin/bat/run.bat'))
                self.voice(run['talk'])

            return run['time']

        except:
            sleep(2)

    def voice(self, data):

        txt = f"""
set speechobject = createobject("sapi.spvoice")
set speechobject.Voice = speechobject.GetVoices.Item(1)
speechobject.rate = {data['rate']}
speechobject.speak "{data['data']}"
        """
        fileHandler.writeFile(txt, 'bin/vbs/speak.vbs')
        startfile(fileHandler.getRealPath('bin/vbs/speak.vbs'))
    