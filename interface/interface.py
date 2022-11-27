import os
import json
import time


def main():
    while(1):
        print("""\nMENU PRICIPAL\n
            Escolha umas da opções asseguir:\n
            0 - Sair\n
            1 - Criar Recursos\n
            2 - Listar infraestrutura atual\n
            3 - Deletar infraestrutura\n
            4 - Subir na AWS e Sair\n""")
        option = input("Favor escrever apenas o número da opção(ex. 1): ")
        
        if option == "1":
            try: 
                with open("inputs.tfvars.json", "r") as f:
                    infra = json.load(f)
            except:
                print("Não foi encontrada uma infraestrutura prévia será necessário configurar uma VPC:")
                print("Configurando VPC:")
                vpc_cidr = input("VPC cidr: ")
                time.sleep(2)
                print("Configurando subnet:")
                time.sleep(2)
                infra = {"users":[], "instances":[],"security_groups":[],"vpc_cidr":vpc_cidr}


            while(1):
                print("""Criando recursos, escolha uma opção:\n
                        1 - Instâncias\n
                        2 - Grupos de segurança\n
                        3 - Usuários\n
                """)

                option = input("-> ")

                if option == "1":
                    #Adiciona instancia
                    instances = infra["instances"]
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
                elif option == "2":
                    #Adiciona security group
                    security_groups = infra["security_groups"]
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
                elif option == "3":   
                    #Adciona usuario
                    users = infra["users"]
                    while(1):
                        users_name = input("Nome do usuário: ")
                        user = {
                            "name" : users_name
                        }
                        users.append(user)
                        continuar = input("Deseja adicionar mais um usuário: [s/n] ").lower()
                        if continuar == "não" or continuar == "n" or continuar == "nao":
                            break
                else:
                    break
        
            json_object = json.dumps(infra, indent=4)

            with open('inputs.tfvars.json', 'w') as f:
                f.write(json_object) 
                    
        elif option == "2":
            while(1):
                print("""Listando recursos, escolha uma opção:\n
                        1 - Instâncias\n
                        2 - Grupos de segurança\n
                        3 - Usuários\n 
                """)
                option = input("-> ")
                if option == "1":
                    try : 
                        f =  open("inputs.tfvars.json")
                    except : 
                        print("Não há uma infraestrutura criada") 
                        pass
                    print("Lista de Instâncias:")
                    
                    instances = json.load(f)["instances"]
                    for instance in instances:
                        print("Nome -> "+ instance["name"])
                        print("Tipo -> "+ instance["instance_type"])
                        print("AMI -> "+ instance["ami"])
                        print("Região -> "+ instance["region"])
                        print("Grupos de segurança ->")
                        for sg in instance["security_groups"]:
                            print("     ->"+sg)
                        print(" ")
                elif option == "2":
                    try : 
                        f =  open("inputs.tfvars.json")
                    except : 
                        print("Não há uma infraestrutura criada") 
                        pass
                    print("Lista dos grupos de segurança:")
                    
                    sgs = json.load(f)["security_groups"]
                    f.close()

                    for sg in sgs:
                        print("Nome -> "+ sg["name"])
                        print("ID -> "+ sg["id"])
                        print("Descrição -> "+ sg["description"])
                        print("Regras de ingresso ->")
                        for r in sg["ingress"]:
                            print("     Porta de entrada-> "+r["from_port"])
                            print("     Porta de saída-> "+r["to_port"])
                            print("     Descrição-> "+r["description"])
                            print("     Protocolo-> "+r["protocol"])
                            print("     Cidr blocks-> ")
                            for block in r["cidr_blocks"]:
                                print("         -> "+block)
                            print(" ")

                elif option == "3":
                    try : 
                        f =  open("inputs.tfvars.json")
                    except : 
                        print("Não há uma infraestrutura criada") 
                        pass
                    print("Lista dos usuários:")
                    
                    users = json.load(f)["users"]
                    f.close()

                    for user in users:
                        print("Nome -> "+user["name"]+"\n")

                else:
                    break
                        
        elif option == "3":
            try : 
                f =  open("inputs.tfvars.json")
                infra = json.load(f)
                f.close()
            except : 
                print("Não há uma infraestrutura criada") 
                pass

            while(1): 
                print("""Removendo recursos, escolha uma opção:\n
                        1 - Instâncias\n
                        2 - Grupos de segurança\n
                        3 - Usuários\n
                        4 - Tudo\n 
                """)
                option = input("-> ")

                if option == "1":
                    print("Lista de Instâncias:")
                    
                    instances = infra["instances"]
                    flag = ""
                    while(flag != "n"):
                        i = 0
                        for instance in instances:
                            print(str(i)+": Nome -> "+ instance["name"])
                            i += 1
                        i = input("-> ")
                        instances.pop(int(i))
                        
                        if len(instances) > 0:
                            flag = input("Deseja continuar a remover[s/n]: ")
                        else:
                            flag = "n"

                elif option == "2":
                    print("Lista dos grupos de segurança:")
                    
                    sgs = infra["security_groups"]
                    flag = ""
                    while(flag != "n"):
                        i = 0
                        for sg in sgs:
                            print(str(i)+": Nome -> "+ sg["name"])
                            i += 1
                        i = input("-> ")
                        sgs.pop(int(i))

                        if len(sgs) > 0:
                            flag = input("Deseja continuar a remover[s/n]: ")
                        else:
                            flag = "n"
                    

                elif option == "3":
                    print("Lista dos grupos de segurança:")
                    
                    users = infra["users"]
                    flag = ""
                    while(flag != "n"):
                        i = 0
                        for user in users:
                            print(str(i)+": Nome -> "+ user["name"])
                            i += 1
                        i = input("-> ")
                        users.pop(int(i))

                        if len(users) > 0:
                            flag = input("Deseja continuar a remover[s/n]: ")
                        else:
                            flag = "n"
                    

                elif option == "4":
                    print("Deletando toda infraestrutura:")
                    
                    os.system("terraform destroy")
                
                else:
                    break

                infra = json.dumps(infra, indent=4)

                with open('inputs.tfvars.json', 'w') as f:
                    f.write(infra)                 
        
        elif option == "4":
            os.system('terraform plan -var-file="inputs.tfvars.json"')
        
        elif option == "0":
            break
        
        else:
            print("Entrada inválida")
            time.sleep(2)
            
            







    

if __name__ == "__main__":
    main()