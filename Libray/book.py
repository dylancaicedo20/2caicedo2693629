class Book:
    def __init__(self, title, author, ISBN, yearpub):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.yearpub = yearpub

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_ISBN(self):
        return self.ISBN

    def set_ISBN(self, ISBN):
        self.ISBN = ISBN

    def get_yearpub(self):
        return self.yearpub

    def set_yearpub(self, yearpub):
        self.yearpub = yearpub

    @staticmethod
    def show_due_date():
        print("Due date: June 30, 2023")

    def reservation_status(self, option):
        if self.title == option:
            print("You reserved that book")
        else:
            print("You cannot reserve that book")

    def request_status(self, option):
        if self.title == option:
            print("Book status: Available")
        else:
            print("Book status: Unavailable")

    def renewal_info(self, option):
        if self.title == option:
            print("Renewal information: You can renew this book for 7 more days")
        else:
            print("This book cannot be renewed")

    def book_details(self):
        while True:
            print("1. Show Due Date")
            print("2. Check Reservation Status")
            print("3. Check Request Status")
            print("4. Get Renewal Information")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                Book.show_due_date()
            elif choice == "2":
                option = input("Enter the book title: ")
                self.reservation_status(option)
            elif choice == "3":
                option = input("Enter the book title: ")
                self.request_status(option)
            elif choice == "4":
                option = input("Enter the book title: ")
                self.renewal_info(option)
            elif choice == "5":
                print("Exiting the menu...")
                break
            else:
                print("Invalid choice. Please try again.")
