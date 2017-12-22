# shadowsocks administrator

1. deploy shadowsocks on remote host vpnserv
ansible-playbook ssinstall.yml

2. add port 8399
ansible-playbook ssadd.yml
3. remove port 8339
ansible-playbook ssremove.yml
