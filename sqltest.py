import sqlite3
connection = sqlite3.connect("student.db")
cursor = connection.cursor()
table_info = """
create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR(5), SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

cursor.execute('''INSERT INTO STUDENT VALUES('Krish','Data_science','A',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Manu','Data_Engineering','B',50)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Das','Data_science','A',70)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Hari','Devops','A',10)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Kathir','Data_science','A',90)''')


print("The inserted records are ")

data = cursor.execute("""SELECT * FROM STUDENT""")

for row in data:
    print(row)

connection.commit()
connection.close()