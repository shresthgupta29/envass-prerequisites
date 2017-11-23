# envass-prerequisites
Scripts to run pre-requisites in envass environment for new installation using Chef

Pre-requisites : ChefToolkit
1. Copy the folde 'pre_envass.zip' to machine
2. Extract the zip file
3. cd pre_envass
4. Edit the machines details in the 'machines.py' files
5. Enter chef_path in the "machines.py" till the folder containing 'ChefOrchestration' folder.
6. Run ./pdit_clean file first
7. execute python pre.py 


Note: config.py; db1.py; db2.py; db3.py use only at db machine
1. Edit config.py file
2. Execute db1.py as gbuora
3. Execute db2.py as root
4. Exeute db3.py as gbuora  - type 'y' when prompted
  

Note: If db client is already installed then directly run db3.py - type 'n' when prompted
