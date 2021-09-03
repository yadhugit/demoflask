# Demo Flask App Project ![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)  ![image](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)
This is a demo project to show how to deploy a two tier application using a [K8s](https://kubernetes.io/) cluster ( [minikube](https://minikube.sigs.k8s.io/docs/start/) ) 

## Pre-requisites

- [Minikube](https://minikube.sigs.k8s.io/docs/start/) installed and running.
- Virtualization enabled in the host.
- [Docker](https://docs.docker.com/engine/install/) installed.
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) CLI installed.

## To execute the project using [Minikube](https://minikube.sigs.k8s.io/docs/start/)  [K8s](https://kubernetes.io/) cluster :

1. execute below command using [Minikube](https://minikube.sigs.k8s.io/docs/start/). :

```bash
minikube start
```

2. clone the github repo using :
```bash 
git clone https://github.com/yadhugit/demoflask.git
```

3. change directory k8s_resources/flaskapp :

```bash 
cd demoflask/k8s_resources/flaskapp
```

4. Execute deployment file inside the k8s_resources/flaskapp folder respectively using k8s.

```bash 
kubectl create -f deployment-svc-conf.yaml
```
5. change directory k8s_resources/mysql :

```bash 
cd demoflask/k8s_resources/mysql
```

6. Execute deployment file inside the k8s_resources/mysql folder respectively using k8s.

```bash 
kubectl create -f mysql-deploy-svc-pv.yaml
```


will create flask app deployment, services in your PC

7. Use below command to get your service url,
```bash
minikube service demoflask-service --url
```
 and open url up your default browser.