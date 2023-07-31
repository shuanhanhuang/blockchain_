import sqlite3

# Connect to the database
conn = sqlite3.connect('search.db')

# Create a cursor object
c = conn.cursor()

# Create the table
c.execute('''CREATE TABLE search (
    date DATE,
    time TIME,
    employee_id INT,
    transactionHash_str TEXT);''')

# Save the changes
conn.commit()

# Close the connection
conn.close()
