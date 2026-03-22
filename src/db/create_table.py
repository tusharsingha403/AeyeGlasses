#Run once to create Table if not exists.

from connection import get_connection 

conn = get_connection()
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS Vision_API_usage(id INTEGER, Unit_used NUMBER )")

conn.commit()


c.execute("CREATE TABLE IF NOT EXISTS State_Check(id VARCHAR(30), State NUMBER )")

conn.commit()
conn.close()

#END WITH TUSHAR