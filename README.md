# deskdb
> Simple (and stupid) python3 db module

Basic setup:
```py
from deskdb import DataStore

users_db = DataStore("users_db") # deskdb.DataStore
```

Write & Read:
```py
db_item = users_db.get_item("bob") # deskdb.DataStoreItem

db_item.write("cash", 500)
db_item.read("cash") # int(500)
db_item.increment("level", 1)
db_item.decrement("xp", 100)
```

If value that ur trying to read is integer (example: `50`)  
It will be returned as `int`
