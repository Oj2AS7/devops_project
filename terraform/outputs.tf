output "cluster_name" {
  description = "EKS cluster name"
  value       = module.eks.cluster_name
}

output "cluster_endpoint" {
  description = "EKS cluster control plane endpoint"
  value       = module.eks.cluster_endpoint
}

output "vpc_id" {
  description = "AWS VPC ID"
  value       = module.vpc.vpc_id
}
