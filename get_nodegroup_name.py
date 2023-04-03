import boto3

# EKS client
eks_client = session.client('eks',region_name='ap-south-1')

# Get nodegroup name of the cluster
cluster_name = 'eks-test23'
nodegroup_name = ''
try:
    response = eks_client.list_nodegroups(clusterName=cluster_name)
    if len(response['nodegroups']) > 0:
        nodegroup_name = response['nodegroups'][0]
        print(f"Nodegroup name: {nodegroup_name}")
    else:
        print("No nodegroups found in the cluster.")
except Exception as e:
    print(f"Error: {e}")

# Autoscale the nodegroup
if nodegroup_name:
    autoscaling_client = session.client('autoscaling')
    try:
        response = autoscaling_client.update_auto_scaling_group(
            AutoScalingGroupName=nodegroup_name,
            MinSize=1, # set your desired min size
            DesiredSize=2,
            MaxSize=10 # set your desired max size
        )
        print("Autoscaling group updated successfully.")
    except Exception as e:
        print(f"Error: {e}")



