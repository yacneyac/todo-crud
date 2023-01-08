import models


def test_get_tasks_empty(client):
    response = client.get('/tasks')
    assert response.json == [], response.status == 200


def test_get_tasks_by_page(client):
    for name in ['task1', 'task2', 'task3']:
        response = client.post('/tasks', json={'description': name})
        assert response.json['status'] == 1, response.status == 201

    response = client.get('/tasks')
    assert len(response.json) == 3, response.status == 200

    response = client.get('/tasks?page=1&per_page=2')
    assert len(response.json) == 2, response.status == 200

    response = client.get('/tasks?page=2&per_page=2')
    assert len(response.json) == 1, response.status == 200


def test_get_missed_task_by_id(client):
    response = client.get('/tasks/1')
    assert response.json == {'message': 'Task with id=1 is missed'}, response.status == 200


def test_add_a_new_task_success(client, app):
    response = client.post('/tasks', json={'description': 'task1'})
    assert response.json['status'] == 1, response.status == 201

    # task is created in the db
    with app.app_context():
        assert (
            models.Task.query.filter_by(description='task1').one_or_none()
            is not None
        )


def test_add_a_new_task_missed_description(client):
    response = client.post('/tasks', json={})
    assert response.status == '415 UNSUPPORTED MEDIA TYPE'


def test_task_change_status_success(client, app):
    response = client.post('/tasks', json={'description': 'task2'})
    assert response.json['status'] == 1, response.status == 201

    response = client.put(f'/tasks/{response.json["id"]}', json={'status': 3})
    assert response.json['status'] == 3, response.status == 200

    # status is changed in the db
    with app.app_context():
        assert (
            models.Task.query.filter_by(status=3, description='task2').one_or_none()
            is not None
        )


def test_task_change_missed_status(client, app):
    response = client.post('/tasks', json={'description': 'task2'})
    assert response.json['status'] == 1, response.status == 201

    response = client.put(f'/tasks/{response.json["id"]}', json={'status': 5})
    assert response.status == '415 UNSUPPORTED MEDIA TYPE'

    # task is not changed in the db
    with app.app_context():
        assert (
            models.Task.query.filter_by(status=1, description='task2').one_or_none()
            is not None
        )
