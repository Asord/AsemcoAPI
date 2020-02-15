from os.path import exists, join
from os import mkdir, listdir
from shutil import copyfile

from AsemcoAPI.Tools.Json import loadf
from consts import configPath, quicklaunchFile, settingsFile, customMenusPath

def createFilesIfNotExists():
    if not exists(configPath):
        mkdir(configPath)
    if not exists(customMenusPath):
        mkdir(customMenusPath)

    if not exists(quicklaunchFile):
        copyfile("default/quicklaunch.json", quicklaunchFile)
    if not exists(settingsFile):
        copyfile("default/settings.json", settingsFile)

def getCustomMenus():
    menus = []
    for file in listdir(customMenusPath):
        if file.endswith(".json"):
            fdata = loadf(join(customMenusPath, file))

            pos = fdata["menu"].pop("position", -1)
            name = fdata["menu"].pop("name", "Unamed Menu")
            buttons = fdata["buttons"]
            menus.append( {"pos": pos, "name": name, "data": buttons} )

    return menus