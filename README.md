# Projeto Terraform AWS
### - Bruno Freita do Nascimento Rodrigues
---
# Guia de utilização:
## Configuração:
Primeiro é necessário criar um arquivo chamado *terraform.tfvars*, e conteúdo dele deve seguir o padrão abaixo:
```
access_key = "{sua acecss key}"
secret_key = "{sua secret key}" 
```
Para executar o programa use o comando, na raiz do repositório:
```
python interface/interface.py
```

## Uso:
Ao executar o arquivo *interface.py*, o programa começa no menu principal, no qual é possível escolher uma opção de configuração digitando o número associado a opção:
```
MENU PRICIPAL

            Escolha uma das opções asseguir:

            0 - Sair

            1 - Criar Recursos

            2 - Listar infraestrutura atual

            3 - Deletar infraestrutura

            4 - Subir na AWS e Sair

Favor escrever apenas o número da opção(ex. 1): 0
```
As opções 1, 2 e 3 levam a menus com comportamento semelhante a esse.

## Criar Recursos:
Caso não haja nenhuma infraestrutura criada antes de acessar o menu será necessário configurar uma VPC:
```
Não foi encontrada uma infraestrutura prévia será necessário configurar uma VPC:
Configurando VPC:
VPC cidr:
```
Após configura a VPC ou caso já exista uma infraestrutura préviao o menu irá aparecer.
As opcções possuem o seguinte comportamento: 
```
1. Permite criar uma ou mais intâncias, sendo necessário configurar nome, grupos de segurança que ela faz parte, imagem (ami) e tipo da instância.

2. Permite criar um ou mais grupos de segurança, sendo necessário configurar id, nome, descrição, regras de ingresso.

3. Perimite criar um ou mais usuários sendo necessário passar apenas o nome. 
```

## Listar Recursos:
```
1. Lista todas as intâncias.

2. Lista todos os grupos de segurança.

3. Lista todos os usuários. 
```

## Remover Recursos:
```
1. Permite remover uma ou mais intâncias.

2. Permite remover um ou mais grupos de segurança.

3. Permite remover um ou mais usuários.

4. Remove toda a infraestrutura.
```