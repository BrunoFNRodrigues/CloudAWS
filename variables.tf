variable "access_key" {
  type = string
  sensitive = true
}

variable "secret_key" {
  type = string
  sensitive = true
}

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "instances" {
  type = list(object({
    security_groups = list(string)
    name            = string
    ami             = string
    instance_type   = string
    region          = string
  }))
}

variable "security_groups" {
  type = list(object({
    id          = string
    name        = string
    description = string
    ingress = list(object({
      from_port   = number
      to_port     = number
      description = string
      protocol    = string
      cidr_blocks = list(string)
    }))
  }))
}

variable "users" {
  type = list(object({
    name = string
  }))

}

variable "vpc_cidr" {
  type = string
}

