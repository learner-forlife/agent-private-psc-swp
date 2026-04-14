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
