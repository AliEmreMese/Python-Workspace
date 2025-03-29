#Reads data from the file. Takes the file name as an input parameter. Returns a list containing the data read from the file.
def read_data(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))
    return data

#Writes data to the file. Takes the file name and data as input parameters. Writes each item in the data list as a line in the file.
def write_data(file_name, data):
    with open(file_name, 'w') as file:
        for information in data:
            file.write(','.join(map(str, information)) + '\n')

#Lists all books in the library. Takes the list of books as input parameters. Prints the details of each book, including ISBN number, book name, author name, and checked status.
def list_books(books):
    print("\nList of all books in the library:")
    for i in books:
        print(', '.join(i))

#Lists books that are checked out. Takes the list of books as input parameters. Prints details of books that have been checked out.
def list_checked_out_books(books):
    print("\nList of checked out books:")
    for i in books:
        if i[3] == 'T':
            print(', '.join(i))
        else:
            print("There is no checked up book.")
            break

#Adds a new book to the library. Takes the list of books as input parameters. Asks the user for ISBN number, book name, and author name, and adds a new book with 'F' (unchecked) status.
def add_book(books):
    isbn = input("\nEnter ISBN number: ")
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    checked = 'F'
    books.append([isbn, name, author, checked])
    print("Book added successfully!")

#Deletes a book from the library. Takes the list of books as input parameters. Asks the user for the ISBN number of the book to be deleted. If the book is not checked out, it is removed; otherwise, a warning is issued.
def delete_book(books):
    isbn = input("\nEnter ISBN number of the book to delete: ")
    for i in books:
        if i[0] == isbn:
            if i[3] == 'F':
                books.remove(i)
                print("Book deleted successfully!")
            else:
                print("Cannot delete checked out book.")
            return
    print("Book not found!")

#Searches for a book by ISBN number. Takes the list of books as input parameters. Asks the user for an ISBN number and prints details if found.
def search_by_isbn(books):
    isbn = input("\nEnter ISBN number to search: ")
    for i in books:
        if i[0] == isbn:
            print(', '.join(i))
            return
    print("Book not found!")

#Searches for a book by name. Takes the list of books as input parameters. Asks the user for a keyword and prints details of books whose names contain the specified keyword.
def search_by_name(books):
    book_name = input("\nEnter a book name to search: ")
    results = []
    for i in books:
        if book_name.lower() in i[1].lower():
            results.append(i)
    if results:
        print("\nMatching books:")
        for i in results:
            print(', '.join(i))
    else:
        print("Book not found!")

#Checks out a book to a student. Takes the lists of books and students as input parameters. Asks the user for the ISBN number of the book and the student ID. If the book is available, it is checked out to the student.
def check_out_book(books, students):
    isbn = input("\nEnter ISBN number of the book to check out: ")
    student_id = input("Enter student ID: ")
    for i in books:
        if i[0] == isbn:
            if i[3] == 'F':
                i[3] = 'T'
                print("Book checked out successfully!")
                for j in students:
                    if j[0] == student_id:
                        if len(j) > 3:
                            j[3].append(i)
                        else:
                            j.append([i])
                        return
                print("Student not found!")
                return
            else:
                print("Book is already checked out!")
                return
    print("Book not found!")

#Lists all students and books checked out by each student. Takes the list of students as input parameters. Prints details of each student, including student ID, name, surname, and books checked out.
def list_students(students):
    print("\nList of Students:")
    for j in students:
        print(f"{j[0]}, {j[1]} {j[2]}")
        if len(j) > 3:
            name = str(f"{j[3]} {j[4]} {j[5]}")  #Since there are too many nested lists in the students list, I assigned it to a value and removed the redundancies by slice operation.
            print("  Checked out books:", name[2:])
            
#Adds a new student to the system. Takes the list of students as input parameters. Asks the user for the student ID, name, and surname and adds a new student.
def add_student(students):
    student_id = input("\nEnter student ID: ")
    name = input("Enter student name: ")
    surname = input("Enter student surname: ")
    students.append([student_id, name, surname])
    print("Student added successfully!")

#Deletes a student from the system. Takes the list of students as input parameters. Asks the user for the student ID and deletes the student if found.
def delete_student(students):
    student_id = input("\nEnter student ID to delete: ")
    for j in students:
        if j[0] == student_id:
            students.remove(j)
            print("Student deleted successfully!")
            return
    print("Student not found!")

#The main function that drives the entire library application. Manages the menu, user input, and calls the appropriate functions based on the user's choice. Reads initial data from files, performs operations, and writes updated data back to the files upon exit.
def main():
    students = read_data('C:\PROJE\students.txt')
    books = read_data('C:\PROJE\\books.txt')

    while True:
        print("\nLibrary Application Menu:")
        print("1. List all books")
        print("2. List checked out books")
        print("3. Add a new book")
        print("4. Delete a book")
        print("5. Search a book by ISBN")
        print("6. Search a book by name")
        print("7. Check out a book to a student")
        print("8. List all students")
        print("9. Add a new student")
        print("10. Delete a student")

        choice = input("Enter your choice (or 'exit' to exit): ").lower()

        if choice == '1':
            list_books(books)
        elif choice == '2':
            list_checked_out_books(books)
        elif choice == '3':
            add_book(books)
        elif choice == '4':
            delete_book(books)
        elif choice == '5':
            search_by_isbn(books)
        elif choice == '6':
            search_by_name(books)
        elif choice == '7':
            check_out_book(books, students)
        elif choice == '8':
            list_students(students)
        elif choice == '9':
            add_student(students)
        elif choice == '10':
            delete_student(students)
        elif choice == 'exit':
            write_data('C:\PROJE\students.txt', students)
            write_data('C:\PROJE\\books.txt', books)
            print("Exiting the library application. Data saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
