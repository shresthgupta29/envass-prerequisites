import os
import subprocess
from subprocess import Popen, PIPE
from machines import *


print ("\n\nWarning : Please make sure that /u02/app_files is mounted properly before running the script!\n\n")
app=input("Select app :\n\t\t0: For IDM(A/B)\n\t\t1: For App01(A/B)\n\t\t2: For app02(A/B)\n\t\t3: For app03(A/B)\n")
if app not in [0,1,2,3]:
	print ("Wrong input....Exinitg")
	exit()
print (m_list)
os.chdir('/etc')
if os.path.isfile('/etc/resolv.conf'):
	print("Editing /etc/resolv.conf")
else:
	print("/etc/resolv.conf file missing...Exiting")
	exit()
with open('/etc/resolv.conf','r') as myfile:
	lines=myfile.read()

print lines
if(lines.find('nameserver 10.75.137.245')+1):
	print("Pass 1")
else:
	with open('/etc/resolv.conf','a') as myfile:
		print("Editing resolv.conf file")
		myfile.write('nameserver 10.75.137.245\n')

if(lines.find('nameserver 10.75.137.246')+1):
	print("Pass 2")
else:
	with open('/etc/resolv.conf','a') as myfile:
		print("Editing resolv.conf file")
		myfile.write('nameserver 10.75.137.246')

try:
	subprocess.call('service iptables stop',shell=True)
except OSError as e:
	print (e)
	exit()
# if os.path.isfile('/etc/exports'):
# 	print("Editing exports file")
# else:
# 	print("/etc/exports file missing...Exiting")
# 	exit()
# with open('/etc/exports','a') as myfile:
# 	for i in m_list:
# 		myfile.write("/u02 "+i+"(rw,sync,no_root_squash)\n")
# subprocess.call('service nfs restart',shell=True)
# subprocess.call('service nfs status',shell=True)
# try:
# 	subprocess.call('mount -t nfs '+nfs+':/u02 /u02',shell=True)
# 	subprocess.call('mount | grep nfs',shell=True)
# except OSError as e:
# 	print("/u02 not mounted properly")
# 	exit()
os.chdir(chef_path+'/ChefOrchestration/testing')
if os.path.isfile('/etc/fstab'):
	print("Editing exports file")
else:
	print("/etc/fstab file missing...Exiting")
	exit()
with open('/etc/fstab','r') as myfile:
	lines=myfile.read()

if(lines.find(nfs+':/u02    /u02   nfs    defaults   0   0')+1):
	print("fstab already edited")
else:
	with open('/etc/fstab','a') as myfile:
		print("Editing fstab file")
		myfile.write(nfs+':/u02    /u02   nfs    defaults   0   0')

try:
	subprocess.call('/usr/sbin/groupadd oinstall -g 56056',shell=True)
	subprocess.call('/usr/sbin/groupadd dba -g 56057',shell=True)
	subprocess.call('/usr/sbin/usermod -a -g pgbu_apps -G oinstall,dba pgbu_apps',shell=True)
except OSError as e:
	print (e)
	exit()

try:
	subprocess.call('yum -y install telnet nfs-utils nfs-utils-lib bind-utils man wget tigervnc-server xorg-x11-xauth xterm unzip',shell=True)
	subprocess.call('yum groupinstall -y basic-desktop',shell=True)
	subprocess.call('wget http://slc06uwv.us.oracle.com/ChefSoftware/Software/Common/Base/packages_idc',shell=True)
	subprocess.call('wget http://slc06uwv.us.oracle.com/ChefSoftware/Software/Common/Base/packages_new',shell=True)
	subprocess.call('chmod 777 packages_idc packages_new',shell=True)
	subprocess.call('yum -y install $(cat /tmp/packages_idc)',shell=True)
	subprocess.call('yum -y install $(cat /tmp/packages_new)',shell=True)
	subprocess.call('yum install -y vim vnc screen libaio zip xauth compat-libcap1-1.10  compat-libstdc++-33 libstdc++-devel gcc-c++ ksh libaio-devel',shell=True)
	subprocess.call('yum install bind-utils -y',shell=True)
