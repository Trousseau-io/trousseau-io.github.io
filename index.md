---
layout: default
---

### why Trousseau

Kubernetes platform users are all facing the very same question; ***how to handle Secrets?***   

While there are significant efforts to improve Kubernetes component layers, [the state of Secret Management is not receiving much interests](https://fosdem.org/2021/schedule/event/kubernetes_secret_management/).   
Using *etcd* to store API object definition & states, Kubernetes secrets are encoded in Base64 and shipped into the key value store database.  Even if the filesystems on which *etcd* runs are encrypted, the secrets are still not.   

Instead of leveraging the native Kubernetes way to manage secrets, commercial and open source solutions solve this design flaw by leveraging different approaches all using different toolsets or practices. This leads to training and maintaining niche skills and tools increasing cost and complexity of Kubernetes day 0, 1 and 2. 

Once deployed, Trousseau will enable seamless secret management using the native Kubernetes API and ```kubectl``` CLI usage while leveraging an existing Key Management Service (KMS) provider.  
How? By using using the [Kubernetes KMS provider](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/) framework to provide an envelop encryption scheme to encrypt secrets on the fly.

### what is Trousseau

Trousseau is: 

* Open source project
* design based on [Kubernetes KMS provider design](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)
* design to be a framework for any KMS provider (see release notes)
* Easy deployment
* API driven approach

### about the name
The name *Trousseau* comes from the French language and is usually associated with keys like in *trousseau de clés* meaning *keyring*.
