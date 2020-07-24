import cx_Oracle
import getpass

sqlId = raw_input('Enter sql_id: ')
databaseName = raw_input('Enter database: ')

if sqlId=="":
   sqlId = "01f146t8a4bdg"

if databaseName=="":
   databaseName = "xxxxxxxx"

userName = "xxxxxxx"

if databaseName=="xxxxxxxxxx":
   dsnStr = cx_Oracle.makedsn("mx1-scan", "1521", service_name="xxxxxxxxxxxxx")
else:
   dsnStr=""

con = cx_Oracle.connect(user='ODITMP', password='xxxxxxxxx', dsn=dsnStr)
cur = con.cursor()
sql = """SELECT dbms_sqltune.report_sql_monitor(sql_id => '""" + sqlId + """', type=> 'ACTIVE') FROM sys.dual"""
cur.execute(sql)

file = open("sql_mon.htm","w")
result =  cur.fetchall()
resultPart = result[0][0].read()
file.write(str(resultPart)) 
file.close()

cur.close()
con.close()
