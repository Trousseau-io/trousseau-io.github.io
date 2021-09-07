---
layout: default
---

### why Trousseau

Kubernetes platform users are all facing the very same question; how to handle Secrets?   

While there are significant efforts to improve Kubernetes component layers, [the state of Secret Management is not receiving much interests](https://fosdem.org/2021/schedule/event/kubernetes_secret_management/).   
Using *etcd* to store API object definition & states, Kubernetes secrets are encoded in Base64 and shipped into the key value store database.  Even if the filesystems on which *etcd* runs are encrypted, the secrets are still not.   

To solve this design flaw, both commercial and open source solutions exist leveraging different approaches to handle secrets calling for a different set of tools or practices instead of leveraging the native Kubernetes way to manage secrets. This leads to training and maintaining niche skills and tooling set increasing cost and complexity of Kubernetes day 2 operations. 

With Trousseau, any user/workload can leverage the native Kubernetes way to store and access secrets in a safe way by plugin to any Key Management Service (KMS) provider using the [Kubernetes KMS pluging](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/) framework.

### what is Trousseau

Trousseau is: 

* Open source project
* Kubernetes native respecting the [Kubernetes KMS plugin design](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)
* Universal plugin addressing potentially any KMS provider
* Easy deployment
* API driven approach

### about the name
The name "Trousseau" comes from the French language used within the context of "Trousseau de clés" or "Keyring".
