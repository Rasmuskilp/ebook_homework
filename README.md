The following is to consilidate our understanding of pyodbc and Python.

objectives:

create a new DB IN SQL SERVER

INSERT a about 5 books in there using SQL SERVER

Connect this project to that DB

Have a function that retrieves all books and print them with the following formar

-> 1) title: XYZ - Author: XPTO - Date: 1/3/1343
-> 2) title: XYZ - Author: XPTO - Date: 1/3/1343
-> 3) title: XYZ - Author: XPTO - Date: 1/3/1343
(...)
have a function that searches for a book's title
Be able to Save one book # search for .commit() on pyodbc
Persistent in DB (using insert)
API Section:

Be able to add a postcode to a book
have a method that is called geo_code_api_call()
get the postcode of the book, from the objt
use the post code to generate a URL link to postcode.io
use requests package, to make a GET request with URL
capture the response of the GET Resquest in variable to use later
Use the capture response to get out the LAT and LONG
print it out to the user (the lat and long of the postcode)
EXTRA:

update the book record with long and lat
A book should have:

Title

Author

Date

Postcode

Lat

Long