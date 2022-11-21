import os
import json


instance_security_groups = [""]
instance_name = ""
instance_ami = ""
instance_type = ""
instance_region = ""

instances = [
    {
        "security_groups" : instance_security_groups,
        "name"            : instance_name,
        "ami"             : instance_ami,
        "instance_type"   : instance_type,
        "region"          : instance_region
    }
]

security_group_id = ""
security_group_name = ""
security_group_description = ""
security_group_ingress = []
security_group_ingress_from_port = ""
security_group_ingress_to_port = ""
security_group_ingress_description = ""
security_group_ingress_protocol = ""
security_group_ingress_cidr_blocks = [""]
ingress = {
    "from_port"   : security_group_ingress_from_port,
    "to_port"     : security_group_ingress_to_port,
    "description" : security_group_ingress_description,
    "protocol"    : security_group_ingress_protocol,
    "cidr_blocks" : security_group_ingress_cidr_blocks
}
security_group_ingress = [ingress]

security_groups = [
    {
        "id"          : security_group_id,
        "name"        : security_group_name,
        "description" : security_group_description,
        "ingress" : security_group_ingress
    }
]

users_name = ""
users = [
    {
        "name" : users_name
    }
]

vpc_cidr = ""








def main():
    print("""\nBem-vindo(a) ao melhor sistema de configuração de infra para aws já feito:\n
          Escolha umas da opções asseguir:\n
          1 - Criar infraestruturo do zero\n
          2 - Editar infraestrutura atual\n
          3 - Deletar infraestrutura\n""")
    option = input("Favor escrever apenas o número da opção(ex. 1): ")
    
    if option == "1":
        print("Configurando VPC:")
        vpc_cidr = input("VPC cidr: ")
        print("Configurando subnet:")
        #Adiciona instancia
        instances = []
        while(1):
            print("Configurando instâncias:")
            print("Insira os nomes dos security groups da instância:")
            print("Obs: Para parar digite 0")
            while(1):
                instance_security_groups = []
                sg = input("Nome do grupo de segurança: ")
                if sg == "0":
                    break
                instance_security_groups.append(sg)
            
            instance_name = input("Nome da instância: ")
            instance_ami = input("AMI (ex. ami-08c40ec9ead489470): ")
            instance_type = input("Tipo de instância (ex. t2.micro): ")
            instance_region = input("Região da instância (ex.us-east-1): ")  
            instance = {
                    "security_groups" : instance_security_groups,
                    "name"            : instance_name,
                    "ami"             : instance_ami,
                    "instance_type"   : instance_type,
                    "region"          : instance_region
                }
            
            instances.append(instance)

            continuar = input("Deseja adicionar mais uma instância: [s/n] ").lower()
            if continuar == "não" or continuar == "n" or continuar == "nao":
                break
        #Adiciona security group
        security_groups = []
        print("Criando grupo de segurança: ")
        while(1):
            security_group_id = input("ID do grupo de segurança: ")  
            security_group_name = input("Nome do grupo de segurança: ")  
            security_group_description = input("Descrição do grupo de segurança: ")  
            security_group_ingress = []
            print("Definição das regras de engreço")
            while(1):
                security_group_ingress_from_port = input("Porta de entrada: ")  
                security_group_ingress_to_port = input("Porta de saída: ")  
                security_group_ingress_description = input("Descrição da regra: ")  
                security_group_ingress_protocol = input("Protocolo (ex. tcp): ")  
                security_group_ingress_cidr_blocks = []
                print("Definindo cidr_blocks:")
                print("Obs: Para parar digite 0")
                while(1):
                    cidr_block = input("Cidr block: ")
                    if cidr_block == "0":
                        break
                    security_group_ingress_cidr_blocks.append(cidr_block)

                ingress = {
                    "from_port"   : security_group_ingress_from_port,
                    "to_port"     : security_group_ingress_to_port,
                    "description" : security_group_ingress_description,
                    "protocol"    : security_group_ingress_protocol,
                    "cidr_blocks" : security_group_ingress_cidr_blocks
                }
                security_group_ingress.append(ingress)
                
                continuar = input("Deseja adicionar mais uma regra: [s/n] ").lower()
                if continuar == "não" or continuar == "n" or continuar == "nao":
                    break
                
            security_group = {
                    "id"          : security_group_id,
                    "name"        : security_group_name,
                    "description" : security_group_description,
                    "ingress" : security_group_ingress
                }
            
            security_groups.append(security_group)
            
            continuar = input("Deseja adicionar mais um grupo de segurança: [s/n] ").lower()
            if continuar == "não" or continuar == "n" or continuar == "nao":
                break
        
        #Adciona usuario
        users = []
        while(1):
            users_name = input("Nome do usuário: ")
            user = {
                "name" : users_name
            }
            
            users.append(user)
            continuar = input("Deseja adicionar mais um usuário: [s/n] ").lower()
            if continuar == "não" or continuar == "n" or continuar == "nao":
                break
      
    var = {
        "users":users,
        "instances":instances,
        "security_groups": security_groups,
        "vpc_cidr": vpc_cidr
    }
   
    json_object = json.dumps(var, indent=4)

    with open('testes.tfvars.json', 'w') as f:
        f.write(json_object) 
             
    os.system('terraform plan -var-file="testes.tfvars.json"')
    

if __name__ == "__main__":
    main()