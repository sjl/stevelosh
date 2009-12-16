from fabric.api import *

def regen():
    local('hyde -g -s .')

def serve():
    local('hyde -w -s .')
