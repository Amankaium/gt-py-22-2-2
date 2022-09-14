import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

contacts_dict = {
    "Papa": "353452345",
    "Sister": "243234"
}

sql_command = "INSERT INTO Mynames VALUES "

for key, value in contacts_dict.items():
    sql_command += f"('{key}', '{value}'), "

sql_command = sql_command[:-2] + ";"
# Execute a query
# cur.execute(f"INSERT INTO Mynames VALUES ('test2', '3243246245'), ('Test3', '22');")
print(sql_command)
cur.execute(sql_command)
conn.commit()
cur.close()
conn.close()

# Retrieve query results
# records = cur.fetchall()
# print(records)