except OSError as e:
	print (e)
	exit()

	
os.chdir('/etc/security/limits.d')
with open("90-nproc.conf", "a") as myfile:	
    myfile.write("* soft nproc 15349\n")
try:
	subprocess.call('mkdir -p /u01',shell=True)
	subprocess.call('chown pgbu_apps:pgbu_apps /u01',shell=True)
 	subprocess.call('chmod 777 /u01',shell=True)
 	subprocess.call('mkdir -p /u02/app_files',shell=True)
 	subprocess.call('chmod 777 /u02',shell=True)
 	subprocess.call('chmod 777 /u02/app_files',shell=True)
 	subprocess.call('rm -rf /etc/oraInst.loc',shell=True)
except OSError as e:
	print (e)
	exit()
os.chdir('/etc')
with open("oraInst.loc","w") as myfile:
	myfile.write('inventory_loc=/u01/oracle/oraInventory\ninst_group=oinstall\n')
try:
 	subprocess.call('chmod 777 /etc/oraInst.loc',shell=True)
 	subprocess.call('rm -rf /u01/oracle/oraInventory/*',shell=True)
 	subprocess.call('mkdir -p /u01/oracle/oraInventory',shell=True)
 	subprocess.call('mkdir -p /u01/oracle/oraInventory/locks',shell=True)
 	subprocess.call('chown -R pgbu_apps:oinstall /u01/oracle',shell=True)
 	subprocess.call('chmod -R 777 /u01/oracle',shell=True)
 	subprocess.call('/usr/sbin/usermod -a -G oinstall pgbu_apps',shell=True)
	proc = Popen("ps -ef | grep vnc | awk '{print $2}'",shell=True,stdout=PIPE)
	vnc = proc.communicate()[0].split('\n')
	print vnc
 	# vnc= subprocess.check_output("ps -ef | grep vnc | awk '{print $2}'",shell=True,stderr=subprocess.STDOUT)
	# vnc= vnc.split('\n')
	# print vnc 
	subprocess.call('rm -rf /root/freecache.sh',shell=True)
	subprocess.call("printf '%s\n' 'while true; do echo 1 | tee /proc/sys/vm/drop_caches; sleep 60s; done;' >> /root/freecache.sh",shell=True)
	os.chdir('/root')
	print os.getcwd()
 	subprocess.call('chmod 777 freecache.sh',shell=True)
 	subprocess.call('rm -rf nohup.out',shell=True)
 	subprocess.call('./freecache.sh >> freecache.log &',shell=True) #check
except OSError as e:
 	print (e)
 	exit()

print ("Killing all vncserver session")	
try:
 	for i in range(len(vnc)-1):
 		# print('kill -9 '+vnc[i])
 		subprocess.call('kill -9 '+vnc[i],shell=True)
except OSError as e:
	print (e)
	exit()

proc = Popen("ps -ef | grep yum | awk '{print $2}'",shell=True,stdout=PIPE)
yum = proc.communicate()[0].split('\n')
## yum= subprocess.check_output("ps -ef | grep yum | awk '{print $2}'",shell=True,stderr=subprocess.STDOUT)
## yum= yum.split('\n')
print yum
print ("Killing all yum processes")	
try:
 	for i in range(len(yum)-1):
		# print ('kill -9 '+yum[i])	
 		subprocess.call('kill -9 '+yum[i],shell=True)
except OSError as e:
	print (e)
	exit()

