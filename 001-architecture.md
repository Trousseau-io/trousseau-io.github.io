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
The MVP1.0 architecture aims to a single instance approach with a limited the code footprint and components. Trousseau MVP1.0 will consist of several main components working securely to handle CRUD operations:

* clectl; the command line interface providing connectivity to one or multiple Trousseau instances and handle CRUD operations
* trousseaud; the server instance acting as a broker towards the key-value store
* key-value store; the key-value store is based on a single instance of an encrypted etcd at the current stage 

The below figure shows a basic representation of the flow: 
![mvp1overview](https://raw.githubusercontent.com/Trousseau-io/trousseau-io.github.io/main/assets/diagrams/trousseau_mvp1_-_overview.png)

### MVP1.0 CRUD Operations
The architecture takes into consideration two scenarios related to the creation of secrets:
* existing credentials to become a new secret 
* generating a new secret

The first scenario of bringing existing credentials to be converted to a secret can't be optimized for security as per their origins:

![existingcredentials](https://raw.githubusercontent.com/Trousseau-io/trousseau-io.github.io/main/assets/diagrams/trousseau_mvp1_-_simple_credentials.png)

Considering the above diagram, existing credentials will be processes by the client towards the server to be inserted within the key-value store. 
This scenario exposes the secret at the client side level which, despite many different approach, could be retrieved in different ways. 

The second scenario of generating a new secret offers the capability of totally ofuscating its value.

![generatingsecrets](https://raw.githubusercontent.com/Trousseau-io/trousseau-io.github.io/main/assets/diagrams/trousseau_mvp1_-_generate_a_secret.png)

Considering the above diagram, generating a secret from a client side will not expose the secret value from that standpoint as the overall process is carried over at the server side. 

## future work
This section provides an overview of Trousseau vision for the next MVP releases.

### MVP1.5
The MVP1.5 architecture aims to provide a high available architecture allowing full resilience and hybrid scenario. 


