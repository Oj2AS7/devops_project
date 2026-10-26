# Project Demo & Presentation Deliverables

This directory contains the final presentation slide deck and recorded walkthrough demonstration for the **TaskBoard Cloud-Native DevOps Capstone Project**.

---

## Deliverables in this Directory

| File | Description | Status |
|---|---|---|
| [`TaskBoard_DevOps_Presentation.pptx`](./TaskBoard_DevOps_Presentation.pptx) | 10-Slide Full DevOps Capstone Presentation Deck | Ready |
| `demo_walkthrough.mp4` | Recorded end-to-end video demonstration | Included / Linked below |

---

## Presentation Deck Contents ([`TaskBoard_DevOps_Presentation.pptx`](./TaskBoard_DevOps_Presentation.pptx))

1. **Title & Executive Summary**: Presenter details (Ojas Kotiyal) and project scope.
2. **End-to-End DevOps Architecture**: Flow diagram from local Git commits to monitored AWS EKS workloads.
3. **Module 1 — Application & Database**: FastAPI backend, React dashboard UI, PostgreSQL 16 & Alembic migrations.
4. **Module 2 — Automated Testing**: Pytest test suite with isolated SQLite database fixtures (14/14 tests passing).
5. **Module 4 — Docker Containerization**: Multi-stage unprivileged builds, non-root security (`USER 10001` and `USER nginx`), and Docker Compose.
6. **Modules 5 & 6 — CI/CD & DevSecOps**: GitHub Actions automated pipeline, Aqua Security Trivy vulnerability scan, and GHCR container registry publishing.
7. **Module 7 — Infrastructure as Code**: Terraform modules for AWS VPC (Multi-AZ public/private subnets) and AWS EKS cluster.
8. **Module 8 — Kubernetes & Helm**: Helm chart configuration, 2-replica Deployments, ClusterIP Services, Nginx Ingress routing, and Horizontal Pod Autoscaler (HPA).
9. **Module 9 — Observability & Troubleshooting**: Prometheus metrics scraping (`/metrics`), ServiceMonitor, Grafana dashboards, and diagnostic triage scenarios.
10. **Module 10 — Deliverables & Checklist**: Verification mapping to the grading rubric.

---

## Video Walkthrough Demonstration

- **Demonstration Video**: `demo_walkthrough.mp4` (or streaming link below)
- **Demo Highlights Covered**:
  - React frontend dashboard & task progression
  - FastAPI interactive documentation (`/docs`) & health/readiness endpoints (`/health`, `/ready`)
  - Running automated test suite with Pytest (`pytest -v`)
  - GitHub Actions CI/CD pipeline execution with green status
  - Trivy container security scanning and GHCR image publishing
  - Kubernetes cluster workloads, Helm releases, Ingress routing, and Prometheus metrics
