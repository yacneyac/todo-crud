# todo-crud
The simple CRUD API for to-do list.
## Requirements
1. docker compose
2. poetry

## How to start
1. need to run docker `docker-compose -f ./compose-db.yml up -d`
2. build db ``
3. run server

## CRUD API
* See all available status
  curl -X GET http://localhost:5000/statuses
    response: 
[
    {
        "id": 1,
        "name": "new"
    },
    {
        "id": 2,
        "name": "done"
    },
    {
        "id": 3,
        "name": "in_work"
    }
]
* 
* Create a new todo
    curl -X POST http://localhost:5000/todos 
         -d '{"description": "Task 1"}' 
         -H 'Content-Type: application/json'

* Read all todos
    curl -X GET http://localhost:5000/todos 

* Update todo
    curl -X PUT http://localhost:5000/todos/1 
         -d '{"status": 2, "description": "Updated description"}' 
         -H 'Content-Type: application/json'
* Delete todo
    curl -X DELETE http://localhost:5000/todos/1

docker-compose -f ./compose-db.yml up -d