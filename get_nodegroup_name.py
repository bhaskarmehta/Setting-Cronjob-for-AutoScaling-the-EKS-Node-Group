import boto3

# EKS client
eks = boto3.client('eks',region_name='ap-south-1')
ec2 = boto3.client('ec2', region_name='ap-south-1')
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
    
# asg_name = "eks-eks-node-4cc39b3a-f931-76e8-254c-3321f079a3be"
# print(asg_name)

nodegroup_response = eks.describe_nodegroup(
    clusterName=cluster_name,
    nodegroupName=nodegroup_name
)
asg_name = nodegroup_response['nodegroup']['resources']['autoScalingGroups'][0]

asg2_name = asg_name.values()

print(f"asg_name is : {asg2_name}")


# Get the current node group size
# asg_response = autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])
# current_size = len(asg_response['AutoScalingGroups'][0]['Instances'])

# Scale the node group
response = autoscaling.update_auto_scaling_group(
    AutoScalingGroupName=asg_name,
    MinSize=1,
    MaxSize=1,
    DesiredCapacity=1
)




