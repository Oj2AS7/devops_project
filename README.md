# TaskBoard — Cloud-Native SaaS Project & Production DevOps Architecture

[![CI/CD Pipeline](https://github.com/Oj2AS7/devops_project/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Oj2AS7/devops_project/actions/workflows/ci-cd.yml)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/Frontend-React%20%2B%20Vite-61DAFB?logo=react&logoColor=black)](https://react.dev)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com)
[![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-326CE5?logo=kubernetes&logoColor=white)](https://kubernetes.io)
[![Helm](https://img.shields.io/badge/Package-Helm%20v3-0F1689?logo=helm&logoColor=white)](https://helm.sh)
[![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC?logo=terraform&logoColor=white)](https://www.terraform.io)
[![Trivy](https://img.shields.io/badge/Security-Trivy%20Scan-1B365D?logo=aquasecurity&logoColor=white)](https://trivy.dev)
[![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C?logo=prometheus&logoColor=white)](https://prometheus.io)

An enterprise-grade, end-to-end cloud-native SaaS task management application engineered with a complete modern DevOps lifecycle: from local containerized development and automated CI/CD security gating to AWS EKS infrastructure provisioning, Kubernetes orchestration, Helm packaging, and full-stack observability.

---

## Architecture Overview

```text
 Developer Laptop
        │
        ▼
   Git / GitHub (main branch)
        │
        ▼
 GitHub Actions CI/CD Pipeline
  ├── 1. Automated Testing (Pytest + Test DB)
  ├── 2. Frontend Production Build (Vite)
  ├── 3. Multi-Stage Docker Container Builds
  ├── 4. Trivy Security Scanning (FAIL on HIGH/CRITICAL)
  └── 5. Push Immutable SHA Tags to GitHub Container Registry (GHCR)
              │
              ▼
    Terraform (AWS Cloud IaC)
  ├── AWS VPC (Multi-AZ Public + Private Subnets + NAT Gateway)
  └── AWS EKS Cluster (Managed Node Groups)
              │
              ▼
       Helm Orchestration
  ├── Ingress Controller (Nginx routes '/' to Frontend, '/api' to Backend)
  ├── Frontend Deployment (2 Replicas, unprivileged Nginx)
  ├── Backend Deployment (2 Replicas, non-root FastAPI, HPA Autoscaling)
  └── PostgreSQL Database (Stateful storage with PVC)
              │
              ▼
   Full-Stack Observability
  ├── FastAPI Prometheus Instrumentator (/metrics)
  ├── CoreOS Prometheus Operator (ServiceMonitor)
  └── Grafana Metrics Dashboards
```

---

## Technology Stack

| Layer | Technology | Details |
|---|---|---|
| **Frontend** | React 18, Vite | SaaS workspace dashboard, responsive layout, task board |
| **Backend** | Python 3.12, FastAPI | RESTful APIs, Pydantic validation, Prometheus instrumentation |
| **Database** | PostgreSQL 16, SQLAlchemy 2.0 | Relational storage, declarative ORM, Alembic migrations |
| **Testing** | Pytest, FastAPI TestClient | 14 automated unit & integration tests with SQLite isolation |
| **Containerization** | Docker, Docker Compose | Multi-stage unprivileged builds, non-root execution (UID 10001, nginx) |
| **CI/CD** | GitHub Actions | Automated test, build, scan, push to GHCR, and Helm release |
| **Security (DevSecOps)** | Aqua Security Trivy | Container image vulnerability scanner (blocks HIGH/CRITICAL CVEs) |
| **Infrastructure as Code** | Terraform | Reusable AWS VPC and AWS EKS cluster modules |
| **Orchestration** | Kubernetes & Helm 3 | Declarative package management, multi-environment values |
| **Traffic Routing** | Kubernetes Ingress | Nginx Ingress Controller host & path-based routing |
| **Autoscaling** | Kubernetes HPA | Horizontal Pod Autoscaler based on dynamic CPU utilization |
| **Observability** | Prometheus & Grafana | Application `/metrics` scraping via ServiceMonitor & visualization |

---

## Repository Structure

```text
devops_project/
├── .github/
│   └── workflows/
│       └── ci-cd.yml             # GitHub Actions CI/CD & DevSecOps pipeline
├── backend/
│   ├── alembic/                  # Database migration scripts
│   ├── app/
│   │   ├── config.py             # App environment configuration
│   │   ├── db.py                 # SQLAlchemy engine and session factory
│   │   ├── main.py               # FastAPI router, endpoints & lifespan
│   │   ├── models.py             # Database ORM models
│   │   └── schemas.py            # Pydantic request/response schemas
│   ├── tests/
│   │   ├── conftest.py           # Pytest test DB fixtures & client setup
│   │   └── test_api.py           # 14 comprehensive API endpoint tests
│   ├── Dockerfile                # Non-root container specification
│   ├── pytest.ini                # Pytest configuration
│   └── requirements.txt          # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── main.jsx              # React root & application dashboard
│   │   └── styles.css            # Responsive SaaS styling
│   ├── Dockerfile                # Multi-stage unprivileged Nginx build
│   ├── nginx.conf                # Frontend reverse proxy configuration
│   ├── package.json              # Frontend scripts & dependencies
│   └── vite.config.js            # Vite build configuration
├── terraform/
│   ├── main.tf                   # AWS VPC + EKS cluster resource definitions
│   ├── variables.tf              # Configurable infrastructure variables
│   ├── outputs.tf                # Cluster endpoint and VPC outputs
│   ├── versions.tf               # Terraform and AWS provider versions
│   └── terraform.tfvars.example  # Example variables configuration
├── helm/
│   └── taskboard/
│       ├── Chart.yaml            # Helm chart metadata
│       ├── values.yaml           # Base deployment values
│       ├── values-dev.yaml       # Development override values (Ingress enabled)
│       ├── values-prod.yaml      # Production override values
│       └── templates/            # K8s manifests (Deployments, Services, HPA, Ingress)
├── k8s/
│   └── namespace.yaml            # Isolated namespace definition
├── monitoring/
│   └── prometheus-values.yaml    # Prometheus and Grafana Helm values
├── scripts/
│   └── load-test.sh              # Automated HTTP load generator for HPA
├── troubleshooting/
│   ├── broken-image.yaml         # Kubernetes diagnostic scenario: ImagePullBackOff
│   └── broken-service.yaml       # Kubernetes diagnostic scenario: Label selector mismatch
└── docker-compose.yml            # Complete local multi-container stack
```

---

## Application & API Specification

FastAPI exposes RESTful endpoints with interactive Swagger UI documentation at `/docs`:

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | API status, application metadata, and documentation URL |
| `GET` | `/health` | Lightweight liveness probe for container runtime orchestrators |
| `GET` | `/ready` | Readiness probe confirming active database connectivity |
| `GET` | `/metrics` | Prometheus exposition endpoint for request rate, latency, and status codes |
| `GET` | `/api/tasks` | Retrieve all tasks ordered by recent creation |
| `GET` | `/api/tasks/{id}` | Retrieve details for a specific task |
| `POST` | `/api/tasks` | Create a new task (validates status and priority) |
| `PUT` | `/api/tasks/{id}` | Update existing task attributes or advance task workflow |
| `DELETE` | `/api/tasks/{id}` | Delete a task by ID |
| `GET` | `/api/tasks/stats` | Aggregated metrics for total, todo, in-progress, and done counts |

### Health, Readiness & Metrics Design Rationale
- **Liveness (`/health`)**: Allows Kubernetes to restart an unresponsive container process without verifying external state.
- **Readiness (`/ready`)**: Verifies that the database pool is healthy and accepting queries. If PostgreSQL is unreachable, the pod is temporarily removed from service traffic routing rather than killed.
- **Metrics (`/metrics`)**: Formatted for Prometheus scraping with latency histograms and response counts.

---

## Local Development & Quickstart

### Method 1: Docker Compose (Full Stack)

Requirements: Docker Engine 20+ and Docker Compose v2.

```bash
# Build and start frontend, backend, and PostgreSQL
docker compose up --build

# Access services:
# Frontend UI: http://localhost:3000
# Backend API: http://localhost:8000/docs
# Metrics:     http://localhost:8000/metrics

# Stop services and retain database data
docker compose down

# Stop and purge database volumes
docker compose down -v
```

### Method 2: Running Services Locally

#### 1. Backend Setup
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run database migrations
export DATABASE_URL="postgresql+psycopg://taskboard:taskboard@localhost:5432/taskboard"
alembic upgrade head

# Start development server
uvicorn app.main:app --reload --port 8000
```

#### 2. Running Automated Tests
The test suite utilizes an isolated SQLite test database with dependency overrides to ensure zero side effects on production data:

```bash
cd backend
pytest -v
```

#### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

---

## Container Architecture & Security

### Backend Container (`backend/Dockerfile`)
- Base: `python:3.12-slim` (minimal attack surface)
- Non-root user: Executes as UID `10001` (`appuser`)
- Migrations: Executes Alembic schema migration before starting Uvicorn

### Frontend Container (`frontend/Dockerfile`)
- Stage 1 (`build`): Node 22 Alpine builds static production bundles with Vite
- Stage 2 (`runtime`): Nginx 1.27 Alpine serves static files and reverse-proxies `/api`
- Non-root permissions: Configured unprivileged `USER nginx`

### Vulnerability Gating (Trivy)
Every image build in CI is automatically scanned by Aqua Security Trivy. Any `HIGH` or `CRITICAL` severity CVE triggers an automatic pipeline failure before images can be published.

---

## CI/CD Pipeline (GitHub Actions)

The pipeline is defined in [`.github/workflows/ci-cd.yml`](file:///Users/ojaskotiyal/devops_project/.github/workflows/ci-cd.yml) and executes on every push and pull request to `main`:

```text
 ┌──────────────┐      ┌─────────────────────────────┐      ┌─────────────┐
 │   1. TEST    │ ───► │  2. BUILD, SCAN & PUBLISH   │ ───► │  3. DEPLOY  │
 ├──────────────┤      ├─────────────────────────────┤      ├─────────────┤
 │ Pytest tests │      │ Docker multi-stage build    │      │ Helm deploy │
 │ Vite build   │      │ Trivy scan (HIGH/CRITICAL)  │      │ to cluster  │
 │              │      │ Push to GHCR with Git SHA   │      │ (on secrets)│
 └──────────────┘      └─────────────────────────────┘      └─────────────┘
```

- **Immutable Artifacts**: Images are tagged with the exact Git commit SHA (`${{ github.sha }}`) to guarantee end-to-end traceability from deployment back to code commit.
- **Fail-Fast Policy**: If any test fails or container vulnerability is detected, pipeline stops immediately.

---

## Infrastructure as Code (Terraform)

The [`terraform/`](file:///Users/ojaskotiyal/devops_project/terraform) directory provisions production-ready AWS cloud infrastructure:

- **VPC Module**: Custom CIDR (`10.20.0.0/16`) spanning 2 Availability Zones (`ap-south-1a`, `ap-south-1b`) with isolated public and private subnets and managed NAT Gateways.
- **EKS Module**: Kubernetes 1.31 cluster with private node placement, public endpoint access, and managed node groups (`t3.medium`, auto-scaling 2–4 nodes).

### Provisioning Instructions

```bash
cd terraform

# 1. Initialize provider plugins and modules
terraform init

# 2. Preview infrastructure changes
terraform plan

# 3. Apply changes to provision AWS resources
terraform apply

# 4. Configure local kubectl to point to your new EKS cluster
aws eks --region ap-south-1 update-kubeconfig --name taskboard-eks

# 5. Teardown infrastructure when no longer needed
terraform destroy
```

---

## Kubernetes & Helm Deployment

The application is packaged as a configurable Helm 3 chart in [`helm/taskboard/`](file:///Users/ojaskotiyal/devops_project/helm/taskboard):

### 1. Create Namespace
```bash
kubectl apply -f k8s/namespace.yaml
```

### 2. Deploy with Helm
```bash
# Deploy base release with 2 replicas and HPA enabled
helm upgrade --install taskboard ./helm/taskboard \
  --namespace taskboard \
  --create-namespace

# Deploy with development ingress enabled
helm upgrade --install taskboard ./helm/taskboard \
  --namespace taskboard \
  -f ./helm/taskboard/values-dev.yaml
```

### 3. Verify Workloads
```bash
kubectl get pods -n taskboard -o wide
kubectl get svc -n taskboard
kubectl get hpa -n taskboard
kubectl get ingress -n taskboard
```

---

## Observability & Metrics

### Prometheus & ServiceMonitor
- The backend exports standard Prometheus metrics at `/metrics`.
- The Helm chart includes a `ServiceMonitor` manifest (`monitoring.coreos.com/v1`) that auto-registers with Prometheus Operator.

### Deploying the Monitoring Stack
```bash
# Add prometheus-community helm repo
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Install kube-prometheus-stack
helm install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  -f monitoring/prometheus-values.yaml
```

---

## Load Testing & Troubleshooting Scenarios

### Automated Load Testing
Generate 500 requests against the ingress endpoint to observe Horizontal Pod Autoscaler (HPA) metrics and pod scaling:

```bash
chmod +x scripts/load-test.sh
./scripts/load-test.sh
```

Monitor scaling in real time:
```bash
kubectl get hpa -n taskboard -w
```

### Diagnostic Exercises

#### Scenario 1: Image Pull Backoff
Simulate an invalid image tag deployment:
```bash
kubectl apply -f troubleshooting/broken-image.yaml
kubectl describe pod -l app=broken-image
# Root cause: non-existent container tag triggers ImagePullBackOff
```

#### Scenario 2: Service Selector Mismatch
Simulate a broken service label selector:
```bash
kubectl apply -f troubleshooting/broken-service.yaml
kubectl get endpoints broken-backend-service
# Root cause: Service selector does not match pod labels; endpoints are empty (<none>)
```

---

## Author & Maintainer

- **Developer / DevOps Engineer**: Ojas Kotiyal ([@Oj2AS7](https://github.com/Oj2AS7))
- **Repository**: [https://github.com/Oj2AS7/devops_project](https://github.com/Oj2AS7/devops_project)
