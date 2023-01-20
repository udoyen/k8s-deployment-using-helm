# Deploying a simple Nginx frontend and Flask backend using Helm

## Prerequisites

- Ubuntu 20.04
- Minikube
- Helm
- Kubectl

## Steps

1. Start Minikube
2. Run:

   - minikube addons enable ingress
   - minikube addons enable ingress-dns

3. Deploy using helm command with locally stored nginx and flask images
4. Steps to access Ingress

   - Append 127.0.0.1 hello-world.info to your /etc/hosts file on MacOS (NOTE: Do NOT use the Minikube IP)

   - Run minikube tunnel ( Keep the window open. After you entered the password there will be no more messages, and the cursor just blinks)

   - Hit the hello-world.info ( or whatever host you configured in the yaml file) in a browser and it should work

### Important links

[StackOverflow](https://stackoverflow.com/a/73735009/2782188)