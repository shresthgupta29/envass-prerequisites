import os
import subprocess
from subprocess import Popen, PIPE
from config import *
os.putenv('ORACLE_HOME',oracle_home)
os.putenv('JAVA_HOME',java_home)
try:
	os.chdir(client_path)
except OSError as err:
	print(err)
	exit()

cwd = os.getcwd()
print "At "+cwd

try:
	subprocess.call('./runInstaller -silent -responseFile '+client_path+'/response/db_install.rsp -showProgress -ignorePrereq -ignoreSysPrereqs -waitforcompletion 	oracle.install.option=INSTALL_DB_SWONLY UNIX_GROUP_NAME=oinstall INVENTORY_LOCATION=/u01/app/oraInventory SELECTED_LANGUAGES=en ORACLE_HOME='+oracle_home+' ORACLE_BASE='+oracle_base+' oracle.install.db.InstallEdition=EE oracle.install.db.isCustomInstall=false oracle.install.db.DBA_GROUP=dba oracle.install.db.OPER_GROUP=dba oracle.install.db.BACKUPDBA_GROUP=dba oracle.install.db.config.starterdb.characterSet=AL32UTF8 oracle.install.db.config.starterdb.memoryOption=true oracle.install.db.DGDBA_GROUP=dba oracle.install.db.KMDBA_GROUP=dba SECURITY_UPDATES_VIA_MYORACLESUPPORT=false DECLINE_SECURITY_UPDATES=true', shell=True)
except OSError as err:
	print(err)
	exit()		
print "Run script db2.py with root privilages"
