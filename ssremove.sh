#! /bin/bash
#written by  bodhi wang
#mail:jyxz5@qq.com
#2017.12.21
set -x

DIRNAME=$(dirname $0)

cd ${DIRNAME} && ansible-playbook ssremove.yml
