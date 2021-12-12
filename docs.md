---
layout: default
---

Table of contents
* [Documentaton](#documentation)
  * [Release Notes](#release-notes)
* [Installation with HashiCorp Vault](#installation-with-hashicorp-vault)  
* [Setup HashiCorp Vault](#setup-hashicorp-vault)  
  * [Requirements](#requirements)  
  * [Shell Environment Variables](#shell-environment-variables)  
  * [Enable a Transit Engine](#enable-a-transit-engine)  
* [Kubernetes](#kubernetes)
  * [Vanilla k8s](#vanilla-k8s-like-gke)  
  * [RKE Specifics](#rke-specifics)
  * [RKE2 Specifics](#rke2-specifics)    
* [Setup monitoring](#setup-monitoring)  

# Documentation

## Release Notes

### Release of Trousseau [v1.0.0](https://github.com/Trousseau-io/trousseau/releases/tag/v1.0.0) (aka 'Funny Cookie') - December 1st 2021

*'Funny Cookie' is out of the box!*

We are please to release the very first version of Trousseau this December 1st 2021!
Trousseau is a Kubernetes KMS Provider plugin with support of Hashicorp Vault.

The current release offers the followings:
- respectful of the [Kubernetes KMS Provider](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/) framework
- provide support for Hashicorp Vault Community, Enterprise and Cloud Platform based deployment
- deployment tested on Vanilla, RKE, and RKE2 Kubernetes clusters
- build on distroless for small footprint 

The complementary asset is the container image accessible via the tag ```latest``` or ```v1.0.0```:

```shell
docker pull ghcr.io/trousseau-io/trousseau:latest 
```

The Trousseau Project would like to thanks @wwojcik and @kruc for their precious contributions! 

Reference: GitHub repository [Release notes](https://github.com/Trousseau-io/trousseau/releases)

# Installation with HashiCorp Vault

## Requirements
The following are required:
- a working kubernetes cluster with access to the control plane nodes 
- a HashiCorp Vault instance (Community or Enterprise)
- a SSH access to the control plane nodes as an admin
- the necessary user permissions to handle files in ```etc``` and restart serivces, root is best, sudo is better ;)
- the vault cli tool 
- the kubectl cli tool

## Setup HashiCorp Vault

### Shell Environment Variables
Export environment variables to reach out the HashiCorp Vault instance:

```bash
export VAULT_ADDR="https://addresss:8200"
export VAULT_TOKEN="s.oYpiOmnWL0PFDPS2ImJTdhRf.CxT2N"
```
   
**NOTE: when using the HashiCorp Vault Enterprise, the concept of namespace is introduced.**   
This requires an additional environment variables to target the base root namespace:

```bash
export VAULT_NAMESPACE=admin
```
or a sub namespace like admin/gke01

```bash
export VAULT_NAMESPACE=admin/gke01
```

### Enable a Transit engine

Make sure to have a Transit engine enable within Vault:

```bash
vault secrets enable transit

Success! Enabled the transit secrets engine at: transit/
```

List the secret engines:
```bash
vault secrets list
Path          Type            Accessor                 Description
----          ----            --------                 -----------
cubbyhole/    ns_cubbyhole    ns_cubbyhole_491a549d    per-token private secret storage
identity/     ns_identity     ns_identity_01d57d96     identity store
sys/          ns_system       ns_system_d0f157ca       system endpoints used for control, policy and debugging
transit/      transit         transit_3a41addc         n/a
```

**NOTE about missing VAULT_NAMESPACE**  
Not exporting the VAULT_NAMESPACE will results in a similar error message when enabling the transit engine or even trying to list them:

```
vault secrets enable transit

Error enabling: Error making API request.

URL: POST https://vault-dev.vault.3c414da7-6890-49b8-b635-e3808a5f4fee.aws.hashicorp.cloud:8200/v1/sys/mounts/transit
Code: 403. Errors:

* 1 error occurred:
        * permission denied
```

Finally, create a transit key:

```bash
vault write -f transit/keys/vault-kms-demo
Success! Data written to: transit/keys/vault-kms-demo
```

## Kubernetes
### vanilla k8s
**The following steps needs to be executed on every node part of the control plane; usually one master node in dev/test environment, 3 in production environment.**

The Trousseau KMS Vault provider plugin needs to be set as a Pod starting along with the kube-apimanager.  
To do so, the ```vault-kms-provider.yaml``` configuration file from ```scripts/k8s``` can be used as a template and should be added to every nodes part of the control plane within the directory ```/etc/kubernetes/manifests/```.   

**Note that only the image version and the Vault namespace are open for changes to match your enviroment and everything else is at your own risks.**

Then, create the directory ```/opt/vault-kms/``` to hosts the trousseau configuration files:
* ```config.yaml``` to be update to match your environment
* ```encryption_config.yaml``` as-is and to not modify for any reasons

Add the parameter ```--encryption-provider-config=/opt/vault-kms/encryption_config.yaml``` within the ```kube-apiserver.yaml``` configuration file which is usually located in the folder ```/etc/kubernetes/manifests``` and add the extra volumes bindings for ```/opt/vault-kms```. 

An example is available with the directory ```scripts/k8s``` with commented sections.   
**Edit your own ```kube-apiserver.yaml``` file and not copy/paste the entire content of the example file.**

**NOTES: depending on the Kubernetes distribution, the kubelet might not include the ```/etc/kubernetes/manifests``` for ```staticPodPath```. 
Verifiy ```kubelet-config.yaml``` within ```/etc/kubernetes``` to ensure this parameter is present.**

Finally, restart the ```kube-apiserver``` to apply the configuration. Trousseau should start allow with it.

### RKE Specifics
When deploying using rke (not RKE2) and after successfuly deploying a working kubernetes using your ```cluster.yml``` with ```rke up```, modify the following sections of your ```cluster.yml```:

the ```kube-api``` section:
```YAML
  kube-api:
    image: ""
    extra_args:
      encryption-provider-config: /opt/vault-kms/encryption_config.yaml
    extra_binds: 
      - "/opt/vault-kms:/opt/vault-kms"
```

the ```kubelet``` section:
```YAML
  kubelet:
    image: ""
    extra_args: 
      pod-manifest-path: "/etc/kubernetes/manifests"
    extra_binds: 
      - "/opt/vault-kms:/opt/vault-kms"
```

Once everything in place, perform a ```rke up``` to reload the configuration.

### RKE2 Specifics
Building a Kubernetes RKE2 cluster is a different approach then with RKE fromn a configuration perpective as there is no more ```cluster.yml```configuration file.   

**Note: if you already have an existing RKE2 cluster deployed, the *etcd* is being encrypted at-rest by default with a key configured in the file ```/var/lib/rancher/rke2/server/cred/encryption-config.json```. Removing this file or reconfiguring with the below steps will render previous secrets unreadable!**

Here are the steps for a fresh deployment:  
* prepare the following directory structure:
```
├── etc
│   └── rancher
│       └── rke2
│           └── config.yaml
├── opt
│   └── vault-kms
│       ├── config.yaml
│       └── encryption_config.yaml
└── var
    └── lib
        └── rancher
            └── rke2
                └── server
                    ├── cred
                    │   ├── encryption-config.json
                    │   └── encryption_config.yaml
                    └── manifests
                        └── vault-kms-provider.yaml
```
* here are the content for each files:
    * ```/etc/rancher/rke2/config.yaml```: 
    ```
    # server: https://<address>:9345    #to edit/uncomment for second and third control plane node
    # token: <rke2_server_token>             #to edit/uncomment for second and third control plane node
    kube-apiserver-arg:
      - "--encryption-provider-config=/var/lib/rancher/rke2/server/cred/vault-kms-encryption-config.yaml" 
    kube-apiserver-extra-mount:
      - "/opt/vault-kms:/opt/vault-kms"
    ```
    * ```/opt/vault-kms/config.yaml```: 
    ```
    provider: vault
    vault:
      keynames:
      - demo-token-test
      address: https://<vault_address>:8200
      token: <vault_token>
    ```
    * ```/opt/vault-kms/encryption_config.yaml```
    ```
    kind: EncryptionConfiguration
    apiVersion: apiserver.config.k8s.io/v1
    resources:
      - resources:
          - secrets
        providers:
          - kms:
              name: vaultprovider
              endpoint: unix:///opt/vault-kms/vaultkms.socket
              cachesize: 1000
          - identity: {}
    ```
    * ```/var/lib/rancher/rke2/server/cred/encryption-config.json```:
    ```
    apiVersion: apiserver.config.k8s.io/v1
    kind: EncryptionConfiguration
    resources:
      - resources:
        - secrets
        providers:
        - identity: {}
    ```
    * ```/var/lib/rancher/rke2/server/cred/encryption_config.yaml```:
    ```
    kind: EncryptionConfiguration
    apiVersion: apiserver.config.k8s.io/v1
    resources:
      - resources:
          - secrets
        providers:
          - kms:
              name: vaultprovider
              endpoint: unix:///opt/vault-kms/vaultkms.socket
              cachesize: 1000
          - identity: {}    
    ```
    * ```/var/lib/rancher/rke2/manifests/vault-kms-provider.yaml```: see [DaemonSet file here](https://github.com/Trousseau-io/trousseau/blob/main/scripts/rke2/vault-kms-provider.yaml)
* on the first control plane/master/server node, run the followings:
```
curl -sfL https://get.rke2.io | sh -
systemctl enable --now rke2-server.service
```
* get the server node token from ```/var/lib/rancher/rke2/server/node-token``` and add it to the ```/etc/rancher/rke2/config.yaml``` for control plane/master/server node 2 and 3
* run on control plane/master/server node 2 and 3:
```
curl -sfL https://get.rke2.io | sh -
systemctl enable --now rke2-server.service
```
* carry on with adding worker/agent nodes as usual (and without any of the about configuration)

## Setup monitoring
Trousseau is coming with a Prometheus endpoint for monitoring with basic Grafana dashboard.  

An example of configuration for the Prometheus endpoint access is available within the folder ```scripts/templates/monitoring``` with the name ```prometheus.yaml```. 

An example of configuration for the Grafana dashboard configuration is available within the folder ```scripts/templates/monitoring``` with the name ```grafana-dashboard.yaml```. 
