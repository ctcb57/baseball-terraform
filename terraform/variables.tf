variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-creds.json"
}

variable "project" {
  description = "My project"
  default     = "alien-sol-412801"
}

variable "region" {
  description = "My region"
  default     = "us-central1"
}


variable "location" {
  description = "My Project Location"
  default     = "US"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "baseball-project-charles-clark-1"
}


variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}