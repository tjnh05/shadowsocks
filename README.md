# shadowsocks administrator

1. Deploy shadowsocks on remote host vpnserv

   ansible-playbook ssinstall.yml

2. Add port 8399 to listen

   ansible-playbook ssadd.yml
   
   Note:
   if you wanna add other port to listen , please modify 
   variable SS_ADD defined in file ssvars.yml.

3. Remove listened port 8339

   ansible-playbook ssremove.yml
   
   or
   
   ./ssremove.sh
   
   Note:
   if you wanna add other port to listen , please modify 
   variable SS_ADD defined in file ssvars.yml.
   
4. Schedule task to remove listened port 8399. The schedule
   time should be modified as required before performed.
   
   crontab sscrontab.txt
   
