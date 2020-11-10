--- 
layout: default
---

[back](./)

## Trousseau roadmap

### Current work
Based on the DTAP (Dev, Test, Acceptance, Production) approach, there are not yet any "TAP" releases.
The current work is available as a "dev" branch within the [Trousseau repo](https://github.com/Trousseau-io/trousseau).

### Near-future work
The first aim is to define a simple architecture along with an iterative coding approach to bring quickly to life a MVP (Minimal Viable Product) that will serve as a catalyst for contributors to bring the best of the open source and community development.

The features for the first MVP release are:
* An open source project under GPL3.0 using packages/modules under the same license to avoid any license or IP disputes
* Golang as dev langugage
* A client/server approach using a RESTFul interface compliant with the [OpenAPI Specification] using TLS to secure the CRUD (Create, Read, Update, Delete) operations.
* A reliable and encrypted key-value store 

### Future work
The features for the next MVP release are:
* Deployment of the solution using an operator
* A reliable distributed key/value store scalable from 1 to at least 3 instances to achieve high availability
* Sidecar option for pods
* Zero Trust capabilities 