proc = Popen("ps -ef | grep java | awk '{print $2}'",shell=True,stdout=PIPE)
javaproc = proc.communicate()[0].split('\n')
print javaproc
## javaproc= subprocess.check_output("ps -ef | grep java | awk '{print $2}'",shell=True,stderr=subprocess.STDOUT)
## javaproc= javaproc.split('\n')
print ("Killing all java processes")	
try:
 	for i in range(len(yum)-1):
		# print ('kill -9 '+javaproc[i])
 		subprocess.call('kill -9 '+javaproc[i],shell=True)
except OSError as e:
	print (e)
	exit()



os.chdir(chef_path+'/ChefOrchestration/chef')
subprocess.call('mv solo.rb.sample solo.rb',shell=True)

if os.path.isfile('solo.rb'):
	print ("Editing solo.rb")
else:
	print ("solo.rb not found")
	exit()
try:
	with open('solo.rb','a') as myfile:
		myfile.write('JAVA_OPTIONS "-Djava.security.egd=file:/dev/./urandom"')

	with open('./cookbooks/pgbu_java/recipes/default.rb','a') as myfile:
		myfile.write("\njava_path = node[:pgbu_java][:java_home] + '/jre/lib/security/java.security'\n\nruby_block \"Change values in java.secrity\" do\nblock do\njava_path = Chef::Util::FileEdit.new(java_path)\njava_path.search_file_replace_line(\"securerandom.source=\", \"securerandom.source=file:/dev/./urandom\")\njava_path.write_file\nend\naction :run\nend")

	with open('./cookbooks/pgbu_template_approach/recipes/pre_install.rb','a') as myfile:
		myfile.write("\njava_path = node[:pgbu_java][:java_home] + '/jre/lib/security/java.security'\n\nruby_block \"Change values in java.secrity\" do\nblock do\njava_path = Chef::Util::FileEdit.new(java_path)\njava_path.search_file_replace_line(\"securerandom.source=\", \"securerandom.source=file:/dev/./urandom\")\njava_path.write_file\nend\naction :run\nend")

	with open('./cookbooks/pgbu_template_approach/recipes/pre_upgrade.rb','a') as myfile:
		myfile.write("\njava_path = node[:pgbu_java][:java_home] + '/jre/lib/security/java.security'\n\nruby_block \"Change values in java.secrity\" do\nblock do\njava_path = Chef::Util::FileEdit.new(java_path)\njava_path.search_file_replace_line(\"securerandom.source=\", \"securerandom.source=file:/dev/./urandom\")\njava_path.write_file\nend\naction :run\nend")

	with open('./cookbooks/pgbu_template_approach/recipes/install_node.rb','a') as myfile:
		myfile.write("\njava_path = node[:pgbu_java][:java_home] + '/jre/lib/security/java.security'\n\nruby_block \"Change values in java.secrity\" do\nblock do\njava_path = Chef::Util::FileEdit.new(java_path)\njava_path.search_file_replace_line(\"securerandom.source=\", \"securerandom.source=file:/dev/./urandom\")\njava_path.write_file\nend\naction :run\nend")

	with open('./cookbooks/pgbu_template_approach/recipes/upgrade_node.rb','a') as myfile:
		myfile.write("\njava_path = node[:pgbu_java][:java_home] + '/jre/lib/security/java.security'\n\nruby_block \"Change values in java.secrity\" do\nblock do\njava_path = Chef::Util::FileEdit.new(java_path)\njava_path.search_file_replace_line(\"securerandom.source=\", \"securerandom.source=file:/dev/./urandom\")\njava_path.write_file\nend\naction :run\nend")

except FileNotFoundError as e:
	print (e)
	exit()


try:
	with open('./cookbooks/pgbu_ohs/recipes/install_ohs12c.rb','r') as f:
		lines=f.readlines()
except FileNotFoundError as e:
	print (e)
	exit()
for index, line in enumerate(lines):
    if line.startswith("# Run configuration"):
        break
