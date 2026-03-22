from src.db.connection import get_connection 

def check_glow():
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM State_Check WHERE id='glow' ")
    row = c.fetchone()

    status = row[1]
    conn.commit()
    conn.close()
    print("glow" , status)
    return (status)


def check_search():
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM State_Check WHERE id='search'; ")
    row = c.fetchone()

    status = row[1]
    conn.commit()
    conn.close()
    print("search" , status)
    return (status)


def change_glow(temp):
    conn = get_connection()
    c = conn.cursor()
      
    query = f"UPDATE State_Check SET State = {temp} WHERE id='glow';"
    print (query)
    c.execute(query)

    conn.commit()
    conn.close()



def change_search(temp):
    conn = get_connection()
    c = conn.cursor()
       
    query = f"UPDATE State_Check SET State = {temp} WHERE id='search';"
    print (query)
    c.execute(query)

    conn.commit()
    conn.close()

#change_search(0)
#change_glow(0)
#print(check_glow())
#print(check_search())

#END WITH TUSHAR