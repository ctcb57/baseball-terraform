locals {
  roles = [
    "roles/resourcemanager.projectIamAdmin", # GitHub Actions identity
    "roles/editor",                          # allow to manage all resources
  ]
  github_repository_name = "ctcb57/baseball-terraform" # e.g. yourname/yourrepo
}

resource "google_service_account" "github-actions-prod" {
  project      = var.project
  account_id   = "github-actions-prod"
  display_name = "github actions prod"
  description  = "Prod link to Workload Identity Pool used by GitHub Actions"

}

# Allow to access all resources
resource "google_project_iam_member" "roles-prod" {
  project = var.project
  for_each = {
    for role in local.roles : role => role
  }
  role   = each.value
  member = "serviceAccount:${google_service_account.github-actions-prod.email}"
}

resource "google_iam_workload_identity_pool" "github-prod" {
  provider                  = google-beta
  project                   = var.project
  workload_identity_pool_id = "github-prod"
  display_name              = "github prod"
  description               = "for GitHub Actions"
}

resource "google_iam_workload_identity_pool_provider" "github-prod" {
  provider                           = google-beta
  project                            = var.project
  workload_identity_pool_id          = google_iam_workload_identity_pool.github-prod.workload_identity_pool_id
  workload_identity_pool_provider_id = "github-provider-prod"
  display_name                       = "github actions provider prod"
  description                        = "OIDC identity pool provider for execute GitHub Actions"
  # See. https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#understanding-the-oidc-token
  attribute_mapping = {
    "google.subject"       = "assertion.sub"
    "attribute.repository" = "assertion.repository"
    "attribute.owner"      = "assertion.repository_owner"
    "attribute.refs"       = "assertion.ref"
  }

  oidc {
    issuer_uri = "https://token.actions.githubusercontent.com"
  }
}

resource "google_service_account_iam_member" "github-actions-prod" {
  service_account_id = google_service_account.github-actions-prod.name
  role               = "roles/iam.workloadIdentityUser"
  member             = "principalSet://iam.googleapis.com/${google_iam_workload_identity_pool.github-prod.name}/attribute.repository/${local.github_repository_name}"
}

output "service_account_github_actions_email" {
  description = "Service Account used by GitHub Actions"
  value       = google_service_account.github-actions-prod.email
}

output "google_iam_workload_identity_pool_provider_github_name" {
  description = "Workload Identity Pood Provider ID"
  value       = google_iam_workload_identity_pool_provider.github-prod.name
}