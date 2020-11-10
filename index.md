## TROUSSEAU

Trousseau secures and provides access Secrets for Kubernetes and more, either on-premises, in the cloud or hybrid.

## Why Trousseau

Kubernetes users are always facing the very same question; how will we handle our Secrets? From a pure Kubernetes
perspectives, the by-design solution using etcd w/o encryption is not enough. 
With Trousseau, your applications running within Kubernetes cluster(s) or oustide can access their secrets in a safe
way with unique features. 

Trousseau is a completly open source and design to be a solution in a landscape where there isn't many options to chose from. 

## What Trousseau will provide

* A easy deployment using an operator
* A sidecar option to proxy authentication towards external services
* An API based secure password management for CRUD activities
* A zero trust option to generate new secrets and configure remote services 

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

[Link to another page](./_posts/001-architecture.html)
