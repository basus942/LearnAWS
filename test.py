import boto3


def create_ec2_instance (imageid,choose_min,choose_max,instancetype,enterkeyname):
    try:
        print("Creating ec2 Instance")
        ec2_resources=boto3.client("ec2")
        ec2_resources.run_instances(
            ImageId=imageid,
            MinCount=choose_min,
            MaxCount=choose_max,
            InstanceType=instancetype,
            KeyName=enterkeyname,
        )
    except Exception as e:
        print(e)




def describe_ec2_instance ():
    try:
        ec2_resources=boto3.client("ec2")
        print(ec2_resources.describe_instances())
        return ec2_resources.describe_instances()["Reservations"][1]["Instances"][0]["InstanceId"]
    except Exception as e:
        print(e)


def list_running_instances() :
    ec2_resources=boto3.client("ec2")
    allinfo=ec2_resources.describe_instances()["Reservations"]
    j=0
    listofinstances=[]
    for i in allinfo:
        if(allinfo[j]["Instances"][0]['State']['Name']=='running'):
            # print(allinfo[j]["Instances"][0]["InstanceId"])
            listofinstances.append(allinfo[j]["Instances"][0]["InstanceId"])
        j += 1
    if listofinstances:
            print(listofinstances)
            return listofinstances
    else:
        print("no instances available")

# list_running_instances()



def list_all():
    
    ec2=boto3.resource('ec2')
    ec2_filter=[{'Name':'instance-state-name','Values': ['running','stopped']}]
    instances=ec2.instances.filter(Filters=ec2_filter)

    for i in instances:
        print(i.id,i.instance_type)
    # It returns nothing when there is no instances
    return instances
   
        
# list_all()


# 'State': {'Code': 16, 'Name': 'running'}


def stop_specific_instance(instanceid):
    try:
        
        ec2_resources=boto3.client("ec2")
        ec2_resources.stop_instances(InstanceIds=[instanceid])
        a="Stopped instance id :{}"
        print(a.format(instanceid))
    except Exception :
        print("Invalid Instance id")


def terminate_ec2_instance (instanceid):


    try:
        
        ec2_resources=boto3.client("ec2")
        ec2_resources.terminate_instances(InstanceIds=["instanceid"])
        a="Terminated instance {}"
        print(a.format(instanceid))

       
    except Exception :
        print("Invalid Instance id")


def terminate_all():
    listof_all_instances=list_all()
    ec2_resources=boto3.client("ec2")
    
    for i in listof_all_instances:
        ec2_resources.terminate_instances(InstanceIds=[i.id])
        a="terminated instance id :{}"
        print(a.format(i.id))














# create_ec2_instance()
# describe_ec2_instance()
# stop_ec2_instance()
# terminate_ec2_instance() not completed



def creating_new_instance():
    choose_OS=input("Choose Your Amazon Machine Image- \n1-- Amazon Linux   \n2-- Ubuntu  ")
    match choose_OS:
        case "1":
            imageid="ami-005f9685cb30f234b"
        case "2":
            imageid="ami-0557a15b87f6559cf"
        case _:
            print("invalid option")

    choose_min=int(input("Enter Min Virtual Machine ")or 1)
    choose_max=int(input("Enter Max Virtual Machine ")or 1)

    choose_instance_type=input("Choose Your instance_type- \n1-- t1.micro   \n2-- t2.micro    ")
    match choose_instance_type:
        case "1":
            instancetype="t1.micro"
        case "2":
            instancetype="t2.micro"
        case _:
            print("invalid option   ")
    enterkeyname=input("Enter Key pair  ")
    create_ec2_instance (imageid,choose_min,choose_max,instancetype,enterkeyname)





preview=1
if(preview==1):
    print("1-- Create Instance \n2-- List all Running Instances \n3-- List all Running and Stopped Instances \n4-- Stop specific Instance   \n5-- Terminating a instance   \n6-- Terminating all instances   \n7-- Quit   ")
    option = input("enter a option between 1-4: ")

match option:
    case "1":
        creating_new_instance()
        
    case "2":
        list_running_instances()

    case "3":
        list_all()        

    case "4":
        instanceid_to_stop=input("Enter the instance id to stop:  ")
        stop_specific_instance(instanceid_to_stop)

    case "5":
        instanceid_to_terminate=input("Enter the instance id to terminate:    ")
        terminate_ec2_instance(instanceid_to_terminate)
    
    case "6":
        terminate_all()
        
    case "7":
        print("Quiting  ")
        preview=0
    
    case _:
        print("invalid")
        preview=1

