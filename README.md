Solution 1:
In this solution, APIs are implemented by using methods and classes without any DB.
There are two files in the project.
1. API.py : All API are implemented in this class
2. TestAPI.py: This file consists of unit tests for the API class.


Follow the below documentation for further details on each API
APIs

addAnAuthor

Arguments
name: str value
phone_number: Integer number
birth_date: Specify in the DD-MM-YYYY format
death_date: Specify in the DD-MM-YYYY format

Documentation
Add a new author to the existing author list.

Example:
addAnAuthor(name, phone_number, birth_data, death_date)

searchBookbyAuthorname

Arguments
author_name: str value

Documentation
Search the book by author name in the list.

Example: 
searchBookbyAuthorname(author_name)


getAllAuthorName

Documentation
Get all author names from the author list.

Example: 
getAllAuthorName()



getListOfCategories

Documentation
Get the list of categories from the book list.

Example: 
getListOfCategories()


getMostSoldBookInCategory

Arguments
category: str value

Documentation
Get the most sold book from the given category.

Example: 
getMostSoldBookInCategory(category):



searchBookbyBookname

Arguments
book_name: str value

Documentation
Search the book in the book list by the given book name.

Example: 
searchBookbyBookname(book_name)


addBookToCatalog

Arguments
title:  str value
author_id:  str value
publisher:  str value
category_id: str value
price:  str value
sold_count: str value

Documentation
Add the new given book to the existing book list.

Example: 
addBookToCatalog(title, author_id, publisher, category_id, price, sold_count)
