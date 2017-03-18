# items

## Usage

add expired item (start_time must be great than {start_time + days}):
```#!bash

curl -H "Content-Type: application/json" -X POST -d '{"start_time": "2017-03-10 12:30:00.662599","days": 3,"end_percent": 50,"start_price": 1450}' http://localhost:8080/api/v1/add
```
