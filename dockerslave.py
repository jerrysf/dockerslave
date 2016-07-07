import os
import sys
import subprocess
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class dockerslave():
    '''Class to run docker commands'''

    def __init__(self, image=None, volume=None):
        logger.info('Initialize dockerslave instance')
        self.image = image
        self.volume = volume

    def pull_image(self):
        logger.info('Start to pull docker image')
        pull_result = subprocess.call(['docker', 'pull', self.image])
        if pull_result == 0:
            print "Docker pull succeed!"
        else:
            print "There is something wrong with Docker pull! Exit...!"
            sys.exit()

    def start_container(self, command):
        logger.info('Start to run container')
        run_result = subprocess.call(['docker', 'run', '-u', 'username', '-v', self.volume, self.image, '/bin/sh', '-c', command])
        if run_result == 0:
            print "Docker run succeed!"
        else:
            print "There is something wrong with Docker run! Exit...!"
            sys.exit()
