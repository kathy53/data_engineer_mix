locals {
  credentials = jsondecode(file("../../secrets/az_credentials.json"))
}

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.10.0" # Or latest stable version
    }
  }

  required_version = ">= 1.3.0" # Ensures you are using a compatible Terraform version
}

# Authenticate into Azure using the cache
provider "azurerm" {
#  client_id       = local.credentials.client_id
#  client_secret   = local.credentials.client_secret
#  tenant_id       = local.credentials.tenant_id
  subscription_id = local.credentials.subscription_id
  features {}

}

# Create a resource group
resource "azurerm_resource_group" "your_project_rg" {
  name     = "your_project-rg"
  location = "West US"
}


# PostgreSQL Flexible Server Configuration
resource "azurerm_postgresql_flexible_server" "your_project_server" {
  name                          = "your_project-server"
  resource_group_name           = "your_project-rg"
  location                      = "West US"
  version                       = "13"
  public_network_access_enabled = true # Allows public access
  administrator_login           = local.credentials.administrator_login
  administrator_password        = local.credentials.administrator_password
  storage_mb                    = 32768
  sku_name                      = "GP_Standard_D2s_v3" # Smaller configuration for cost-saving
}

# PostgreSQL Database
resource "azurerm_postgresql_flexible_server_database" "your_project_database" {
  name      = "your_project-database"
  server_id = azurerm_postgresql_flexible_server.your_project_server.id
  charset   = "utf8"
  collation = "en_US.utf8"

  # prevent the possibility of accidental data loss
  # lifecycle {
  #   prevent_destroy = true
  # }
}

# Firewall Rule for Local Access
resource "azurerm_postgresql_flexible_server_firewall_rule" "allow_local_access" {
  name             = "allow-local-access"
  server_id        = azurerm_postgresql_flexible_server.your_project_server.id
  start_ip_address = local.credentials.public_ip_address
  end_ip_address   = local.credentials.public_ip_address
}