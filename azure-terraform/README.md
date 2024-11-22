# Starting with Terraform

It is necessary to create an application object in the Azure Home. In the browser navigate to the `Azure Active Directory` in the left menu. Go to App registrations. Add a `New Registration` by clicking in such button. Provide a name and click on the `Register` button.

To know more about te setup and credential creation watch https://www.youtube.com/watch?v=wB52Rd5N9IQ&list=PLLc2nQDXYMHowSZ4Lkq2jnZ0gsJL3ArAw&index=5

## main.tf
### Set the provider and versions
It is needed to start by setting up a provider and the app registration.\
About the provider you can find more information in https://registry.terraform.io/\
go to https://registry.terraform.io/providers/hashicorp/azurerm/latest and click on `USE PROVIDER` drop-down menu to copy the code to initialize your tf code. In this code snippet check that the version is the same that yours.
Then add the next block
```
terraform {}
```
### Set up credentials

1. While working locally, you can use the cache and use features{}
```
provider "azurerm" {
# used this while ruuning terraform locally after loggin using `az login` command
    features {}
}
```
2. If you don't own the Azure account ask the administrator for your credentials 
```
locals {
  credentials = jsondecode(file("<path_to_your_credntials_json_file>/secrets/az_credentials.json"))
}
provider "azurerm" {
    client_id       = local.credentials.client_id
    client_secret   = local.credentials.client_secret
    tenant_id       = local.credentials.tenant_id
    subscription_id = local.credentials.subscription_id
    features {}
}
```
For that you need to create a az_credentials.json

### Set resource group
It is necessary to set a resource group because all Azure resources must belong to one resource group.\
The groups are used for:
1. Logical organization
- Groups all related Azure resources for a project or workload (e.g., Storage Account, Database, Virtual Machines) under one container.
- Makes it easier to manage, monitor, and navigate resources.
2. Simplified Resource Management
- Actions like applying permissions, deleting, or moving resources can be done at the resource group level instead of individually.
3. Cost management
- Allows you to track costs for all resources within a resource group, helping with budgeting and chargebacks.
4. Lyfecycle management
- Deleting a resource group removes all the resources it contains, ensuring no leftover services are running and incurring charges.
5. Regional organization
- Ensures resources within the group share the same Azure region, which can reduce latency and improve performance.


## Terraform workflow
Terraform has Core commands:\
__init__ prepares your workspace (initialize the working directory that contins the terraform cofiguration files), so Terraform can apply your configuration.\
__plan__ allows you to preview the changes Terraform will make before you apply them, the changes are based on the configuration file.\
__apply__ makes the changes defined by your plan to create, update, or destroy resources.
__destroy__  it will destroy your infrastructure objects based on the Terraform configuration.
### Running commans based on our main.tf file for first time 
1. `terraform init`
The initialization was successed and a commit was made.
2. `terraform plan`
The command could were executed becasue the subscrption_id was no set correctly. The issue was fixed with the command
`export ARM_SUBSCRIPTION_ID="<subscrition_id>"`  
After setting the subscription_id another isse rose. To solve the issue read https://learn.microsoft.com/en-us/answers/questions/2103239/resource-provider-registration-issue
Include the line
`skip_provider_registration = "true"` in theprovider block 

# Creating the database
## Setting a server and a postgresql database
To create a postgresql  blocksin the 
1. azurerm_postgresql_flexible_server:
Creates a PostgreSQL server using the Flexible Server deployment option, which is cost-effective and supports public access.
2. azurerm_postgresql_flexible_server_database:
Adds a database (exampledb) to the server.
3. azurerm_postgresql_flexible_server_firewall_rule:
Configures a firewall rule to allow your local machine (based on its public IP) to connect to the database.
## Connecting to the postgresql database
The data needed to connect with the database is the following:

Host: example-psqlflexibleserver.postgres.database.azure.com
Port: 5432
User: psqladmin
Database: exampledb
Password: Your set password.