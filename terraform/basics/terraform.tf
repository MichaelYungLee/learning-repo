terraform {
  required_version = ">= 1.0.0"
  required_providers {
    aws = {
      version = ">= 5.0.0"
      source  = "hashicorp/aws"
    }
    local = {
      source  = "hashicorp/local"
      version = "2.1.0"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "3.1.0"
    }
  }
}