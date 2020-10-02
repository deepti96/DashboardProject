# DashboardProject
Contains a server parameters displaying dashboard.

Please refer to the following set of instructions for setting up the project.
Clone the project in "/var/www/html" folder of Linux CentOS

Make sure you are the Root user :-
Type “su root”, then enter the password.

Use the commands in the following link to install and run Apache web server:

https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-centos-7

In this step, if the firewall command doesn’t work,use the following commands:

yum install firewalld
systemctl start firewalld
systemctl enable firewalld
systemctl status firewalld

Resource for this: https://www.tecmint.com/fix-firewall-cmd-command-not-found-error/#:~:text=To%20fix%20this%20error%2C%20you,yum%20package%20manager%20as%20follows.&text=Next%2C%20start%20firewalld%20and%20enable,boot%2C%20then%20check%20its%20status.



To start Apache on terminal

Check your ip address using “ip addr sh”  and type “http://your-ip-address/” in the browser  to open apache




Follow the steps given in the following video from 0:34 to 8:23. Don’t open Apache as shown in this video. Use the above stepfor that.

https://www.youtube.com/watch?v=CFH_TUGZt5I

Type in your browser (to open the project):
“http://your-ip-address/test.cgi” 


