
import unittest
import API as APIClass


class TestApi(unittest.TestCase):
    def setUp(self):
        super(TestApi, self).setUp()
        API = APIClass.API
        API.resetData(self)

    def test_getAllAuthorName(self):
        API = APIClass.API
        API.addAnAuthor('AAA', 'g12345', '4-2-1976', 'null')
        API.addAnAuthor('BBB', 'g12345', '4-2-1976', 'null')
        result = API.getAllAuthorName(self)
        self.assertEqual(len(result), 2)

    def test_addAnAuthor1(self):
        API = APIClass.API
        result = API.addAnAuthor('JK Rowling', 'g12345', '25-2-1968', 'null')
        self.assertEqual(result, 'SUCCESS')

    def test_addAnAuthor2(self):
        API = APIClass.API
        result = API.addAnAuthor('JK Rowling', 'g12345', '41-2-1976', 'null')
        self.assertEqual(result, 'Invalid date of birth')


    def test_searchBookbyAuthorname(self):
        API = APIClass.API
        API.addBookToCatalog('Book1', 'JK Rowling', 'Sample code book', 'john', '1000', '111')

        book = API.searchBookbyAuthorname('JK Rowling')
        self.assertEqual(book,['Book1'])


    def test_getListOfCategories(self):
        API = APIClass.API
        result = API.getListOfCategories()
        self.assertEqual(result, 'aa')

    def test_addBookToCatalog(self):
        API = APIClass.API
        result = API.addBookToCatalog('Book2','Author1', 'Sample code book', 'john', '1000', '111')
        self.assertEqual(result, 'SUCCESS')

    def test_getListOfCategories(self):
        API = APIClass.API
        API.addBookToCatalog('Book1', 'Author1', 'Sample code book', 'john', '1000', '111')
        result = API.getListOfCategories(self)
        self.assertEqual(result, ['john'])

    def test_getMostSoldBookInCategory(self):
        API = APIClass.API
        API.addBookToCatalog('Book1', 'Author1', 'Sample code book', 'Health', '1000', '111')
        API.addBookToCatalog('Book2', 'Author2', 'Sample code book', 'Health', '5000', '222')
        API.addBookToCatalog('Book3','Author3', 'Sample code book', 'Health', '100', '333')
        book = API.getMostSoldBookInCategory('Health')
        self.assertEqual(book['Title'], 'Book3')

    def test_searchBookByAuthorName(self):
        API = APIClass.API
        API.addBookToCatalog('Book1', 'Dan', 'Sample code book', 'john', '1000', '111')
        result = API.searchBookbyAuthorname('Dan')
        print(result)
        self.assertEqual(result, ['Book1'])

    def test_searchBookbyBookname(self):
        API = APIClass.API
        API.addBookToCatalog('Book1', 'Dan', 'Sample code book', 'john', '1000', '111')
        book = API.searchBookbyBookname('Book1')
        self.assertEqual(book,'Book1')




