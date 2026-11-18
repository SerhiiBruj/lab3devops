
variable "bucket_name" {
  description = "S3 bucket name"
  type        = string
  default     = "serhii-api-items-bucket"
}

variable "function_name" {
  description = "Lambda function name"
  type        = string
  default     = "get-items-function"
}

variable "api_name" {
  description = "API Gateway name"
  type        = string
  default     = "items-api"
}
