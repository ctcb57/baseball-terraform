module "bigquery" {
  source = "terraform-google-modules/bigquery/google"
  version = "~> 7.0"
  dataset_id = "${var.bg_dataset_name}${var.environment_underscore}"
  project_id = var.project
  location = "US"
}

# resource "bg_dataset_name" "dev_dataset" {
#   dataset_id = "${var.bq_dataset_name}${var.environment_underscore}"
#   location   = var.location
# }