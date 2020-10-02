#!/usr/bin/python

import os
import subprocess
import cgi

output1 = subprocess.check_output("uptime | awk '{print $3}' | tr -d ,", shell=True).strip()
mout1=output1.replace('\n','&#13;&#10;')

output2 = subprocess.check_output("ps -ef | grep -c ?", shell=True).strip()
mout2=output2.replace('\n','&#13;&#10;')

output3 = subprocess.check_output("ls",shell=True).strip()
mout3=output3.replace('\n','&#13;&#10;')

output4 = subprocess.check_output("df -h |head -2 |tail -1 | awk '{print $3}'",shell=True).strip()
mout4=output4.replace('\n','&#13;&#10;')

avl = subprocess.check_output("df -h |head -2 |tail -1 | awk '{print $4}'",shell=True).strip()
mavl=avl.replace('\n','&#13;&#10;')

percent = subprocess.check_output("df -h |head -2 |tail -1 | awk '{print $5}'",shell=True).strip()
mpercent=percent.replace('\n','&#13;&#10;')

filename = subprocess.check_output("df -h |head -2 |tail -1 | awk '{print $1}'",shell=True).strip()
mfilename=filename.replace('\n','&#13;&#10;')


output5 = subprocess.check_output("hostname", shell=True).strip()
mout5=output5.replace('\n','&#13;&#10;')

output6 = subprocess.check_output("hostname -I| cut -c1-15", shell=True).strip()
mout6=output6.replace('\n','&#13;&#10;')

output7 = subprocess.check_output("uname -r | cut -c1-6", shell=True).strip()
mout7=output7.replace('\n','&#13;&#10;')

output8 = subprocess.check_output("free -h | head -2 | tail -1 |awk '{print $3}'", shell=True).strip()
mout8=output8.replace('\n','&#13;&#10;')

total = subprocess.check_output("free -h | head -2 | tail -1 |awk '{print $2}'", shell=True).strip()
mtotal=total.replace('\n','&#13;&#10;')

available = subprocess.check_output("free -h | head -2 | tail -1 |awk '{print $7}'", shell=True).strip()
mavailable=available.replace('\n','&#13;&#10;')


output9 = subprocess.check_output("echo $SHELL | cut -c7-", shell=True).strip()
mout9=output9.replace('\n','&#13;&#10;')

output10 = subprocess.check_output("cat /etc/redhat-release", shell=True).strip()
mout10=output10.replace('\n','&#13;&#10;')

print """Content-type: text/html; charset=utf-8\n\n
<!DOCTYPE html>
<html>
<head>
<script  type='text/javascript'>"""
print("function myFunction1(){ document.getElementById('tex').innerHTML='Server is running for "+mout1+" (HH:mm)';}")
print("function myFunction2(){ document.getElementById('tex').innerHTML='Total number of services currently running : "+mout2+"';}")
print("function myFunction3(){ document.getElementById('tex').innerHTML='"+mout3+"';}")
print("function myFunction4(){ document.getElementById('tex').innerHTML='For file /  Used : "+mout4+", Available : "+mavl+", Use% : "+mpercent+ "';}")
print("function myFunction5(){ document.getElementById('tex').innerHTML='Hostname of server : "+mout5+"';}")
print("function myFunction6(){ document.getElementById('tex').innerHTML='IP Address of server : "+mout6+"';}")
print("function myFunction7(){ document.getElementById('tex').innerHTML='Kernel version of the server : "+mout7+"';}")
print("function myFunction8(){ document.getElementById('tex').innerHTML='Memory Used :  "+mout8+", Available : " +mavailable+ "';}")
print("function myFunction9(){ document.getElementById('tex').innerHTML='Current shell : "+mout9+"';}")
print("function myFunction10(){ document.getElementById('tex').innerHTML='OS Version : "+mout10+"';}")
print """

</script>
<meta http-equiv="refresh" content="60">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
<style>
.btn{
	background-color: #d1eafa; color: black;
	transition-duration: 0.4s;
	margin:2%;
	width:90%;
	height: 140%;
	border-radius : 8px;
	border: 3px solid #67B9EE;
}
.btn:hover {
	background-color: #e8f5fd; 
	color: black;
	box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24) , 0 17px 50px 0 rgba(0,0,0,0.19);
}
.image{
	height:40px;
	width:40px;
}
.texta{
	width: 700px;
	height:70px;
	border: 3px solid #67B9EE;
	font-size:20px;
	padding: 15px;
	color : #004988;
	background-color: #f4fafe;
	
}

</style>
</head>
<body style="background-image: linear-gradient(to bottom, rgb(0,190,244), rgb(0,73,136))">
<div class="container">
	<div class="row">
               	<div class="col-sm-12">
				<h1 style="color:#e8f5fd; text-align:center"><b>SERVER MONITORING DASHBOARD</b></h1>
               </div>
	</div>
		
	<div = "row">
		<div class="col-sm-4">

			<button name=cmd value=uname class="btn button1" onClick="myFunction1()">
			<input type="image" src="Server Runtime.png" class="image"/>		
			<br>Server Runtime
			</button>			

			<button name=cmd value=uname class="btn" onClick="myFunction2()">
			<input type="image" src="Services Running.png" 				class="image"/>		
			<br>Running Services
			</button>

			<button name=cmd value=uname class="btn" onClick="myFunction4()">
			<input type="image" src="Disk Usage.png" class="image"/>		
			<br>Disk Usage
			</button>			
		</div>

		<div class="col-sm-4">
			
			<button name=cmd value=uname class="btn" onClick="myFunction5()">
			<input type="image" src="Hostname.png" class="image"/>		
			<br>Hostname
			</button>

			<button name=cmd value=uname class="btn" onClick="myFunction6()">
			<input type="image" src="IP Address.png" class="image"/>		
			<br>IP Address
			</button>

			<button name=cmd value=uname class="btn" onClick="myFunction7()">
			<input type="image" src="Kernel Version.png" class="image"/>		
			<br>Kernel Version
			</button>
		</div>

		<div class="col-sm-4">
			<button name=cmd value=uname class="btn" onClick="myFunction8()">
			<input type="image" src="Memory Usage.png" class="image"/>		
			<br>Memory Usage
			</button>
			
			<button name=cmd value=uname class="btn" onClick="myFunction9()">
			<input type="image" src="Current Shell.png" class="image"/>		
			<br>Current Shell
			</button>

			<button name=cmd value=uname class="btn" onClick="myFunction10()">
			<input type="image" src="OS Version.png" class="image"/>
			<br>OS Version		
			</button>
		</div>
	</div>
			
	<div class="row">
		
		
		<div class="col-sm-12">
                        <center><textarea  style="text-align:center;color : #004988; margin:auto;" readonly  id="tex" class="texta" placeholder="Your result gets displayed here" width=50%></textarea></center>

                </div>
		
	</div>

</div>
</body>
</html>"""

