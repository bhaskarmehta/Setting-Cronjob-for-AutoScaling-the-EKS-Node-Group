import boto3

# Create an EKS client
eks = boto3.client('eks',region_name='ap-south-1')

# Set the name of the EKS cluster
cluster_name = 'eks-test23'

# Get the list of nodegroups for the EKS cluster
response = eks.list_nodegroups(clusterName=cluster_name)
nodegroups = response['nodegroups']

# Print the list of nodegroups
print('Nodegroups:', nodegroups)

# Get the name of the first nodegroup in the list
nodegroup_name = nodegroups[0]

# Print the name of the first nodegroup
print('Nodegroup name:', nodegroup_name)


