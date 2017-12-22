# shadowsocks administrator

1. Deploy shadowsocks on remote host vpnserv

   ansible-playbook ssinstall.yml

2. Add port 8399 to listen

   ansible-playbook ssadd.yml

3. Remove listened port 8339

   ansible-playbook ssremove.yml
   
   or
   
   ./ssremove.sh
   
4. Schedule task to remove listened port 8399. The schedule
   time should be modified as required before performed.
   
   crontab sscrontab.txt
   
