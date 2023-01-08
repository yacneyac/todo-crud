# todo-crud
The simple CRUD API for to-do list.
## Stack
python3.9, Flask-RESTful, Flask-SQLAlchem, PostgresDB

## Install
Need to install docker compose [Install the Compose standalone](https://docs.docker.com/compose/install/other/)

Clone the repository:

    $ git clone git@github.com:yacneyac/todo-crud.git
    $ cd todo-crud

Create a virtualenv and activate it:

    $ python3.9 -m venv todo-venv
    $ . todo-venv/bin/activate

Install requirements:

    $ pip3.9 install -r ./requirements.txt

## How to start
1. need to start a PostgresDB in docker container `$ docker-compose -f ./compose-db.yml up -d`
2. run tests `$ pytest`
3. build Database `$ python3.9 make_db.py`
4. run server `$ python3.9 main.py`

## DB Schema
Table **Task**

| name        | type                    |    
|-------------|-------------------------|
| id          | Integer **PK**          |
| description | String                  |
| created     | DateTime                |
| status      | Integer **FK(Status.id)** |

Table **Status**

| name        | type           |    
|-------------|----------------|
| id          | Integer **PK** |
| name        | String         |


## CRUD API
**Get all available statuses**
```
    curl -X GET http://localhost:5000/statuses
 
    < HTTP/1.1 200 OK
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
    
   < HTTP/1.1 201 CREATED
   {
        "id": 1,
        "description": "Need to buy a bottle of milk",
        "status": 1,
        "created": "2023-01-06 15:05:49.714290"
   }      
```

**Read tasks**

To prevent users from requesting too many results on a single page 
the result will be generated with 20 items per page.
```
    curl -X GET http://localhost:5000/tasks
    
    < HTTP/1.1 200 OK
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
        },
        {
            "id": 3,
            "description": "Need to buy a butter",
            "status": 1,
            "created": "2023-01-06 15:08:23.224000"
        },
        ...
    ]
```

Need to specify arguments `page` and `per_page` in the URL
```
    curl -X GET "http://localhost:5000/tasks?page=1&per_page=2"
    
    < HTTP/1.1 200 OK
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
    
    < HTTP/1.1 200 OK
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
   
   < HTTP/1.1 200 OK
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
    
    < HTTP/1.1 204 NO CONTENT
```

## Invalid requests

**Missed task**
```
    curl http://localhost:5000/tasks/33
    
    < 404 NOT FOUND
    {
        "message": "Task with id=33 is missed"
    }
```

**Invalid type of status field**
```
    curl -X PUT http://localhost:5000/tasks/1 
    -d '{"status":"done"}' 
    -H 'Content-Type: application/json'
    
    < 400 BAD REQUEST
    {
        "message": {
            "status": "invalid literal for int() with base 10: 'done'"
        }
    }
```
**Status ID is missed in the DB**
```
    curl -X PUT http://localhost:5000/tasks/1 
    -d '{"status":23}' 
    -H 'Content-Type: application/json'
    
    < 415 UNSUPPORTED MEDIA TYPE
    {
        "message": "Cannot update the task"
    }
```
**All parameters are missed**
```
    curl -X PUT http://localhost:5000/tasks/1 
    -d '{}' 
    -H 'Content-Type: application/json'
    
    < 415 UNSUPPORTED MEDIA TYPE
    {
        "message": "Nothing to update! The values are missed or the name of the fields are invalid"
    }
```