lines.insert(index, "java_path = ohs_install_path + '/oracle_common/jdk/jre/lib/security/java.security'\nruby_block \"Change values in java.secrity\" do\nblock do\njava_path = Chef::Util::FileEdit.new(java_path)\njava_path.search_file_replace_line(\"securerandom.source=\", \"securerandom.source=file:/dev/./urandom\")\njava_path.write_file\nend\naction :run\nend\n")

with open('./cookbooks/pgbu_ohs/recipes/install_ohs12c.rb', 'w') as f:
    contents = f.writelines(lines)

try:
	with open('./cookbooks/pgbu_weblogic_12_2_1/recipes/install_java.rb','a') as myfile:
		myfile.write("\njava_path = node[:pgbu_weblogic_12_2_1][:weblogic_java_home] + '/jre/lib/security/java.security'\nruby_block \"Change values in java.secrity\" do\nblock do\njava_path = Chef::Util::FileEdit.new(java_path)\njava_path.search_file_replace_line(\"securerandom.source=\", \"securerandom.source=file:/dev/./urandom\")\njava_path.write_file\nend\naction :run\nend\n")
except FileNotFoundError as e:
	print (e)
	exit()

#######################################################################################################

proc = Popen("cut -d: -f1 /etc/passwd | grep 'pgbu_apps'",shell=True,stdout=PIPE)
res = proc.communicate()[0].split('\n')
print res
if not (res[0]=="pgbu_apps"):
	subprocess.call('mkdir /u01',shell=True)
	subprocess.call('chmod 777 /u01',shell=True)
	subprocess.call('cd /usr/sbin',shell=True)
	subprocess.call('sudo ./useradd -g oinstall -G dba -d /u01/pgbu_apps pgbu_apps',shell=True)
	subprocess.call('sudo passwd pgbu_apps',shell=True)

try:
	subprocess.call('rm -rf /u01/oracle/oraInventory_bak',shell=True)
	subprocess.call('mkdir /u01/oracle/oraInventory_bak',shell=True)
	subprocess.call('cp -r /u01/oracle/oraInventory/* /u01/oracle/oraInventory_bak',shell=True)
	subprocess.call('/usr/sbin/usermod -a -G oinstall pgbu_apps',shell=True)
	subprocess.call('rm -rf /u01/oracle/oraInventory/locks',shell=True)
	subprocess.call('mkdir -p /u01/oracle/oraInventory/locks',shell=True)
	subprocess.call('chown -R pgbu_apps:oinstall /u01/oracle',shell=True)
	subprocess.call('chmod -R 777 /u01/oracle',shell=True)
	subprocess.call('chown -R pgbu_apps:pgbu_apps /u02/app_files',shell=True)
	subprocess.call('rmdir /u01/app/stage',shell=True)
	subprocess.call('mkdir -p /u01/app/stage',shell=True)
	subprocess.call('chown -R pgbu_apps:pgbu_apps /u01/app',shell=True)
except OSError as e:
	print(e)

os.chdir('/etc/security/')
flag=0
try:
	with open('limits.conf','r') as f:
		lines=f.readlines()
except FileNotFoundError as e:
	print (e)
	exit()
for index, line in enumerate(lines):
    if line.startswith("pgbu_apps") and line.endswith('15349\n'):
    	print line
        flag=1

if (flag==0):
	print ("Editing limits.conf file")
	with open("limits.conf", "a") as myfile:
		myfile.write("pgbu_apps   soft   nproc   15349\npgbu_apps   hard   nproc   16384\npgbu_apps   soft   nofile   32768\npgbu_apps   hard   nofile   65536\npgbu_apps   soft   core   2097152\npgbu_apps   hard   core   unlimited\n")
  
if app==0:
	subprocess.call('yum install expect*',shell=True)
	print('Done for IDM')
elif app==1:
	subprocess.call('yum install expect*',shell=True)
	print("Done for App01")
elif app==2:
	 print("Done for App02")
elif app==3:
	print("Edit /etc/hosts before proceeding further")

