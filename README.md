# items

## 1 Install 

### 1.1 Clone repo

Fork repo and clone your:
```#!bash
$ git clone git@github.com:{you}/items.git items
```

or download zip and unzip:
```#!bash
$ mkdir items 
$ cd items
$ unzip items-master.zip
```

### 1.2 virtualenv
```#!bash
$ virtualenv venv
$ source venv/bin/activate
```

### 1.3 pip install -e
```#!bash
(venv)$ cd items-master
(venv)$ pip install -e src/
```

### 1.4 Environment
```#!bash
(venv)$ export FLASK_APP=items.app
(venv)$ export PYTHONPATH=/path/to/items-master/src

# DB url, for example if nessesary:
(venv)$ export SQLALCHEMY_DATABASE_URI=sqlite:///path/to/items-master/project.db
```

### 1.5 Init DB

run custom app command for initialize DB structure and state:
```#!bash
(venv)$ flask initdb
```

### 1.6 Run

Run application:
```#!bash
(venv)$ flask run -h {host} -p {port}

# for example below:
(venv)$ flask run -h localhost -p 8080
```

## Usage

Add expired item (start_time must be great than {start_time + days}):
```#!bash
$ curl -H "Content-Type: application/json" -X POST -d '{"start_time": "2017-03-10 12:30:00.662599","days": 3,"end_percent": 50,"start_price": 1450}' http://localhost:8080/api/v1/add
```

Get list (you will have different result depending by added items):
```#!bash
$ curl http://localhost:8080/api/v1/items
{
  "items": [
    {
      "current_price": 9000.0,
      "id": 1,
      "is_price_min": false
    }
  ],
  "status": "ok"
}
```

Get item by id:
```#!bash
$ curl http://localhost:8080/api/v1/items/1
{
  "current_price": 9000.0,
  "id": 1,
  "is_price_min": false
}
```

### Negative results

Got empty list:
```#!bash
$ curl http://localhost:8080/api/v1/items
{
  "items": [],
  "status": "ok"
}
```

Got expired or not existed item:
```#!bash
$ curl http://localhost:8080/api/v1/items/1
{"status": "not found"}

$ curl http://localhost:8080/api/v1/items/qwerty
{"status": "not found"}
```

Got HTTP 404 status:
```#!bash
$ curl -I http://localhost:8080/api/v1/items/qwerty
HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 23
Server: Werkzeug/0.12.1 Python/2.7.12
Date: Mon, 10 Mar 2017 18:16:47 GMT

```