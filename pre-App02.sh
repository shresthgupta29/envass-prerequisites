#!/bin/sh
result=$(cut -d: -f1 /etc/passwd | grep 'pgbu_apps')
if [ -z "$result" ]; then
	mkdir /u01
	chmod 777 /u01
	cd /usr/sbin
	sudo ./useradd -g oinstall -G dba -d /u01/pgbu_apps pgbu_apps
	sudo passwd pgbu_apps
fi
pwd
cd /etc
rm -rf oraInst.loc
touch oraInst.loc
echo "inventory_loc=/u01/oracle/oraInventory" >> oraInst.loc
echo "inst_group=oinstall" >> oraInst.loc
rm -rf /u01/oracle/oraInventory_bak 
mkdir /u01/oracle/oraInventory_bak
cp -r /u01/oracle/oraInventory/* /u01/oracle/oraInventory_bak
/usr/sbin/usermod -a -G oinstall pgbu_apps
rm -rf /u01/oracle/oraInventory/locks
mkdir -p /u01/oracle/oraInventory/locks
chown -R pgbu_apps:oinstall /u01/oracle
chmod -R 777 /u01/oracle
chown -R pgbu_apps:pgbu_apps /u02/app_files
rmdir /u01/app/stage
mkdir -p /u01/app/stage
chown -R pgbu_apps:pgbu_apps /u01/app
cd /etc/security/

result=$(grep 'pgbu_apps soft nproc 15349' limits.conf)
echo $result
if [ -z "$result" ]; then
	echo 'editing the limits.conf file' 
	echo 'pgbu_apps soft nproc 15349' >> limits.conf
	echo 'pgbu_apps hard nproc 16384' >> limits.conf
	echo 'pgbu_apps soft nofile 32768' >> limits.conf
	echo 'pgbu_apps hard nofile 65536' >> limits.conf
	echo 'pgbu_apps soft core 2097152' >> limits.conf
	echo 'pgbu_apps hard core unlimited9' >> limits.conf
else
	echo 'limits.conf already edited'
fi

cd /etc/security/limits.d/
result=$(grep '*          soft    nproc     15349' 90-nproc.conf)

if [ -z "$result" ]; then
	echo '*          soft    nproc     15349' >> 90-nproc.conf
else
	echo "entry addes to 90-nproc.conf file"
fi

