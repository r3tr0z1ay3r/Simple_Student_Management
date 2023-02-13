import sqlite3

con = sqlite3.Connection('Student1.db')
cur = con.cursor()
exam = 'Half_Yearly'
name = "Merry"
standard = 12
result = '''select * from {} where student_name='{}' and standard = '{}' '''.format(exam,name,standard)
marks = cur.execute(result).fetchall()[0]
print(marks[3])
con.commit()
con.close()
#print(english)