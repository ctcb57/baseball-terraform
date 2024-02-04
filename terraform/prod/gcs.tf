resource "google_storage_bucket" "data-lake-bucket-prod" {
  # count    = var.is_prod ? 1 : 0
  name     = "${var.gcs_bucket_name}${var.environment}"
  location = var.location

  # Optional, but recommended settings:
  storage_class               = var.gcs_storage_class
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30 // days
    }
  }

  force_destroy = true
}

# resource "google_storage_bucket" "data-lake-bucket" {
#   # count    = var.is_dev ? 1 : 0
#   name     = "${var.gcs_bucket_name}${var.environment}"
#   location = var.location

#   # Optional, but recommended settings:
#   storage_class               = var.gcs_storage_class
#   uniform_bucket_level_access = true

#   versioning {
#     enabled = true
#   }

#   lifecycle_rule {
#     action {
#       type = "Delete"
#     }
#     condition {
#       age = 30 // days
#     }
#   }

#   force_destroy = true
# }