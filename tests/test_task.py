import models


def test_get_tasks_empty(client):
    response = client.get('/todos')
    assert response.json == [], response.status == 200


def test_add_a_new_task_success(client, test_app):
    response = client.post('/todos', json={'description': 'task1'})
    assert response.json['status'] == 1, response.status == 201

    with test_app.app_context():
        assert (
            models.Todo.query.filter_by(description='task1').one_or_none()
            is not None
        )
