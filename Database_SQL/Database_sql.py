import mysql.connector
import pandas as pd

# Load the cleaned CSV data
cleaned_data = pd.read_csv('cleaned_merge_data_10.csv')

# Establish a connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",  # or "127.0.0.1"
    user="root",       # Your MySQL username
    password="2610",   # Your MySQL password
    database="Red_bus_project"  # The database you created in MySQL Workbench
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

# SQL query to insert data into the bus_routes table
sql = """
    INSERT INTO bus_routes (
        route_name, route_link, bus_name, bus_type, 
        departing_time, duration, reaching_time, 
        star_rating, price, seat_availability, state
    ) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Loop through the cleaned data and insert each row into the database
for index, row in cleaned_data.iterrows():
    values = (
        row['Route Name'],          # Ensure this matches the renamed column
        row['Route Link'],          # Ensure this matches the renamed column
        row['Bus Name'],            # Ensure this matches the renamed column
        row['Bus Type'],            # Ensure this matches the renamed column
        row['Departure Time'],      # Ensure this matches the renamed column
        row['Duration'],            # Ensure this matches the renamed column
        row['Arrival Time'],        # Ensure this matches the renamed column
        row['Star Rating'],         # Ensure this matches the renamed column
        row['Price'],               # Ensure this matches the renamed column
        row['Seat Availability'],   # Ensure this matches the renamed column
        row['state']                # Ensure this matches the renamed column
    )
    
    try:
        # Execute the SQL query
        mycursor.execute(sql, values)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Commit the transaction
mydb.commit()

# Print success message
print(f"{mycursor.rowcount} rows inserted into the bus_routes table.")

# Close the connection
mycursor.close()
mydb.close()