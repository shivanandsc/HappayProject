import datetime
books_data = []
author_data = []
class API:

    def addAnAuthor(name, phone_number, birth_data, death_date):
        day, month, year = birth_data.split('-')
        Author_ID = len(author_data) + 1
        try:
            datetime.datetime(int(year), int(month), int(day))
            add_author = {'Author_ID': Author_ID,
                          'Name': name,
                          'Phone_Number': phone_number,
                          'Birth_Data': birth_data,
                          'Death_Date': death_date}

            author_data.append(add_author)
            return 'SUCCESS'
        except:
            return 'Invalid date of birth'

    def searchBookbyAuthorname(author_name):
        Booksby_Author = []
        for book in books_data:
            if author_name==book['Author_id']:
                Booksby_Author.append(book['Title'])
        try:
            len(Booksby_Author) != 0
        except:
            return 'No such author found'

        return Booksby_Author

    def getAllAuthorName(self):
        ListOfAuthorname = []
        for author in author_data:
            ListOfAuthorname.append(author['Name'])
        ListOfAuthorname = list(dict.fromkeys(ListOfAuthorname))

        return ListOfAuthorname

    def getListOfCategories(self):
        ListOfCategories = []
        for book in books_data:
            if book['Category_id'] != 'null':
                ListOfCategories.append(book['Category_id'])
        return ListOfCategories

    def getMostSoldBookInCategory(category):
        Soldcount = 0
        mostsold_book = 0
        for book in books_data:
            if book['Category_id'] == category and int(book['Sold_Count']) > int(Soldcount):
                Soldcount = book['Sold_Count']
                mostsold_book = book

        return mostsold_book

    def searchBookbyBookname(book_name):
        Bookby_searchlist = []
        for book in books_data:
            if book_name in book['Title']:
                Bookby_searchlist.append(book)

        if len(Bookby_searchlist) != 0:
            return Bookby_searchlist[0]['Title']
        else:
            return 'No such book found'

    def resetData(self):
        books_data.clear()
        author_data.clear()

    def addBookToCatalog(title, author_id, publisher, category_id, price, sold_count):
        Book_Id = len(books_data) + 1
        addBook = {'Book_Id': Book_Id,
                   'Title': title,
                   'Author_id': author_id,
                   'Publisher': publisher,
                   'Category_id': category_id,
                   'Price': price,
                   'Sold_Count': sold_count}
        for book in books_data:
            if book['Title']==addBook['Title']:
                return "book already present"
        books_data.append(addBook)
        return 'SUCCESS'
