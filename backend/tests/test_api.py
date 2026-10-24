def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}

def test_ready(client):
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "READY"}

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "TaskBoard API"
    assert "version" in response.json()

def test_create_task(client):
    payload = {
        "title": "Configure EKS Cluster",
        "description": "Set up AWS VPC and worker nodes with Terraform",
        "priority": "HIGH",
        "assignee": "DevOps Engineer",
        "status": "TODO"
    }
    response = client.post("/api/tasks", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["priority"] == payload["priority"]
    assert data["assignee"] == payload["assignee"]
    assert data["status"] == "TODO"
    assert "id" in data
    assert "created_at" in data

def test_create_task_validation_missing_title(client):
    response = client.post("/api/tasks", json={"description": "Missing title"})
    assert response.status_code == 422

def test_list_tasks(client):
    client.post("/api/tasks", json={"title": "Task 1", "priority": "LOW"})
    client.post("/api/tasks", json={"title": "Task 2", "priority": "MEDIUM"})
    response = client.get("/api/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert isinstance(tasks, list)
    assert len(tasks) >= 2

def test_get_task_by_id(client):
    create_res = client.post("/api/tasks", json={"title": "Specific Task", "priority": "HIGH"})
    task_id = create_res.json()["id"]

    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == "Specific Task"

def test_get_task_not_found(client):
    response = client.get("/api/tasks/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

def test_update_task(client):
    create_res = client.post("/api/tasks", json={"title": "Initial Title", "status": "TODO"})
    task_id = create_res.json()["id"]

    update_payload = {
        "title": "Updated Title",
        "status": "IN_PROGRESS",
        "priority": "HIGH"
    }
    response = client.put(f"/api/tasks/{task_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["status"] == "IN_PROGRESS"
    assert data["priority"] == "HIGH"

def test_update_task_not_found(client):
    response = client.put("/api/tasks/99999", json={"title": "Non-existent"})
    assert response.status_code == 404

def test_delete_task(client):
    create_res = client.post("/api/tasks", json={"title": "To be deleted"})
    task_id = create_res.json()["id"]

    delete_res = client.delete(f"/api/tasks/{task_id}")
    assert delete_res.status_code == 204

    get_res = client.get(f"/api/tasks/{task_id}")
    assert get_res.status_code == 404

def test_delete_task_not_found(client):
    response = client.delete("/api/tasks/99999")
    assert response.status_code == 404

def test_task_stats(client):
    client.post("/api/tasks", json={"title": "Task A", "status": "TODO"})
    client.post("/api/tasks", json={"title": "Task B", "status": "IN_PROGRESS"})
    client.post("/api/tasks", json={"title": "Task C", "status": "DONE"})

    response = client.get("/api/tasks/stats")
    assert response.status_code == 200
    stats = response.json()
    assert "total" in stats
    assert "todo" in stats
    assert "inProgress" in stats
    assert "done" in stats
    assert stats["total"] >= 3
    assert stats["todo"] >= 1
    assert stats["inProgress"] >= 1
    assert stats["done"] >= 1

def test_metrics_endpoint(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "http_request" in response.text or "http_requests" in response.text or "process_cpu_seconds" in response.text
