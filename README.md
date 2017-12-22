# shadowsocks administrator

1. Deploy shadowsocks on remote host vpnserv

   ansible-playbook ssinstall.yml
   
   If you wanna install tool qrcode on localhost, perform command below:
   
   ansible-playbook ssinstall.yml --extra-vars="INSTALL_QRCODE=yes"
   
   Perform command below on remote host by root user to check if shadowsocks services
   
   have been started:
   
   netstat -ntlp | egrep "(80)|(83)"

2. Add port 8399 to listen

   ansible-playbook ssadd.yml
   
   Perform command below on remote host by root user to check if shadowsocks service
   
   has been started:
   
   netstat -ntlp | egrep "8399"
   
   Note:
   if you wanna add other port to listen , please modify 
   
   variable SS_ADD defined in file ssvars.yml.

3. Remove listened port 8339

   ansible-playbook ssremove.yml
   
   or
   
   ./ssremove.sh
   
   Perform command below on remote host by root user to check if shadowsocks service
   
   has been removed:
   
   netstat -ntlp | egrep "8399"
   
   Note:
   
   if you wanna add other port to listen , please modify 
   
   variable SS_REMOVE defined in file ssvars.yml.
   
4. Schedule task to remove listened port 8399. The schedule

   time should be modified as required before performed.
   
   crontab sscrontab.txt

5. Generate QR code for configuration of shadowsocks client.

   echo -n "ss://"$(echo -n aes-256-cfb:helloworld@40.71.199.96:8000 | base64) | qr

   Note:
   
   IP address 40.71.199.96 should be replaced with your own IP.
   
