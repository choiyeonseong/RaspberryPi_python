import sqlite3

# db 연결
dbconn = sqlite3.connect('./testdb.db')
cursor = dbconn.cursor()

try:
    cursor.execute("CREATE TABLE if not exists user(id INTEGER, name text, phone text, sex text)")
    cursor.execute("INSERT INTO user(id, name, phone, sex) VALUES (1, 'Hong', '010-1234-1234', 'male')")
    cursor.execute("INSERT INTO user(id, phone, name, sex) VALUES (2, '011-2345-6666', 'Park', 'female')")
    cursor.executemany("INSERT INTO user(id, name, phone, sex) values (?, ?, ?, ?)",\
        [(3, 'Kim', '010-333-3333','female'),(4,'Choi','010-4565-3456','male'),(5,'Lee','010-7777-8888','female')])
    dbconn.commit() # commit하고 실행해야 저장 됨
    
except KeyboardInterrupt:
    dbconn.close()