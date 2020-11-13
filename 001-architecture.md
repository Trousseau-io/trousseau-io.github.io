--- 
layout: default
---

[back](./)

## Trousseau architecture

As per Trousseau [roadmap](./005-roadmap.html), releases are defined as a MVP or Minimal Viable Product with a well defined set of features.

## near-future 
### MVP1.0
The version 1.0 target a production grade MVP with a limited set of features matching 3 simple use cases from which features are defined.

Use cases:
* create, read, update, delete (CRUD) operations of secrets from a CLI perspective
* handle a secret type to access an external service like a DB
* provide the basic health status of the service
The extra mile
* Read a secret a application within a container using minikube

Required features for the use cases:
* single instance encrypted key-value store 
* server (trousseaud) to act as a broker with the key-value store for clients 
* command line interface (clectl) to interact with the server instance
* validate identity via Kubernetes Auth method
* validate authorization access 1 single simple policy (if identity ok, access granted)

### MVP1.0 blueprint overview
The MVP1.0 architecture aims to a single instance approach with a limited the code footprint and components. Trousseau MVP1.0 will consist of several main components working securely to handle CRUD operations:

* ```clectl```; the command line interface providing connectivity to one or multiple Trousseau instances and handle CRUD operations
* ```trousseaud```; the server instance acting as a broker towards the key-value store
* key-value store; the key-value store is based on a single instance of an encrypted key-value store instance at the current stage 

The below figure shows a basic representation of the flow: 
![mvp1overview](https://raw.githubusercontent.com/Trousseau-io/trousseau-io.github.io/main/assets/diagrams/trousseau_mvp1_-_overview.png)

### MVP1.0 Use cases
#### create, read, update, delete (CRUD) operations of Secrets from a CLI perspective
The use case takes into consideration two scenarios related to the creation of secrets:
* injecting an existing secret
* generating a new secret

##### injecting an existing secret
This scenario takes an already existing secret, like the credentials ```john/mysuprP@ssw0rd```, and injects it within Trousseau, either for safe keeping or for dynamic usage within an application. 
From a secret perspective, this is what could be called an "almost secret" since the key-value is either existing within another systems or files (happy csv/xls day!) and the pair will transit to Trousseau. This scenario will unmasked the secret and expose it to potential leakage during CLI handling prior to transiting to ```trousseaud```.

![existingcredentials](https://raw.githubusercontent.com/Trousseau-io/trousseau-io.github.io/main/assets/diagrams/trousseau_mvp1_-_simple_credentials.png)

From an operation perspective, the ```create``` operation will require to format as safely as possible the existing secret in order to transfer it to ```trousseaud``` after being process via ```clectl```. Considering the above diagram, the main surface attack exists prior to the transfer to ```trousseaud```.

##### generating a new scret
This scenario takes a different approach about generated a secret while being totally ofuscated to the user. The user will ```create``` a new secret which can be retrieve later from a CLI, API and Kubernetes secret perspective, and even be securely passed to a service like a DB (see next use case details).

![generatingsecrets](https://raw.githubusercontent.com/Trousseau-io/trousseau-io.github.io/main/assets/diagrams/trousseau_mvp1_-_generate_a_secret.png)

Considering the above diagram, generating a secret from a client side will not expose the secret value as the overall process is carried over at the server side.

#### handle a secret to access an external service like a DB
This scenario leverage the generating a new secret and pass it to services for which a package has been define to insure a full secure transition of the credetentials to that service. 

![generatingsecrets](https://raw.githubusercontent.com/Trousseau-io/trousseau-io.github.io/main/assets/diagrams/trousseau_mvp1_-_generate_&_handle_a_secret_to_a_3rd_party.png)

#### provide the basic health status of the service

### MVP1.0 Features

## future work
This section provides an overview of Trousseau vision for the next MVP releases.

### MVP1.5
The MVP1.5 architecture aims to provide a high available architecture allowing full resilience and hybrid scenario. 


