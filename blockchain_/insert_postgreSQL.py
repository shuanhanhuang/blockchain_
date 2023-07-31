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

# Define the data to be inserted into the "recort" table
date = "2023-05-03"
time = "01:01:01"
employee_id = 2543
research_data = "老爸測試dadtests and development tools. In addition, one needs to possess strong logical thinking abilities, problem-solving skills, and innovative spirit. Lastly, continuous learning and keeping up with the latest technologies and trends, actively participating in community and industry events, and exchanging experiences with other professionals are crucial to becoming a true blockchain expertt, one needs to have a comprehensive understanding of various aspects and skills. Firstly, it is necessary to have an in-depth個專業的區塊鏈專家需要具備多方面的知識和技能。首先，他需要對區塊鏈的原理、技術和應用場景，以及各種類型的區塊鍊和不同的共識算法有深刻的理解。其次，它 需要掌握智能合約的編寫和開發技巧，以及相關的編程語言和開發工具，此外，還需要具備較強的邏輯思維能力、解決問題的能力和創新精神。最後，需要 不斷學習和跟進最新的技術和趨勢，積極參與社區和行業活動，並與其他專家合作To become understanding of the principles, technology, and application scenarios of blockchain, as well as the different types and consensus algorithms of blockchain. Secondly, it is essential to master the skills of writing and developing smart contracts, as well as related programming language"

# Execute the INSERT statement
cur.execute(
    "INSERT INTO recort (date, time, employee_id, research_data) VALUES (%s, %s, %s, %s)",
    (date, time, employee_id, research_data)
)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
