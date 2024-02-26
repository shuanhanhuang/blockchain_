import sqlite3

# Connect to the database
conn = sqlite3.connect('serch.db')

# Create a cursor object
c = conn.cursor()

# Create the table
c.execute('''CREATE TABLE upload_record (
    transaction_hash TEXT,
    current_date DATE DEFAULT CURRENT_DATE
);''')

# Save the changes
conn.commit()

# Close the connection
conn.close()