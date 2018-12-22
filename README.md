```
C:\Users\plankton\PycharmProjects\new_django\venv\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2018.2\helpers\pydev\pydevconsole.py" 56637 56638
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\plankton\\PycharmProjects\\new_django', 'C:/Users/plankton/PycharmProjects/new_django'])
PyDev console: starting.
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32

import os
import sqlite3
db_file = os.path.join(os.getcwd(), 'newprog', 'db.sqlite3')
db_file
'C:\\Users\\plankton\\PycharmProjects\\new_django\\newprog\\db.sqlite3'
conn = sqlite3.connect(db_file)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
<sqlite3.Cursor object at 0x036AB4E0>
tables = cur.fetchall()
tables
[('django_migrations',), ('sqlite_sequence',), ('auth_group',), ('auth_group_permissions',), ('auth_user_groups',), ('auth_user_user_permissions',), ('django_admin_log',), ('django_content_type',), ('auth_permission',), ('auth_user',), ('django_session',), ('foo_foo',)]
AttributeError: 'tuple' object has no attribute 'name'
for table in tables:
    print(table)
    
('django_migrations',)
('sqlite_sequence',)
('auth_group',)
('auth_group_permissions',)
('auth_user_groups',)
('auth_user_user_permissions',)
('django_admin_log',)
('django_content_type',)
('auth_permission',)
('auth_user',)
('django_session',)
('foo_foo',)
```
# python-examples
