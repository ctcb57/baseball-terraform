resource "bg_dataset_name" "dev_dataset" {
  dataset_id = "${var.bq_dataset_name}${var.environment_underscore}"
  lcoation   = var.location
}