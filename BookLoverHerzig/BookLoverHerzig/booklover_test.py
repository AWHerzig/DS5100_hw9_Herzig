import unittest

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        x = BookLover('Aidan', 'a@gmail.com', 'sports')
        x.add_book('mybook', 4)
        self.assertTrue('mybook' in list(x.book_list.book_name))

    def test_2_add_book(self):
        x = BookLover('Aidan', 'a@gmail.com', 'sports')
        x.add_book('mybook', 4)
        x.add_book('mybook', 4)
        self.assertTrue(1 == len(x.book_list))
                
    def test_3_has_read(self): 
        x = BookLover('Aidan', 'a@gmail.com', 'sports')
        x.add_book('mybook', 4)
        self.assertTrue(x.has_read('mybook'))
        
    def test_4_has_read(self): 
        x = BookLover('Aidan', 'a@gmail.com', 'sports')
        x.add_book('mybook', 4)
        self.assertFalse(x.has_read('yourbook'))
        
    def test_5_num_books_read(self): 
        x = BookLover('Aidan', 'a@gmail.com', 'sports')
        x.add_book('mybook', 4)
        x.add_book('mybook2', 4)
        self.assertTrue(2 == x.num_books_read())

    def test_6_fav_books(self):
        x = BookLover('Aidan', 'a@gmail.com', 'sports')
        x.add_book('mybook', 2)
        x.add_book('mybook2', 3)
        x.add_book('mybook3', 4)
        x.add_book('mybook4', 5)
        self.assertTrue(min(list(x.fav_books().book_rating)) > 3)
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)