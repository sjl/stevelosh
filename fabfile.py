from fabric.api import *

def clean():
    local('rm -rf ./deploy')

def regen():
    clean()
    local('hyde -g -s .')

def serve():
    local('hyde -w -s .')

def reserve():
    regen()
    serve()
