# MySQL Example Project

This repository contains a Python script to interact with a MySQL database. The script demonstrates basic operations such as connecting to the database, creating tables, inserting data, fetching data, updating data, and more.

## Project Structure

```plaintext
.
├── README.md
├── Vocabulary_list.csv
└── wordsdb.py
```

### Files

- **README.md**: This file, providing an overview and instructions for the project.
- **Vocabulary_list.csv**: A CSV file containing a list of vocabulary words and their definitions.
- **wordsdb.py**: The main Python script that interacts with the MySQL database.

## Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package installer)
- `mysql-connector-python` package
- `python-dotenv` package

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/asavoullis/medium_content/mysql_example.git
   cd mysql_example
   ```

2. Install the required Python packages:

   ```sh
   pip install mysql-connector-python python-dotenv

   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your MySQL credentials:

   ```env
   MYSQL_HOST=your_mysql_host
   MYSQL_USER=your_mysql_username
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_DATABASE=your_database_name
   ```

4. Ensure your MySQL server is running and accessible using the credentials provided in the `.env` file.

## Running the Script

The script performs the following operations:

1. Loads MySQL credentials from environment variables.
2. Connects to the MySQL database.
3. Reads vocabulary words from the `Vocabulary_list.csv` file.
4. Creates a table in the database to store the vocabulary words.
5. Inserts the vocabulary words into the table.
6. Fetches and displays all the data from the table.
7. Fetches and displays data for a specific word ("boisterous").

To run the script, execute the following command:

```sh
python wordsdb.py
```

## Functions

### get_credentials()

Loads database credentials from environment variables.

### connect_to_database(db_config)

Establishes a connection to the MySQL database.

### show_databases(connection)

Fetches and displays all databases in the MySQL server.

### drop_and_create_table(connection)

Drops the existing table (if any) and creates a new one.

### insert_data_into_table(connection, word_list)

Inserts a list of vocabulary words and definitions into the table.

### fetch_all_data(connection)

Fetches and displays all records from the table.

### fetch_data_by_word(connection, search_word)

Fetches and displays records for a specific word.

### truncate_table(connection)

Truncates the table, deleting all its data.

### update_word_or_definition(connection, current_word, new_word=None, new_definition=None)

Updates the word or definition of an existing record.

### read_file(filename)

Reads vocabulary data from a CSV file.

## Example Output

Upon running the script, you should see output indicating successful connection to the database, table creation, data insertion, and fetched data from the table.

## Improvements

This is just an introductory example and can be further improved by:

- Adding more robust error handling.
- Implementing more complex queries and operations.
- Enhancing the data model.
- Adding unit tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues, fork the repository, and make pull requests.

## Contact

For any questions or suggestions, please contact [Charilaos Savoullis](mailto:your-email@example.com).
