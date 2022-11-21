import os


instances = [
    {
        "security_groups" : ["tf_test_group"],
        "name"            : "instancias_teste",
        "ami"             : "ami-08c40ec9ead489470",
        "instance_type"   : "t2.micro",
        "region"          : "us-east-1"
    }
]

security_groups = [
    {
        "id"          : "50",
        "name"        : "tf_test_group",
        "description" : "TESTE",
        "ingress" : [{
            "from_port"   : "80",
            "to_port"     : "80",
            "description" : "HTTP",
            "protocol"    : "tcp",
            "cidr_blocks" : ["10.0.0.0/20"]
        }]
    }
]

users = [
    {
        "name" : "TESTE85647" 
    }
]

var = {
    "instances":instances,
    "security_groups":security_groups,
    "users":users,
    "vpc_cidr":"10.0.0.0/16",
}

# os.system('terraform destroy -auto-approve')
os.system('terraform apply -auto-approve -var="users='+str(users).replace("'",'"')+'"')
# print('terraform apply -auto-approve -var="users='+str(users).replace("'",'"')+'"')