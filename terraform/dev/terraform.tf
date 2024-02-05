terraform {
  required_version = ">= 0.14"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">=3.3"
    }
  }

  backend "gcs" {}
}

provider "google" {
  project = var.project
  region  = var.region
}