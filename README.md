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
**Get all available statuses**
```
 curl -X GET http://localhost:5000/statuses
 
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
 
```

**Create a new task**
```
    curl -X POST http://localhost:5000/todos 
         -H 'Content-Type: application/json'
         -d '{"description": "Need to buy a bottle of milk"}' 
         
   {
    "id": 1,
    "description": "Need to buy a bottle of milk",
    "status": 1,
    "is_deleted": 0,
    "created": "2023-01-06 15:05:49.714290",
    "deleted": null
   }      
```

**Read all tasks**
```
    curl -X GET http://localhost:5000/todos
    
    [
    {
        "id": 1,
        "description": "need to buy a car1!",
        "status": 1,
        "is_deleted": 0,
        "created": "2023-01-06 14:37:29.482360",
        "deleted": null
    },
    {
        "id": 2,
        "description": "need to buy a car1!",
        "status": 1,
        "is_deleted": 0,
        "created": "2023-01-06 14:37:57.078415",
        "deleted": null
    }
    ]
    
```

* Update todo
    curl -X PUT http://localhost:5000/todos/1 
         -d '{"status": 2, "description": "Updated description"}' 
         -H 'Content-Type: application/json'
* Delete todo
    curl -X DELETE http://localhost:5000/todos/1

docker-compose -f ./compose-db.yml up -d
