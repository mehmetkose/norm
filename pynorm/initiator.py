
# NoSql Focused ORM for python 3.5 projects
# https://github.com/mehmetkose/pynorm

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmet@linux.com

import rethinkdb as r

async def create_tables(database, connection):
    try:
        await r.db_create(database.db).run(connection)
        print('Database created: %s' % (database.db))
    except:
        pass

    for table in database.tables:
        try:
            await r.db(database.db).table_create(
                table.name, durability='hard').run(connection)
            print('Table created: %s' % (table.name))
        except:
            pass

    for table in database.tables:
        try:
            await r.db(database.db).table_create(
                table.name, durability='hard').run(connection)
            print('Table created: %s' % (table.name))
        except:
            pass

    for table in database.tables:
        for row in table.rows:
            if 'index' in row.specs:
                try:
                    await r.db(database.db).table(table.name).index_create(row.name).run(connection)
                except:
                    pass
