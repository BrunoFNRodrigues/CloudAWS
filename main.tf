provider "aws" {
  region = "us-east-1"

  profile = "${var.profile}" 

  access_key = "${var.access_key}"

  secret_key = "${var.secret_key}"
}

resource "aws" "name" {
  
}