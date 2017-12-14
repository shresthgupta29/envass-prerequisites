HA = 1			#put HA = 1 for HA environment and 0 for Non_HA

IDM_NodeA= ["10.120.0.6","10.75.35.146"]
App01_NodeA = ["10.120.0.7","10.75.35.137"]
App02_NodeA = ["10.120.0.5","10.75.35.207"]
App03_NodeA = ["10.120.0.4","10.120.0.90"]

IDM_NodeB = ["10.120.0.5","10.120.0.5"]
App01_NodeB = ["10.120.0.2","10.75.35.137"]
App02_NodeB = ["10.120.0.8","10.75.35.137"]
App03_NodeB = ["10.120.0.4","10.75.35.137"]

nfs='10.120.0.2'

db=["10.120.0.3","10.75.35.221"]

zip_path = "" #path of the chefToolkit with the file itself Example : "/u02/app_files/PrimeeraXXXXXXXXXX.zip"  
chef_path="/home/cloud-user/Primavera_Orchestration_toolkit_17.11.0.0"  #till Cheforchestration --> this folder should contain chef and testing folders


m_list1 = [IDM_NodeA[0],IDM_NodeB[0],App01_NodeA[0],App01_NodeB[0],App02_NodeA[0],App02_NodeB[0],App03_NodeA[0],App03_NodeB[0]]
m_list2  = [IDM_NodeA[0],App01_NodeA[0],App02_NodeA[0],App03_NodeA[0]]