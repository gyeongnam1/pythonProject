'''
ex15-3-object3.py
'''

class Book:
    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print('책 제목 : {}'.format(self.title))
        print('저자 : {}'.format(self.author))

book1 = Book()
book2 = Book()

book1.set_info('python', '민경태')
book2.set_info('어린왕자', '생텍쥐페리')

book_list = [book1, book2] #객체도 리스트로 담을 수 있다.
for book in book_list:
    book.print_info()