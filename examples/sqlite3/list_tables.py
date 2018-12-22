#!/bin/env python3
import os
import sqlite3

# The sqlite3 data file is here: 
# 'C:\\Users\\plankton\\PycharmProjects\\new_django\\newprog\\db.sqlite3'
db_file = os.path.join(os.getcwd(), 'newprog', 'db.sqlite3')
conn = sqlite3.connect(db_file)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
for table in tables:
    print(table)

'''
output will be:    
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
'''
