# Setup to run LLMs locally by using Ollama running on a Kubernetes pod

## Kubernetes setup
- Create a namespace `kubectl create namespace ollama`
- Create a persistant volume to store models and avoid to re-download them
- Create a deployment file. Using the latest Docker image in November, 2025 ollama:0.12.9
- Create a service file

Run each file:
    kubectl apply -f _infra/

Check your installation by exec the pod and verify the Ollama version with the next commands:

    kubectl exec -it -n ollama deploy/ollama -- bash
    ollama --version

