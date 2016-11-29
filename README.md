# pynorm

NoSql Focused ORM for python 3.5 projects


# Installation

**pip install pypynorm**


# Usage

```python
import tornado.web
import tornado.escape
...

from pynorm import Pynorm, Database, Table, Row
...

# Build Table
UserTable = Table(name='user')
UserTable.rows.append(Row('user_name'))
UserTable.rows.append(Row('user_mail', specs=['index']))
# Buld Database
ProjectDatabase = Database(db='test', host='127.0.0.1', port=28015)
ProjectDatabase.tables.append(UserTable)

class BaseHandler(tornado.web.RequestHandler):

    async def prepare(self):
        self.db = await Pynorm.init(database=ProjectDatabase, create_structure=True)

class DemoHandler(BaseHandler):

    async def get(self):
        for user in (await self.db.list("user")):
            self.write(user['user_name'])

    ...
```