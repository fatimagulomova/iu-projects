# Step 7: Get the Outputs
output "cloudfront_id" {
  description = "Cloudfront ID"
  value       = aws_cloudfront_distribution.s3_distribution.id
}

output "cloudfront_url" {
  description = "Cloudfront distribution URL (HTTPS)"
  value       = "https://${aws_cloudfront_distribution.s3_distribution.domain_name}"
}

output "s3_url" {
  description = "S3 hosting URL"
  value       = aws_s3_bucket_website_configuration.static_website_bucket.website_endpoint
}
