import boto3

# EKS client
eks = boto3.client('eks',region_name='ap-south-1')
autoscaling = boto3.client('autoscaling',region_name='ap-south-1')

# Get nodegroup name of the cluster
cluster_name = 'eks-test23'
nodegroup_name = ''
try:
    response = eks.list_nodegroups(clusterName=cluster_name)
    if len(response['nodegroups']) > 0:
        nodegroup_name = response['nodegroups'][0]
        print(f"Nodegroup name: {nodegroup_name}")
    else:
        print("No nodegroups found in the cluster.")
except Exception as e:
    print(f"Error: {e}")
    

nodegroup_response = eks.describe_nodegroup(
    clusterName=cluster_name,
    nodegroupName=nodegroup_name
)
asg_key_pair_value = nodegroup_response['nodegroup']['resources']['autoScalingGroups'][0]

asg_name = asg_key_pair_value['name']
print(f"asg_name is : {asg_name}")


# Scale the node group
response = autoscaling.update_auto_scaling_group(
    AutoScalingGroupName=asg_name,
    MinSize=1,
    MaxSize=2,
    DesiredCapacity=1
)




