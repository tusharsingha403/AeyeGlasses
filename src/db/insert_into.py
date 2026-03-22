from connection import get_connection 

conn = get_connection()
c = conn.cursor()

c.execute("INSERT INTO State_Check VALUES ('search', 0);")
c.execute("INSERT INTO State_Check VALUES ('glow', 0);")

conn.commit()
conn.close()
