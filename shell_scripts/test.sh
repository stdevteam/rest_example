#!/usr/bin/env bash

export WORKON_HOME=/var/envs
export PROJECT_HOME=/var/www/rest_example
export VIRTUALENVWRAPPER_HOOK_DIR=/var/envs/bin
export PIP_RESPECT_VIRTUALENV=true
export IS_LOCAL=1

source /usr/local/bin/virtualenvwrapper.sh
source /var/envs/rest_example/bin/activate

cd /var/www/rest_example
reset

python manage.py test "$@"