#! /bin/bash
#
# run.sh
# Copyright (C) 2015 george <george@george-ThinkPad-T420>
#
# Distributed under terms of the MIT license.
#


python build.py
python manage.py migrate
python manage.py runserver 0:8000

