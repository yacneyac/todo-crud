
def test_get_all_statuses(client):
    response = client.get('/statuses')
    # [{'id': 1, 'name': 'new'}, {'id': 2, 'name': 'done'}, {'id': 3, 'name': 'in_work'}]
    assert len(response.json) == 3, response.status == 200
