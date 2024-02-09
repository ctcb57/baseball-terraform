locals {
  datasets = jsondecode(file("${path.module}/resource/datasets.json"))["datasets"]
}

resource "google_bigquery_dataset" "datasets" {
  for_each = local.datasets

  project    = var.project
  dataset_id = each.value["dataset_id"]
  location   = "US"
}
