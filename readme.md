**<font size=10>Flask Batch Job API</font>**
<br>
This is a Flask-based API that provides endpoints for filtering and retrieving batch job records from a SQLite database. The API utilizes SQLAlchemy for database connection and query execution.

**<font size=5>Setup Instructions</font>** <br>
To run the code, please follow these steps: <br>

1. Install the required dependencies after creating a new virtual environment by running the following command:

       pip install flask sqlalchemy 
2. Ensure you have a SQLite database file named database.db in the same directory as the code file. If you don't have the file, create an empty SQLite database using the following command:

       touch database.db
    **Note:**
    I have made a python file called `data_cleaning`,
    which fills the missing data of some columns using common methods of data wrangling.
    If you wish to use the complete data you can run the file using the following command:
    
        python data_cleaning.py
    The execution of this file outputs a new file called `filled_file.csv`
3. You can upload the data from the csv file to the database by adding the datasource in the IDE (PyCharm),
    choose SQLite from the menu, and upload the `database.db` file and apply, after that you can right-click on the database and choose the option `Import data from file` and choose either csv file.
4. Open a terminal or command prompt and navigate to the directory containing the code file.

    Run the code using the following command:

       flask --app app run --debug 
**<font size=5>API Endpoints</font>** <br>
The API provides the following endpoints:

**<font size=3>Redirect to Main Page</font>** 

+ **URL:** /
+ **HTTP Method:** GET
+ **Description:** Redirects the user to the main page for batch jobs. 
+ **Response:** A redirect response to the URL `http://localhost:5000/batch_jobs` with status code 302.

**<font size=3>Filter Batch Jobs</font>**

+ **URL:** /batch_jobs
+ **HTTP Method:** GET
+ **Description:** Retrieves batch job records from the database based on the provided query parameters.
+ **Query Parameters:**
    + `min_nodes` (optional): Batch jobs that used at least min_nodes.
    + `max_nodes` (optional): Batch jobs that used at most max_nodes.
    + `submitted_before` (optional): Retrieve batch jobs submitted before a specified date/time.
    + `submitted_after` (optional): Retrieve batch jobs submitted after a specified date/time.
+ **Response:** A JSON response containing the filtered batch job records. The response follows the JSON API specification.

**<font size=5> Testing the API</font>** <br>
To test the API, run the following command from the terminal:

        coverage run -m unittest test_app.py
**Note:** Used unittest.mock to generate mock data to test the API. <br>
**<font size=5>Conclusion</font>** <br>
With the provided instructions, you should be able to set up and run the Flask Batch Job API successfully.