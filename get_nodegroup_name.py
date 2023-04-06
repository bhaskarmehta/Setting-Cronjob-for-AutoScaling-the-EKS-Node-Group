import boto3
import pytz
import os

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

# Scale Up the node
def scale_up():
    autoscaling.update_auto_scaling_group(
    AutoScalingGroupName=asg_name,
    MinSize=1,
    MaxSize=2,
    DesiredCapacity=1
)
    
def scale_down():
    autoscaling.update_auto_scaling_group(
        AutoScalingGroupName=asg_name,
        MinSize=0,
        MaxSize=0,
        DesiredCapacity=0
    )
    
# Call the appropriate function based on the time of day
if __name__ == '__main__':
    import datetime
    # Set the time zone to IST
    tz = pytz.timezone(os.environ['TZ'])
    now = datetime.datetime.now(tz)
    if now.hour == 14 and now.minute == 15:
        scale_up()
    elif now.hour == 14 and now.minute == 17:
        scale_down()
    else:
        print("Not a scheduled time")    




