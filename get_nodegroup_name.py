import subprocess
import json

# Set the name of your EKS cluster and nodegroup
cluster_name = 'eks-test23'
nodegroup_name = 'eks-node'
region = 'ap-south-1'

# Get the ARN of the nodegroup
cmd = f'aws eks describe-nodegroup --cluster-name {cluster_name} --nodegroup-name {nodegroup_name} --region {region}'
output = subprocess.check_output(cmd, shell=True)
nodegroup_arn = json.loads(output.decode('utf-8'))['nodegroup']['nodegroupArn']

# Extract the nodegroup name from the ARN
nodegroup_name = nodegroup_arn.split('/')[-1]

print(f'The nodegroup name for {cluster_name} in {region} is {nodegroup_name}')

