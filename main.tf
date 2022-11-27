#Cria VPC
resource "aws_vpc" "VPC" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true


  tags = {
    Name = "VPC"
  }

}

#Cria subnet
resource "aws_subnet" "public_subnet" {
  vpc_id     = aws_vpc.VPC.id
  cidr_block = cidrsubnet(var.vpc_cidr, 4, 1)

  tags = {
    Name = "PublicSubnet"
  }
}

#Cria Gateway
resource "aws_internet_gateway" "subnet_igw" {
  vpc_id = aws_vpc.VPC.id

  tags = {
    Name = "subnet-igw"
  }

}

resource "aws_route_table" "subnet_public_crt" {
  vpc_id = aws_vpc.VPC.id

  route {
    //associated subnet can reach everywhere
    cidr_block = "0.0.0.0/0"
    //CRT uses this IGW to reach internet
    gateway_id = aws_internet_gateway.subnet_igw.id
  }

  tags = {
    Name = "prod-public-crt"
  }
}

resource "aws_route_table_association" "crta_public_subnet" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.subnet_public_crt.id
}

#Cria instancia
resource "aws_instance" "instance" {
  for_each               = { for instance in var.instances : instance.name => instance }
  ami                    = each.value.ami
  instance_type          = each.value.instance_type
  subnet_id              = aws_subnet.public_subnet.id
  vpc_security_group_ids = [for security_group in aws_security_group.SecurityGroup : security_group.id if contains(each.value.security_groups, security_group.tags.Name)]
  #  key_name               = "teste"
  tags = {
    Name = each.value.name
  }
}

#Cria Security Group
resource "aws_security_group" "SecurityGroup" {
  for_each    = { for security_group in var.security_groups : security_group.name => security_group }
  name        = each.value.name
  description = each.value.description
  vpc_id      = aws_vpc.VPC.id
  tags = {
    Name = each.value.name
  }
  dynamic "ingress" {
    for_each = each.value.ingress

    content {
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      description = ingress.value.description
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }
}

#Cria usario
resource "aws_iam_user" "TfUser" {
  for_each = { for user in var.users : user.name => user }
  name     = each.value.name

  tags = {
    Name = each.value.name
  }
}

#Distribui chaves de acesso
resource "aws_iam_access_key" "user_access_key" {
  for_each = { for user in var.users : user.name => user }
  user     = aws_iam_user.TfUser[each.value.name].name
}

#Cria perfil de login
resource "aws_iam_user_login_profile" "user_profile" {
  for_each                = { for user in var.users : user.name => user }
  user                    = aws_iam_user.TfUser[each.value.name].name
}
