import students
import os

def main():
    # Main loop of the system (runs until user exits)
    while True:

        # Display system title
        print(f"\nStudent Management System")

        # Display menu options to the user
        print("""
\033[1;34m 1. \033[0mRegister student
\033[1;34m 2. \033[0mConsult list of students
\033[1;34m 3. \033[0mFound student
\033[1;34m 4. \033[0mChange data student
\033[1;34m 5. \033[0mDelete data student
\033[1;31m 6. \033[0mExit
""")

        # Print separator line
        print("\033[1;34m" + "-"*113 + "\033[0m")

        # Ask user to select an option
        option = input("\n\033[34m >> \033[0mPlease select a option: ")

        print("\n\033[1;34m" + "-"*113 + "\033[0m")

        # Clear the console screen depending on the operating system
        os.system("cls" if os.name == "nt" else "clear")
        
        # Option 1: Register a new client
        if option == "1":
            students.register_student()

        # Option 2: Show all registered clients
        elif option == "2":
            students.student_shows()
        
        # Option 3: Display cinema room visualization
        elif option == "3":
            students.student_found()
        # Option 4: Execute ticket purchase process
        elif option == "4":
            students.student_change()
        elif option == "5":
            students.student_delet()

        # Option 6: Exit the system
        elif option == "6":
            print("\n\033[1;32m" + "-"*113 + "\n" + 
                    f"{'END OF THE SYSTEM MANAGEMENT THANKS FOR YOU USE :)':^113}" + 
                    "\n" + "-"*113 + "\033[0m")
            break

        # Handle invalid option
        else:
            print("\n\033[1;31m" + "-"*113 + "\n" + 
                    f"{'INVALID OPTION!':^113}" + 
                    "\n" + "-"*113 + "\033[0m")


# Entry point of the program
if __name__ == "__main__":
    main()
