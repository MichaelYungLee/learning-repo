output "vpc_id" {
  description = "Output the ID for the primary VPC"
  value       = aws_vpc.vpc.id
}

output "public_url" {
  description = "Public URL for our Web Server"
  value       = "https://${aws_instance.web_server.private_ip}:8080/index.html"
}

output "vpc_information" {
  description = "VPC Information about Environment"
  value       = "Your ${aws_vpc.vpc.tags.Environment} VPC has an ID of ${aws_vpc.vpc.id}"
}

output "public_ip" {
  value = aws_instance.web_server.public_ip
}

output "ec2_instance_arn" {
  value = aws_instance.web_server.arn
  sensitive = true
}

/* output "public_dns" {
  value = module.server.public_dns
}

output "size" {
  value = module.server.size
}

output "asg_group_size" {
  value = module.autoscaling.autoscaling_group_max_size
}

output "s3_bucket_name" {
  value = module.s3-bucket.s3_bucket_bucket_domain_name
} */