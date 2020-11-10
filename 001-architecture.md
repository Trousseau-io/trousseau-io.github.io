--- 
layout: default
---

[back](./)

## Trousseau architecture

As per Trousseau [roadmap](./005-roadmap.html), releases are defined as a MVP or Minimal Viable Product with a well defined set of features. The 

## near-future 

### MVP1.0
The version 1.0 target a production grade MVP with a limited set of features matching 3 simple use cases.

Use cases
* Create, Read, Update, Delete (CRUD) operations of Secrets from a CLI perspective
* Handle a secret type "login credential" to access an external service like a DB
* Provide the basic health status of the service

The extra mile
* Read a secret a application within a container using minikube

Features
* Single instance encrypted key-value store 
* Server (trousseaud) to act as a broker with the key-value store for clients 
* Command line interface (clectl) to interact with the server instance
* Validate identity via Kubernetes Auth method
* Validate authorization access 1 single simple policy (if identity ok, access granted)

### MVP1.0 blueprint 
The architecture takes into consideration two 




## future work
TODO