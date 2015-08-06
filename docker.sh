#!/bin/bash
#
# docker.sh
# Copyright (C) 2015 kelly
#
# Distributed under terms of the MIT license.
#

##
## base setting option
##

img="rasca0027/ip2naiton:v1"
curr=`pwd`
port=8000
docker_work_dir=/srv/work
docker_run="docker run -i -e PYTHONPATH=$docker_work_dir --rm -p $port:$port -v $curr:$docker_work_dir -w $docker_work_dir -t $img "
ip=0



##
## initialize docker env
##

function init {
    ## running docker
    os=`uname`   
    case $os in
        "Linux" )
            Linux_init
        ;;
        "Darwin" )
            MAC_init
        ;;
        "*" )
            $?=0
        ;;
    esac

    if [ $? -ne 0 ]; then
        echo 'init failure'
        exit 1;
    fi

}


function MAC_init {   
    echo "initialize book2docker"
    echo "boot2docker version need >= 1.4"
    ip=`boot2docker ip`

    if [ `boot2docker status` != 'running' ]; then
        boot2docker init > /dev/null
        boot2docker start > /dev/null
    fi
    $(boot2docker shellinit)
}

function Linux_init {
    echo "initialize linux"    
}



##
## start
##


echo "start initialize..."
init > /dev/null
if [ $? -ne 0 ];then
    echo "initialize error"
    exit $?
fi

echo "initialize success"


case $1 in
    "test" )
        echo 'start testing...'    
        $docker_run python manage.py test
        ;;
    "build" )
        echo "start build"
        docker pull $img
        ;;
    "run" )
        shift 1
        $docker_run $@
        ;;
