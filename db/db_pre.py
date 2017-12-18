import os
import shutil
import subprocess
from subprocess import Popen, PIPE
from config import *
os.putenv('ORACLE_HOME',oracle_home)
os.putenv('JAVA_HOME',java_home)

try:
	os.chdir(oracle_home+'/bin')
except OSError as err:
	print(err)
	exit()


conn = 'sys/'+admin_pass+'@'+cdb+' as sysdba'
session = subprocess.Popen([oracle_home+'/bin/sqlplus', '-S', conn], stdin=PIPE, stdout=PIPE, stderr=PIPE)
session.stdin.write('ALTER SYSTEM SET open_cursors=1000 SCOPE=BOTH;')
(stdout,stderr)=session.communicate()
print stdout

conn = 'sys/'+admin_pass+'@'+cdb+' as sysdba'
session = subprocess.Popen([oracle_home+'/bin/sqlplus', '-S', conn], stdin=PIPE, stdout=PIPE, stderr=PIPE)
session.stdin.write('alter system set processes=1000 scope=spfile;')
(stdout,stderr)=session.communicate()
print stdout


conn = 'sys/'+admin_pass+'@'+cdb+' as sysdba'
session = subprocess.Popen([oracle_home+'/bin/sqlplus', '-S', conn], stdin=PIPE, stdout=PIPE, stderr=PIPE)
session.stdin.write('@'+oracle_home+'/rdbms/admin/xaview;')
(stdout,stderr)=session.communicate()
print stdout


conn = 'sys/'+admin_pass+'@'+cdb+' as sysdba'
session = subprocess.Popen([oracle_home+'/bin/sqlplus', '-S', conn], stdin=PIPE, stdout=PIPE, stderr=PIPE)
session.stdin.write('grant select on v$pending_xatrans$ to sys;')
(stdout,stderr)=session.communicate()
print stdout


conn = 'sys/'+admin_pass+'@'+cdb+' as sysdba'
session = subprocess.Popen([oracle_home+'/bin/sqlplus', '-S', conn], stdin=PIPE, stdout=PIPE, stderr=PIPE)
session.stdin.write('grant select on v$xatrans$ to sys;')
(stdout,stderr)=session.communicate()
print stdout

conn = 'sys/'+admin_pass+'@'+cdb+' as sysdba'
session = subprocess.Popen([oracle_home+'/bin/sqlplus', '-S', conn], stdin=PIPE, stdout=PIPE, stderr=PIPE)
session.stdin.write('commit;')
(stdout,stderr)=session.communicate()
print stdout

conn = 'sys/'+admin_pass+'@'+cdb+' as sysdba'
session = subprocess.Popen([oracle_home+'/bin/sqlplus', '-S', conn], stdin=PIPE, stdout=PIPE, stderr=PIPE)
session.stdin.write('shutdown immediate;')
(stdout,stderr)=session.communicate()
print stdout


os.putenv('ORACLE_SID',cdb)
os.chdir(oracle_home+'/bin')

try:
	session = subprocess.Popen([oracle_home+'/bin/sqlplus', '/ as sysdba'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
except OSError as e:
	print(e)
	exit()	
session.stdin.write('startup;');
res = session.communicate()
print res[0]

#conn = 'sys/'+admin_pass+'@'+cdb+' as sysdba'
#session = subprocess.Popen([oracle_home+'/bin/sqlplus', '-S', conn], stdin=PIPE, stdout=PIPE, stderr=PIPE)
#session.stdin.write('grant create database link to sys_install;')
#(stdout,stderr)=session.communicate()
#print stdout

conn = 'sys/'+admin_pass+'@'+cdb+' as sysdba'
session = subprocess.Popen([oracle_home+'/bin/sqlplus', '-S', conn], stdin=PIPE, stdout=PIPE, stderr=PIPE)
session.stdin.write("select limit from dba_profiles where resource_name='PASSWORD_VERIFY_FUNCTION' and profile='DEFAULT';")
(stdout,stderr)=session.communicate()
print stdout


conn = 'sys/'+admin_pass+'@'+cdb+' as sysdba'
session = subprocess.Popen([oracle_home+'/bin/sqlplus', '-S', conn], stdin=PIPE, stdout=PIPE, stderr=PIPE)
session.stdin.write('alter profile default limit PASSWORD_VERIFY_FUNCTION null;')
(stdout,stderr)=session.communicate()
print stdout


