class Model:
    def __init__(self):
        import sqlite3
        self.conn = sqlite3.connect('books.db')
        self.cursor = self.conn.cursor()
    
    def get_data(self):
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall()
    
    def add_data(self, title, author, genre, publication_year): # Adds a new book into the database
        self.cursor.execute('INSERT INTO books (title, author, genre, publication_year) VALUES (?, ?, ?, ?)', (title, author, genre, publication_year))# Takes a new book and imputs it into the database.
        self.conn.commit()
    
    def remove_data(self, id): # Removes book from the database file. 
        self.cursor.execute('DELETE FROM books WHERE id=?', (id,)) # Takes the given ID and uses it to remove said book from databse.
        self.conn.commit()

    def get_rows(self):
        self.cursor.execute('SELECT * FROM books')
        results = self.cursor.fetchall()
        return len(results)
    
    def get_row(self, num, info):
        command = 'SELECT '+info+' FROM books'
        self.cursor.execute(command)
        results = self.cursor.fetchall()
        return results[num]
    
    def get_row_id(self, id, info):
        command = 'SELECT '+info+' FROM books WHERE id='+id
        self.cursor.execute(command)
        results = self.cursor.fetchall()
        return results[0]

    def borrow_book(self, book_id, patron_name, borrowed_date, return_date):
        self.cursor.execute('UPDATE books SET borrow_name=?, borrow_date=?, return_date=? WHERE id=?',
                            (patron_name, borrowed_date, return_date, book_id))
        self.conn.commit()


class view:
    def __init__(self, model):
        self.model = model
        
    def show_data(self):
        data = self.model.get_data()
        for row in data:
            print(f'\n{row}')









