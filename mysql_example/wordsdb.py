import csv
import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


def get_credentials():
    # Load environment variables
    load_dotenv()
    db_config = {
        'host': os.getenv('MYSQL_HOST'), # url
        'user': os.getenv('MYSQL_USER'),
        'password': os.getenv('MYSQL_PASSWORD'),
        'database': os.getenv('MYSQL_DATABASE') # optional
    }
    return db_config


def connect_to_database(db_config):
    try:
        # Establish connection to MySQL database
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Failed to connect to database: {e}")
        return None


def show_databases(connection):
    cursor = connection.cursor() # Create a cursor object using the connection
    try:
        cursor.execute("SHOW DATABASES")  # Correct SQL command to list databases
        databases = cursor.fetchall()  # Fetch all results
        return databases  # This will return a list of tuples, where each tuple contains a database name
    except mysql.connector.Error as e:
        print(f"Error fetching databases: {e}")
        return None


def drop_and_create_table(connection):
    try:
        cursor = connection.cursor()  # Create a cursor object using the connection

        # SQL query to drop the table if it exists
        drop_query = "DROP TABLE IF EXISTS vocab_table"
        cursor.execute(drop_query)  # Execute the drop table query

        # SQL query to create a new table
        create_query = "CREATE TABLE vocab_table (word VARCHAR(255), definition VARCHAR(255))"
        cursor.execute(create_query)  # Execute the create table query

        print("Table 'vocab_table' dropped (if existed) and created successfully.")

    except mysql.connector.Error as e:
        print(f"Error when trying to drop/create table: {e}")


def insert_data_into_table(connection, word_list):
    try:
        cursor = connection.cursor()  # Create a cursor object using the connection

        # SQL query to insert data into the table 
        # escaping values with %s protects from SQL injections 
        # because this allows the values to be applied separately from the SQL string itself
        insert_query = "INSERT INTO vocab_table (word, definition) VALUES (%s, %s)"
        
        # Executing all insertions in a batch
        cursor.executemany(insert_query, word_list)

        connection.commit()  # Commit the transaction to save changes
        print("Data successfully inserted into 'vocab_table'.")
        
    except mysql.connector.Error as e:
        print(f"Error when trying to insert data into table: {e}")
        connection.rollback()  # Rollback in case of error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        connection.rollback()  # Rollback in case of any other exceptions


def fetch_all_data(connection):
    try:
        cursor = connection.cursor()  # Create a cursor object using the connection

        # SQL query to fetch data
        select_query = "SELECT * FROM vocab_table"
        
        # Executing the query
        cursor.execute(select_query)

        # Fetching all rows from the executed query
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        print("Data successfully fetched from 'vocab_table'.")
        
    except mysql.connector.Error as e:
        print(f"Error when trying to fetch data from the table: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def fetch_data_by_word(connection, search_word):
    try:
        cursor = connection.cursor()  # Create a cursor object using the connection

        # SQL query to fetch data based on a specific word
        select_query = "SELECT * FROM vocab_table WHERE word = %s"

        # Execute the query with a parameter to prevent SQL injection
        cursor.execute(select_query, (search_word,))

        # Fetching all rows that match the query
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No entries found for the word:", search_word)

    except mysql.connector.Error as e:
        print(f"Error when trying to fetch data from the table: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def truncate_table(connection):
    try:
        cursor = connection.cursor()  # Create a cursor object using the connection

        # SQL query to truncate the table
        truncate_query = "TRUNCATE TABLE vocab_table"

        # Execute the query
        cursor.execute(truncate_query)
        connection.commit()  # Commit the transaction to apply changes

        print("Table 'vocab_table' has been truncated successfully.")

    except mysql.connector.Error as e:
        print(f"Error when trying to truncate the table: {e}")
        connection.rollback()  # Rollback in case of error
    finally:
        cursor.close()  # Always close the cursor to free up connection resources


def update_word_or_definition(connection, current_word, new_word=None, new_definition=None):
    try:
        cursor = connection.cursor()  # Create a cursor object using the connection

        # Determine which part to update based on provided arguments
        if new_word and new_definition:
            update_query = "UPDATE vocab_table SET word = %s, definition = %s WHERE word = %s"
            values = (new_word, new_definition, current_word)
        elif new_word:
            update_query = "UPDATE vocab_table SET word = %s WHERE word = %s"
            values = (new_word, current_word)
        elif new_definition:
            update_query = "UPDATE vocab_table SET definition = %s WHERE word = %s"
            values = (new_definition, current_word)
        else:
            print("No update performed. Please provide a new word or definition.")
            return

        # Execute the update query
        cursor.execute(update_query, values)
        connection.commit()  # Commit the transaction to save changes

        print(f"Record updated successfully: '{current_word}' updated.")

    except mysql.connector.Error as e:
        print(f"Error when trying to update the table: {e}")
        connection.rollback()  # Rollback in case of error
    finally:
        cursor.close()  # Always close the cursor to free up connection resources



def read_file(filename):
    try:
        # Open the file using 'with' to ensure it gets closed after reading
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            wd_list = list(reader)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    vocabulary_list = [[entry[0], entry[1].rstrip()] for entry in wd_list if len(entry) >= 2]
    # print(vocabulary_list[0])
    # print(type(vocabulary_list))
    # print(type(vocabulary_list[0]))
    return vocabulary_list

def main():
    db_config = get_credentials()
    filename = "Vocabulary_list.csv"
    connection = connect_to_database(db_config)
    if connection:
        vocabulary_list = read_file(filename)
        # print(vocabulary_list)
        # print(show_databases(connection))
        drop_and_create_table(connection)
        insert_data_into_table(connection, vocabulary_list)
        fetch_all_data(connection)

        fetch_data_by_word(connection, "boisterous")

        
        connection.close()

if __name__ == '__main__':
    main()