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


## Creating namesapace
```
kubectl apply -f [path]/db-namespace.yaml
```
## Running a PostGIS database
```
kubectl apply -f [path]/n8n-claim0-persistentvolumeclaim.yaml
kubectl apply -f [path]/service_postgis.yaml
kubectl apply -f [path]/secret_postgis.yaml
kubectl apply -f [path]/pipeline_postgis.yaml

```
or
```
kubectl apply -f pipeline_postgis/