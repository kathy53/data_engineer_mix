# n8n setup

## PostgreSQL database for n8n
Create a PostgreSQL to use with n8n service. we are going to based the setup in the docs `https://github.com/n8n-io/n8n-hosting/tree/main/kubernetes`

The database is going to be created in a namespace called `databases` which already exists.\
Remember create kubernetes secrets using kubectl or like in this case manually filling a YAML with base64-encoded fields

    echo -n 'to_encode' | base64
pass the output into the YAML file.

The PVC will work with the default StorageClass\
The database is called "n8n"

Run the following YAML files:

    kubectl apply -f [path]/postgres-secrets.yaml
    kubectl apply -f [path]/postgres-claim0-persistentvolumeclaim.yaml
    kubectl apply -f [path]/postgres-configmap.yaml
    kubectl apply -f [path]/postgres-deployment.yaml
    kubectl apply -f [path]/postgres-service.yaml

Check for:
1. The pod `kubectl get pods -n databases`
2. Connect to the database `kubectl exec -n <namespace> -it <pod_name> -- psql -U <POSTGRES_USER> -d <databasename> -c "\du"` where "\du" list the users. You can omit '-c "\du" to get an interactive psql shell.


## Setup for n8n
To access the n8n service from another machine in the same local neetwork use # access at `http://<laptop-ip>:30081`
### Creating namesapace

    kubectl apply -f [path]/n8n-namespace.yaml

## Running n8n
    kubectl apply -f n8n-secrets.yaml
    kubectl apply -f n8n-claim0-persistentvolumeclaim.yaml
    kubectl apply -f n8n-deployment.yaml

## Verify deployment
    kubectl get pods -n n8n
    kubectl get svc -n n8n
    kubectl logs -n n8n <n8n-pod-name>


## Test the connection 
    kubectl exec -n n8n -it <n8n-pod-name> -- sh

Inside pod

    apt update && apt install -y postgresql-client

if needed

    psql -h postgres.database.svc.cluster.local -U n8nuser -d n8ndb


# Connecting to n8n
Now the service is running. We can connect by:
1. __port-forward__ through port 5678 using `kubectl port-forward svc/n8n -n n8n 5678` You can list services by typing `kubectl get svc -n <nammespace>` This way is useful if you want to debugging or troubleshooting, as it only exposes the service or pod to your local machine.  There is no security issues in this option. 

2. __through Internet__ using a DNS `n8n.ajaw.duckdns.org` 