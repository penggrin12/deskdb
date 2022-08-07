# deskdb
> Simple (and stupid) python3 db module

Basic setup:
```py
from deskdb import DataStore

db = deskdb.DataStore("db") # DataStore
```

Write & Read:
```py
db_item = db.get_item("bob") # DataStoreItem

db_item.write("cash", 500)
print(db_item.read("cash")) # 500
```

If value that ur trying to read is integer (example: `50`)  
It will be returned as `int`
