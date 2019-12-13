from db_connect import *

while True:
    print('press 1 if you wish to add  a book to the library')
    print('press 2 if you wish to add the postcode,latitude and longitude to the book')
    print('press 3 if you wish to look up all the ebooks')
    number = input('Enter the number you wish to choose')
    new_ebook = MSDBConnection()
    if number == '1':
        # new_ebook = MSDBConnection()
        # MSDBConnection().title_in()
        # MSDBConnection().author_in()
        # MSDBConnection().release_in()
        new_ebook.insert_to()
    elif number == '2':
        new_ebook.ins_long_lat()
    elif number == '3':
        print( new_ebook.select_from())
    else:
        print('you did not enter a valid number!')
        exit()
