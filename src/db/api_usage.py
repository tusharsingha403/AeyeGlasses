from connection import get_connection 


def check_usage():
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM Vision_API_usage")
    row = c.fetchone()

    usage = row[1]
    #print (usage)
    conn.commit()
    conn.close()
    return (usage)


def increase_usage():
    conn = get_connection()
    c = conn.cursor()
    
    usage = check_usage()

    query = f"UPDATE Vision_API_usage SET Unit_used = {usage + 1} ;"
    print (query)
    c.execute(query)

    conn.commit()
    conn.close()


def clear_usage():
    conn = get_connection()
    c = conn.cursor()
    

    query = f"UPDATE Vision_API_usage SET Unit_used = {0} ;"
    print (query)
    c.execute(query)

    conn.commit()
    conn.close()


clear_usage()
#END WITH TUSHAR