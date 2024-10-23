import mysql.connector
import pandas as pd

# Load the cleaned CSV data
cleaned_data = pd.read_csv('cleaned_merge_data_10.csv')

# Establish a connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",  # or "127.0.0.1"
    user="root",       # Your MySQL username
    password="2610",  # Your MySQL password
    database="Red_bus_project"  # The database you created in MySQL Workbench
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

# SQL query to insert data into the bus_routes table
sql = """
    INSERT INTO bus_routes (
        route_name, route_link, bus_name, bus_type, 
        departing_time, duration, reaching_time, 
        star_rating, price, seats_available
    ) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Loop through the cleaned data and insert each row into the database
for index, row in cleaned_data.iterrows():
    values = (
        row['Route Name'],
        row['Route Link'],
        row['Bus Name'],
        row['Bus Type'],
        row['Departure Time'],
        row['Duration'],
        row['Arrival Time'],
        row['Star Rating'],
        row['Price'],
        row['Seat Availability']
    )
    
    # Execute the SQL query
    mycursor.execute(sql, values)

# Commit the transaction
mydb.commit()

# Print success message
print(f"{mycursor.rowcount} rows inserted into the bus_routes table.")

# Close the connection
mycursor.close()
mydb.close()