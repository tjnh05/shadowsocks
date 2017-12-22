# shadowsocks administrator

1. Deploy shadowsocks on remote host vpnserv

   ansible-playbook ssinstall.yml
   
   Perform command below to check if services have been started:
   netstat -ntlp | egrep "(80)|(83)"

2. Add port 8399 to listen

   ansible-playbook ssadd.yml
   
   Perform command below to check if service has been started:
   netstat -ntlp | egrep "8399"
   
   Note:
   if you wanna add other port to listen , please modify 
   variable SS_ADD defined in file ssvars.yml.

3. Remove listened port 8339

   ansible-playbook ssremove.yml
   
   or
   
   ./ssremove.sh
   
   Perform command below to check if service has been removed:
   netstat -ntlp | egrep "8399"
   
   Note:
   if you wanna add other port to listen , please modify 
   variable SS_REMOVE defined in file ssvars.yml.
   
4. Schedule task to remove listened port 8399. The schedule
   time should be modified as required before performed.
   
   crontab sscrontab.txt
   
