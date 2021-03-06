#! /usr/bin/python3

import os
import subprocess
import sys
sys.path.append("..")

from pyCommon.commonOps import *

def installZsh():
    installSoftWare("zsh")

def installOhMyZsh():
    installSoftWare("curl wget")
    homePath = os.path.expanduser("~")
    newHomepath = homePath.replace("/","\/" )
    #sed -n 's/\/home\/.*\/\.oh/${HOME}/p' ~/.zshrc
    runCommand("[ -f ~/.zshrc ] && sed -i 's/\/home\/.*\/.oh/"+newHomepath+"\/.oh/g' ~/.zshrc || true")
    runCommand("sh -c \"$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)\"")
    #runCommand("chsh -s /bin/bash")   

def installPlugins():
    #auto-suggestion
    runCommand("[ ! -d ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions ] && git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions || true")

def copyMyConf():
    runCommand("[ -f ~/.zshrc ] && mv ~/.zshrc ~/.zshrc.backup.myDevEnv || true")
    runCommand("cp .zshrc ~/.zshrc")
    homePath = os.path.expanduser("~")
    newHomepath = homePath.replace("/","\/" )
    runCommand("sed -i 's/\/home\/.*\/.oh/"+newHomepath+"\/.oh/g' ~/.zshrc")

def updateConfZsh():
    os.chdir("zsh")
    runCommand("[ -f ~/.zshrc ] && mv -f ~/.zshrc ~/.zshrc.backup.myDevEnv || true")
    runCommand("cp .zshrc ~/.zshrc")
    os.chdir("../")

def collectZsh():
    os.chdir("zsh")
    runCommand("[ -f .zshrc ] && rm .zshrc || true")
    runCommand("[ -f ~/.zshrc ] && cp ~/.zshrc .zshrc")
    os.chdir("../")
    
def installZshAll():
    os.chdir("zsh")
    installZsh()
    installOhMyZsh()
    installPlugins()
    copyMyConf()
    os.chdir("../")

def installZshAllTest():
    print("installZsh")

if __name__ == "__main__":
   os.chdir("../")
   installZshAll()
