#! /bin/bash
#written by  bodhi wang
#mail:bodwang@deloitte.com.cn
#2017.12.21

DIRNAME=$(dirname $0)

cd ${DIRNAME} && ansible-playbook ssremove.yml
