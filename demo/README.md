# Project Demo & Presentation Deliverables

This directory contains the final presentation slide deck, custom architecture diagrams, and the recorded walkthrough demonstration video for the **TaskBoard Cloud-Native DevOps Capstone Project**.

---

## Deliverables in this Directory

| File | Description | Status |
|---|---|---|
| [`TaskBoard_DevOps_Presentation.pptx`](./TaskBoard_DevOps_Presentation.pptx) | Interactive 10-Slide Full DevOps Capstone Presentation Deck with high-res architecture diagrams | Ready & Verified |
| [`demo_walkthrough.mp4`](./demo_walkthrough.mp4) | Recorded end-to-end command walkthrough demonstration video (Full HD 1080p @ 30fps) | Included |
| [`assets/`](./assets/) | High-resolution slide diagram images & video previews | Ready |

---

## Presentation Deck Contents ([`TaskBoard_DevOps_Presentation.pptx`](./TaskBoard_DevOps_Presentation.pptx))

1. **Title & Executive Summary**: Presenter details (Ojas Kotiyal, DevOps Engineer), core tech stack badges, and system overview.
2. **End-to-End DevOps Architecture**: Flow diagram tracking local Git commits through CI/CD, container security, Terraform provisioning, Kubernetes orchestration, and Prometheus telemetry.
3. **Module 1 — Application & Database**: Decoupled React 18 SPA, asynchronous FastAPI backend, PostgreSQL 16 persistence, and Alembic migrations (`0001_create_tasks.py`).
4. **Module 2 — Automated Testing**: Pytest test suite with isolated SQLite database fixtures, dependency overrides, and 14/14 automated tests passing in 0.08s.
5. **Module 4 — Enterprise Containers**: Multi-stage unprivileged Docker builds, non-root security (`UID 10001` and `USER nginx`), and full Docker Compose stack.
6. **Modules 5 & 6 — CI/CD & DevSecOps**: GitHub Actions automated pipeline (`test` -> `build-scan-push` -> `deploy`), Aqua Security Trivy vulnerability gate (0 HIGH/CRIT CVEs), and GHCR immutable Git SHA tagging.
7. **Module 7 — Infrastructure as Code**: Terraform modules for AWS VPC (Multi-AZ public/private subnets in `ap-south-1`) and Managed EKS 1.31 cluster with 2–4 `t3.medium` instances.
8. **Module 8 — Kubernetes & Helm**: Helm 3 chart with multi-environment overrides (`values-dev.yaml`, `values-prod.yaml`), 2-replica Deployments, Nginx Ingress routing, and Horizontal Pod Autoscaler (HPA).
9. **Module 9 — Observability & Troubleshooting**: FastAPI `/metrics` exposition, CoreOS ServiceMonitor auto-scraping, Grafana dashboards, automated load testing, and diagnostic triage scenarios (ImagePullBackOff & Service Selector Mismatch).
10. **Module 10 — Deliverables & Checklist**: Complete 100/100 points scorecard verification mapped to the Capstone grading rubric.

---

## Video Walkthrough Demonstration (`demo_walkthrough.mp4`)

- **Format**: MP4 (H.264 / AAC compatible), 1920x1080 Full HD, 30 fps
- **Duration**: ~41 seconds of focused, real-time command execution
- **Commands Executed in Video**:
  1. `git status && git log --oneline -n 3` — Clean working tree and conventional commit history
  2. `cd backend && python3 -m pytest -v` — 14/14 Pytest test cases passing with zero side effects
  3. `cd ../frontend && npm run build` — Production Vite asset compilation
  4. `cd .. && docker compose config --services` — Verification of postgres, backend, and frontend containers
  5. `cd terraform && terraform fmt -check && terraform validate` — Validation of AWS VPC & EKS HCL configurations
  6. `cd .. && helm lint ./helm/taskboard` — Helm 3 packaging validation (0 failed)
  7. `kubectl get pods,svc,hpa,ingress -n taskboard` — Live Kubernetes cluster workloads, ingress routing, and HPA targets
  8. `curl -s /health && curl -s /ready && curl -s /api/tasks/stats` — Verification of liveness, readiness, and metrics endpoints
  9. `./scripts/load-test.sh` — Automated 500-request load test validating HPA auto-scaling behavior
  10. `echo "=== DEVOPS FINAL CAPSTONE VERIFICATION COMPLETED (100/100 PTS) ==="` — Final scorecard confirmation
