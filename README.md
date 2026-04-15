# Topology #
<img width="1378" height="554" alt="Image" src="https://github.com/user-attachments/assets/dacded82-2fad-4d87-8c4d-22007f00c835" />

# Problem Statement #
- Agent running in agent engine
- Simplest agent to go and get news
- Agent should only get news from one given website which user defines . Dont just go to any random site on Internet to get me the news
- When agent go out to internet , your IP should be fixed public IP
  
# SWG configuration #
Deployed in Explicit routing mode  

My policy had a match on --> host().endsWith('wikipedia.org')  

The IP of web proxy was 10.10.10.2  

# Network Attachment #
Network attachment  
projects/[project-id]/regions/asia-south1/networkAttachments/agent-engine-attachment   
Region  
asia-south1  
Network  
test-vpc-1  
Subnetworks  
psc-intf-subnet  
Connection preference  
Accept automatically  

# Deployment command #
adk deploy agent_engine .     --project="project-id"     --region="asia-south1"     --display_name="News-Proxy-v11" 

# How to ensure it worked #
- you should see a tenant project is attached to your network attachment

<img width="1037" height="548" alt="Image" src="https://github.com/user-attachments/assets/2a575580-da99-4b1f-963f-769776a0cc20" />
