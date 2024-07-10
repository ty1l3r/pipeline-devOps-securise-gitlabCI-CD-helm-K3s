# Pipeline DevOps pour Microservices avec GitLab CI/CD et Kubernetes

![Diagramme d'Architecture](https://miro.medium.com/max/1400/1*wiLoL7tiINfAdbgpMJc-uA.png)

## Technologies Clés
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-FCA121?style=for-the-badge&logo=gitlab&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=json-web-tokens&logoColor=white)
![REST API](https://img.shields.io/badge/REST_API-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

## Aperçu du Projet
Ce projet démontre un pipeline CI/CD complet pour déployer des microservices sur Kubernetes en utilisant GitLab CI/CD et Helm. Il met en valeur les pratiques DevOps modernes, notamment :

- **Conteneurisation** avec Docker
- **Orchestration** avec Kubernetes
- **Gestion des packages** avec Helm
- **Automatisation CI/CD** avec GitLab
- **Déploiements multi-environnements** (développement, QA, préproduction, production)
- **Architecture microservices** avec modèle de Passerelle API

L'application se compose de trois microservices :
- Service Passerelle : Passerelle API pour le routage et l'authentification
- Service Utilisateur : Gère l'authentification et les profils utilisateurs
- Service Commande : Gère les commandes

## Architecture

![Architecture Microservices](https://microservices.io/i/basic-microservices.png)

L'application suit une architecture de microservices :
- **Service Passerelle** : Agit comme une passerelle API pour gérer les requêtes, l'authentification et le routage
- **Service Utilisateur** : Gère l'authentification et les profils utilisateurs
- **Service Commande** : Gère les commandes

## Environnements de Déploiement

| Environnement | Objectif | Mise à l'échelle | Accès |
|------------|---------|---------|--------|
| Développement | Tests de développement | 1 réplique | Interne |
| QA | Assurance qualité | 2 répliques | Interne |
| Préproduction | Validation avant production | 3 répliques | Interne |
| Production | Environnement en direct | 3+ répliques | Public (avec approbation manuelle) |

## Stack Technologique
- **Backend** : Python FastAPI
- **Conteneurisation** : Docker 
- **Orchestration** : Kubernetes
- **Gestion des Packages** : Helm
- **CI/CD** : GitLab CI/CD
- **Authentification** : JWT
- **Communication entre Services** : API REST

## Pipeline CI/CD

Le pipeline GitLab CI/CD comprend les étapes suivantes :
1. **Test** : Exécuter les tests unitaires pour tous les services
2. **Construction** : Construire les images Docker pour tous les microservices
3. **Exécution** : Vérifier que les images Docker peuvent fonctionner correctement
4. **Déploiement** : Déployer dans les environnements appropriés selon la branche/commit

![Pipeline CI/CD](https://about.gitlab.com/images/ci/ci-cd-test-deploy-illustration_2x.png)

## Démarrage Rapide

### Prérequis
- Docker et Docker Compose
- Cluster Kubernetes (ou Minikube pour le développement local)
- kubectl configuré pour votre cluster
- Helm 3

### Configuration du Développement Local
```bash
# Cloner le dépôt
git clone https://gitlab.com/jh.hunt3r/gitlab-devop-exam.git
cd gitlab-devop-exam

# Exécuter avec docker-compose pour le développement local
docker-compose up -d
```

### Déploiement sur Kubernetes
```bash
# Environnement de développement
helm install app-dev --namespace dev ./helm/charts/dev/ -f ./helm/charts/dev/values.yaml

# Environnement QA
helm install app-qa --namespace qa ./helm/charts/qa/ -f ./helm/charts/qa/values.yaml

# Environnement de préproduction
helm install app-staging --namespace staging ./helm/charts/staging/ -f ./helm/charts/staging/values.yaml

# Environnement de production (nécessite des approbations appropriées)
helm install app-prod --namespace prod ./helm/charts/prod/ -f ./helm/charts/prod/values.yaml
```

## Documentation API
La documentation API est disponible via Swagger UI lors de l'exécution des services :
- Service Passerelle : http://localhost:31100/docs
- Service Utilisateur : http://localhost:8001/docs
- Service Commande : http://localhost:8002/docs

## Surveillance et Observabilité
Les services incluent des endpoints de vérification de santé et sont configurés pour la surveillance avec Prometheus et Grafana en production.

## Fonctionnalités de Sécurité
- Authentification basée sur JWT
- Gestion des secrets avec Kubernetes secrets
- Contrôle d'accès basé sur les rôles
- Configurations spécifiques à l'environnement

## Structure du Projet

```
.
├── .gitlab-ci.yml              # Configuration du pipeline GitLab CI/CD
├── docker-compose.yml          # Configuration pour développement local
├── README.md                   # Documentation du projet
├── services/                   # Tous les microservices
│   ├── gateway/                # Service Passerelle
│   │   ├── Dockerfile          # Instructions de build Docker
│   │   ├── requirements.txt    # Dépendances Python
│   │   └── src/                # Code source
│   ├── user/                   # Service Utilisateur
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── src/
│   └── order/                  # Service Commande
│       ├── Dockerfile
│       ├── requirements.txt
│       └── src/
├── helm/                       # Charts Helm pour déploiement Kubernetes
│   ├── charts/                 # Charts par environnement
│   │   ├── dev/
│   │   ├── qa/
│   │   ├── staging/
│   │   └── prod/
│   └── templates/              # Templates Helm réutilisables
└── k8s/                        # Configurations Kubernetes brutes
    ├── namespaces/             # Définitions des namespaces
    ├── secrets/                # Templates de secrets
    └── configmaps/             # ConfigMaps pour configuration
```