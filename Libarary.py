import sys
import logging


class Library:
    def __init__(self, list_of_books):
        self.available_books = list_of_books

    # displays all the books available and not available
    def display_available_books(self):
        print("\n\nShowing all available books :")
        print("****************************")
        print("{}\t\t{}\t\t{}\t\t{} ".format('Id', 'Name', 'Author', 'Status'))
        print('=' * 50)
        for book in self.available_books:
            print("{}\t\t{}\t\t{}\t\t{} ".format(book['id'], book['Name'], book['Author'], book['Status']))
        print('\n\n')

    def add_book(self):
        book_name = input('Enter the book title: ')
        book_author = input('Enter the book author:')

        new_id = max([b['id'] for b in self.available_books]) + 1
        # the librarian can add the book , treating the ID as primary key , we have ensured that
        # this is calculated by us to avoid any entry manually

        a = ({'id': new_id, 'Name': book_name.capitalize(), 'Author': book_author.capitalize(), 'Status': 'Available'})
        self.available_books.append(a)  # adding the record to list

        self.display_available_books()  # displaying all the records


    def delete_book(self):

        self.display_available_books()  # shows the list , so that it becomes easier to enter the correct id
        print("Enter the ID of the book you'd like to delete>>")
        id = int(input())

        for i in range(len(self.available_books)):
            if self.available_books[i]['id'] == id:
                a = self.available_books.pop(i)
                print('Book ID : {} Deleted Successfully'.format(a['id']))  # displaying the book deleted
                return

        logging.warning('Book cannot be found')

    # toggle book status ,i have smartly ensured that only the status field of the book gets updated ,
    # all the fields would have taken time, here we just checks for available/ not available and swaps it
    def toggle_book_status(self):
        self.display_available_books()
        print("Enter the ID of the book you'd like to update the status for>>")
        # going by ID bcos its a number and we can easily make mistake in big words

        id = int(input())

        for book in self.available_books:
            if book['id'] == id:
                book['Status'] = 'Available' if book['Status'] == 'NotAvailable' else 'NotAvailable'
                print('Book Status Updated : {}'.format(book['Status']))
                return self.display_available_books()  # to ensure we don't need to go the main menu to check the update
        logging.warning('Book not found')




class Student:
    def __init__(self, library):
        self.library = library

    def lend_book(self):
        # i know mentioning the entire dataset as output is not recommended but here i wanted for you to be easy to
        # copy paste the names of the books
        self.library.display_available_books()
        print("Enter the name of the book you'd like to borrow>>")
        book = input()
        for requestedBook in self.library.available_books:
            if requestedBook['Name'] == book and requestedBook['Status'] == 'Available':
                print(" this book is available and you can borrow it for 2 weeks")
                requestedBook[
                    'Status'] = 'NotAvailable'
                return self.library.display_available_books()
        # after lending the book we are ensuring we update the status in the main table so that if a person requests for a book he can see the updated status
        logging.warning("this book is not available, please try after two weeks")



    #we should also have a timestamp field , which will get updated along with the Not available status when the book is borrowed ,
    #which will keep checking the timestamp and as soon as it is beyond 2 weeks a notification should be sent out.



def main():
    person = input(" For student press 's' for librarian press 'l'")

    #student will have access to view - 1  and Request -2 a book only ,
    # librarian can add -3 ,delete -4 and update - 5 the books/ records

    if not (person.lower() == 's' or person.lower() == 'l'):
        logging.warning('Invalid  input bye bye')
        return

    # my dataset, i have made it small to save time
    list_of_books = [{'id': 1001, 'Name': 'Ramayana', 'Author': 'Author1', 'Status': 'Available'},
                     {'id': 1002, 'Name': 'Bhagwatgeeta', 'Author': 'Author2', 'Status': 'Available'},
                     {'id': 1003, 'Name': 'Mahabarath', 'Author': 'Author3', 'Status': 'NotAvailable'},
                     {'id': 1004, 'Name': 'Valmikistories', 'Author': 'Author4', 'Status': 'Available'},
                     {'id': 1005, 'Name': 'AriabianNights', 'Author': 'Author5', 'Status': 'Available'}]

    library = Library(list_of_books=list_of_books)
    student = Student(library)

    while True:
        try:
            print(""" ======LIBRARY MENU=======
                      1. Display all available books
                      2. Request a book - By student only 
                      3. Add Book -By librarian only
                      4. Delete Book -By librarian only
                      5. Update_book_status --By librarian only
                      6. Exit
                      """)
            choice = int(input("Enter Choice:"))
            if choice == 1:
                library.display_available_books()
            elif choice == 2 and person == 's':  # check for condition if its a student and not a librarian
                student.lend_book()
            elif choice == 3 and person == 'l':  # check for librarian only
                library.add_book()
            elif choice == 4 and person == 'l':
                library.delete_book()
            elif choice == 5 and person == 'l':
                library.toggle_book_status()
            elif choice == 6:
                sys.exit()
            else:
                logging.warning('Invalid Choice or you do not have access')
        except:
            logging.warning('Incorrect Input')


if __name__ == '__main__':
    main()
