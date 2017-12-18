# envass-prerequisites
Setup DB Machine

1.Download the scripts into the db machine.

2. If using cloud-user change the permissions once done copying 

       -→ mv envass-prerequisites-master/ /home/gbuora/

       -→ chown -R gbuora:oinstall /home/gbuora/envass-prerequisites-master/
4. Make sure /u01 and the scripts have the same user group, if not change the user group for /u01 and scripts.

3. Edit config.py file with the correct details 

4. Run "python db1.py" if fresh db install with gbuora

5. Run "python db2.py" with root

6. Run "python db3.py" with gbuora

Note: if db server is already installed skip step 4 and step 5. 

Note: For manual installing db refer to https://confluence.oraclecorp.com/confluence/display/PCE/Setup+Oracle+12c+Database and once done with the installtion edit the config.py file and run "python db_pre.py".

 

Setup NFS

1. Download the scripts into db machine.
2. Edit machines.py with the machines details.
3. run "python nfs.py"
4. Run the command prompted at the end of the script in all other machines (App01,App02.App03)
5. Check if /u02 is mounted properly.
Note : if .u02/ is not mounted properly then refer to  https://confluence.oraclecorp.com/confluence/display/PCE/Provision+OCI+Classic%2C+OPC+P6+SE  (Post Implementation section )
 

Pre-Requisites for App01,App02,IDM,App03

Once /u02 is mounted copy the scripts to /u02/app_files
1.Copy the chef toolkit to the /u02/app_files.
2.Edit the machines.py file.
3.Update the zip_path variable with the correct path for the toolkit zip file.
       Edit the chef_path if unziping the toolkit manually. 
4. A chef folder will be create with the name "chefdd-mm"  Example: /chef18-12.
5. Edit the runlist as per the manuals.
6. Start chef.
