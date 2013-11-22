#coding:utf-8

import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

from fabric.state import env

from essay.tasks import build
from essay.tasks import deploy
#from essay.tasks import nginx
#from essay.tasks import supervisor

env.PROJECT = 'essay_demo_webpy'
#env.DEPLOY_HOST = '10.13.83.204'
#env.DEPLOY_USER = 'moon'
#env.DEPLOY_PATH = '/opt/deploy/'
#env.PROJECT_OWNER = 'clan'
#env.DEFAULT_BRANCH = 'master'
#env.PYPI_INDEX = 'http://10.13.83.194:9791/simple/'
