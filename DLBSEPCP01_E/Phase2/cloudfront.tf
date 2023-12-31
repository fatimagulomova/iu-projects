# Step 6: Set up a CloudFront Distribution
locals {
  s3_origin_id = var.s3_origin_id
}

resource "aws_cloudfront_distribution" "s3_distribution" {
  depends_on = [aws_s3_bucket.s3bucket]

  origin {
    domain_name = aws_s3_bucket.s3bucket.bucket_regional_domain_name
    origin_id   = local.s3_origin_id
  }

  enabled             = true
  is_ipv6_enabled     = var.ipv6_enabled
  default_root_object = var.default_root_object

  viewer_certificate {
    cloudfront_default_certificate = true
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
      locations        = []
    }
  }

  default_cache_behavior {
    cache_policy_id        = var.cache_behavior.cache_policy_id
    viewer_protocol_policy = var.cache_behavior.viewer_protocol_policy
    allowed_methods        = var.cache_behavior.allowed_methods
    cached_methods         = var.cache_behavior.cached_methods
    target_origin_id       = local.s3_origin_id
  }
}