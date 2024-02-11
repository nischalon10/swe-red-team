# incollege_app.py

import re

class InCollegeApp:
    def __init__(self):
        self.user_credentials = {}  # Dictionary to store username and password
        self.MAX_ACCOUNTS = 5  # Maximum number of accounts
        self.job_posts = []  # List to store job posts

    def create_account(self, username, password):
        # Check if maximum number of accounts has been reached
        if len(self.user_credentials) >= self.MAX_ACCOUNTS:
            return "Maximum number of student accounts created."

        # restrictions for password
        if len(password) < 8 or len(password) > 13:
            return "Password must be between 8 and 13 characters."
        if not re.search(r"[A-Z]", password):
            return "Password must contain at least one capital letter."
        if not re.search(r"\d", password):
            return "Password must contain at least one digit."
        if not re.search(r"[!@#$%^&*()_+{}|:\"<>?]", password):
            return "Password must contain at least one special character."
        
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")

        self.user_credentials[username] = {
            'password': password,
            'first_name': first_name,
            'last_name': last_name
        }

        return "Account created successfully"
        
        # [old code]
        # Check if username already exists
        # self.user_credentials[username] = [password, 0]
        # return "Account created successfully"
        

    def login(self, username, password):
        # Check if username and password match
        if username in self.user_credentials and self.user_credentials[username][0] == password:
            self.user_credentials[username][1] += 1
            return "You have successfully logged in"
        return "Incorrect username / password, please try again."

    #---------------- epic 1 -----------------#

    def get_post_login_options(self):
        
        # added a new option to the list #4 for epic#2
        options_list = [
            "1. Job search/Internship",
            "2. Find someone you know",
            "3. Learn a new skill"
            "4. Log out / return to previous level"
        ]
        select_option = "\n".join(options_list)
        return select_option

    def select_option(self, option_number):
        under_construction_message = "Under construction."

        # added a new option to the list #4 for epic#2
        if option_number == "1":
            return under_construction_message
        elif option_number == "2":
            return under_construction_message
        elif option_number == "3":
            return self.list_skills()
        elif option_number == "4":
            return "You have been logged out."
            # or return self.main_menu() for future development
        else:
            return "Invalid Option"

    def list_skills(self):
        skills = [
            "1. Programming",
            "2. Data Analysis",
            "3. Graphic Design",
            "4. Digital Marketing",
            "5. Project Management",
            "6. return to previous level"
        ]
        skill_options = "\n".join(skills)
        return skill_options + "\nSelect a skill to learn."
    
    def select_skill(self, skill_number):
        under_construction_message = "Under construction."
        if skill_number in ["1", "2", "3", "4", "5"]:
            return under_construction_message
        elif skill_number == "6":
            return self.get_post_login_options()
        else:
            return "Invalid Option"
        
    #---------------- epic 2 -----------------#
        
    def display_success_story_and_video_option(self):
        success_story = "Meet Hideo Kojima, a recent graduate who landed their dream job at a top tech company using InCollege."
        print(success_story)

        play_video_option = input("Would you like to watch a video? (yes/no): ")
        if play_video_option.lower() == "yes":
            return "Video is now playing."
        else:
            return "Thank you for visiting InCollege."
        
    def find_person(self):
        first_name = input("Enter the first name of the person you are looking for: ")
        last_name = input("Enter the last name of the person you are looking for: ")

        for user_info in self.user_credentials.values():
            if user_info['first_name'].lower() == first_name and user_info['last_name'].lower() == last_name:
                return "They are a part of the InCollege system."
        return "They are not a part of the InCollege system."
    
    def main_menu(self):
        while True:
            print("\nWelcome to InCollege")
            print("Main Menu")
            print("1. Create Account")
            print("2. Login")
            print("3. View Success Story and Video")
            print("4. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                print(self.create_account(username, password))
            elif choice == "2":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                print(self.login(username, password))
                if self.login(username, password) == "You have successfully logged in":
                    print(self.get_post_login_options())
                    option = input("Select an option: ")
                    print(self.select_option(option))
            elif choice == "3":
                print(self.display_success_story_and_video_option())
            elif choice == "4":
                print("Thank you for visiting InCollege.")
                break
            else:
                print("Invalid Option")
