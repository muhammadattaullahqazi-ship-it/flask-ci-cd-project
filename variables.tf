# variables.tf - Variable definitions

variable "aws_region" {
  description = "The AWS region to deploy resources in"
  type        = string
  default     = "us-east-1"
}

variable "ssh_allowed_cidr" {
  description = "CIDR block allowed to SSH into the instance (your own public IP/32, never 0.0.0.0/0)"
  type        = string
}