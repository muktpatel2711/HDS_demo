import pyodbc

# Set up the connection details
server = '10.2.16.32'
database = 'MIS_QA'                   # Replace with your database name
username = 'misuserqa'                   # Replace with your username
password = ''                   # Replace with your password
driver = '{ODBC Driver 17 for SQL Server}'   # Replace with your SQL driver


try:
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    )
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")

# Create a cursor to execute queries
cursor = conn.cursor()

# Example query
cursor.execute("SELECT * FROM your_table")
rows = cursor.fetchall()

# Print the result
for row in rows:
    print(row)

# Close the connection
conn.close()
