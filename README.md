# todo-crud
The simple CRUD API for to-do list.
## Stack
python3.9, Flask-RESTful, Flask-SQLAlchem, PostgresDB

## Requirements
1. docker compose [Install the Compose standalone](https://docs.docker.com/compose/install/other/)
2. poetry [Install poetry](https://python-poetry.org/docs/#installation)
3. python3.9

## How to start
1. need to start a PostgresDB in docker container `docker-compose -f ./compose-db.yml up -d`
2. build db `poetry run python3.9 make_db.py`
3. run server `poetry run python3.9 main.py`

## DB Schema
Table **Task**

| name        | type                 |    
|-------------|----------------------|
| id          | Integer (PK)             |
| description | String               |
| created     | DateTime             |
| status      | Integer **ForeignKey(Status.id)** |

Table **Status**

| name        | type     |    
|-------------|----------|
| id          | Integer (PK) |
| name        | String   |


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
    curl -X POST http://localhost:5000/tasks 
         -H 'Content-Type: application/json'
         -d '{"description": "Need to buy a bottle of milk"}' 
         
   {
    "id": 1,
    "description": "Need to buy a bottle of milk",
    "status": 1,
    "created": "2023-01-06 15:05:49.714290"
   }      
```

**Read all tasks**
```
    curl -X GET http://localhost:5000/tasks
    
    [
    {
        "id": 1,
        "description": "Need to buy a bottle of milk",
        "status": 1,
        "created": "2023-01-06 15:05:49.714290"
    },
    {
        "id": 2,
        "description": "Need to buy a bread",
        "status": 1,
        "created": "2023-01-06 15:05:55.234221"
    }
    ]
    
```

**Read task by ID**
```
    curl -X GET http://localhost:5000/tasks/1
    
    {
        "id": 1,
        "description": "Need to buy a bottle of milk",
        "status": 1,
        "created": "2023-01-06 15:05:49.714290"
    }
    
```

**Update task by ID**
```
    curl -X PUT http://localhost:5000/tasks/1 
         -d '{"status": 3, "description": "Need to buy a bottle of milk and butter"}' 
         -H 'Content-Type: application/json'
   
   {
    "id": 1,
    "description": "Need to buy a bottle of milk and butter",
    "status": 3,
    "created": "2023-01-06 15:05:49.714290"
   }
```

**Delete a task by ID**
```
    curl -X DELETE http://localhost:5000/tasks/1
```

## Invalid requests

**Missed task**
```
    curl http://localhost:5000/tasks/33
    
    {
    "message": "Task with id=33 is missed"
    }
```

**Missed field**
```
```


