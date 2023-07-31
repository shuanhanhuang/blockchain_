import psycopg2

# Connect to the remote PostgreSQL server
conn = psycopg2.connect(
    host="192.168.1.238",
    port=5432,
    dbname="mydata",
    user="postgres",
    password="1126"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute the CREATE statement
cur.execute(
    "CREATE TABLE recort (date DATE, time TIME, employee_id INT, research_data VARCHAR)"
)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
