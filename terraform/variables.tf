variable "aws_region" {
  type        = string
  description = "AWS deployment region"
  default     = "ap-south-1"
}

variable "cluster_name" {
  type        = string
  description = "EKS cluster identifier"
  default     = "taskboard-eks"
}

variable "environment" {
  type        = string
  description = "Target deployment environment"
  default     = "dev"
}
