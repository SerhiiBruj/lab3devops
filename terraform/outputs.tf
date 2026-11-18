
output "api_id" {
  value = aws_api_gateway_rest_api.api.id
}

output "lambda_name" {
  value = aws_lambda_function.get_items.function_name
}

output "s3_bucket" {
  value = aws_s3_bucket.items.id
}

output "api_url" {
  value = "http://localhost:4566/restapis/${aws_api_gateway_rest_api.api.id}/dev/_user_request_/items"
}
