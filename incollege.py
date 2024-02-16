# incollege_app.py

import re
from deep_translator import GoogleTranslator

class InCollegeApp:
    def __init__(self):
        self.user_credentials = {
            "test" : {
                'password': "test",
                'first_name': "test",
                'last_name': "test"
            },
        }  # Dictionary to store username and password
        self.MAX_ACCOUNTS = 5  # Maximum number of accounts
        self.job_posts = []  # List to store job posts  
        self.language = "English"  # Default language is English

    def create_account(self, username, password):
        # Check if maximum number of accounts has been reached
        if len(self.user_credentials) >= self.MAX_ACCOUNTS:
            return self.translate_language("Maximum number of student accounts created.")

        # restrictions for password
        if len(password) < 8 or len(password) > 13:
            return self.translate_language("Password must be between 8 and 13 characters.")
        if not re.search(r"[A-Z]", password):
            return self.translate_language("Password must contain at least one capital letter.")
        if not re.search(r"\d", password):
            return self.translate_language("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*()_+{}|:\"<>?]", password):
            return self.translate_language("Password must contain at least one special character.")
        
        first_name = input(self.translate_language("Enter your first name: "))
        last_name = input(self.translate_language("Enter your last name: "))

        self.user_credentials[username] = {
            'password': password,
            'first_name': first_name,
            'last_name': last_name
        }

        return self.translate_language("Account created successfully")
        
        # [old code]
        # Check if username already exists
        # self.user_credentials[username] = [password, 0]
        # return "Account created successfully"
        

    def login(self, username, password):
        # Check if username and password match
        if username in self.user_credentials and self.user_credentials[username]['password'] == password:
            # [old code]
            # self.user_credentials[username][1] += 1
            return self.translate_language("You have successfully logged in")
        return self.translate_language("Incorrect username / password, please try again.")

    #---------------- epic 1 -----------------#

    def get_post_login_options(self):
        
        # added a new option to the list #4 for epic#2
        options_list = [
            "1. Job search/Internship",
            "2. Find someone you know",
            "3. Learn a new skill",
            "4. Log out / return to previous level"
        ]
        select_option = "\n".join(options_list)
        return self.translate_language(select_option)

    def select_option(self, option_number, username):
        under_construction_message = self.translate_language("Under construction.")

        # added a new option to the list #4 for epic#2
        if option_number == "1":
            return self.post_job(username)
        elif option_number == "2":
            return self.find_person()
        elif option_number == "3":
            return self.list_skills()
        elif option_number == "4":
            return self.translate_language("You have been logged out.")
            # or return self.main_menu() for future development
        else:
            return self.translate_language("Invalid Option")

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
        return self.translate_language(skill_options + "\nSelect a skill to learn.")
    
    def select_skill(self, skill_number):
        under_construction_message = self.translate_language("Under construction.")
        if skill_number in ["1", "2", "3", "4", "5"]:
            return under_construction_message
        elif skill_number == "6":
            return self.get_post_login_options()
        else:
            return self.translate_language("Invalid Option")
        
    #---------------- epic 2 -----------------#
        
    def display_success_story_and_video_option(self):
        success_story = self.translate_language("Meet Hideo Kojima, a recent graduate who landed their dream job at a top tech company using InCollege.")
        print(success_story)

        play_video_option = input(self.translate_language("Would you like to watch a video? (yes/no): "))
        if play_video_option.lower() == "yes":
            return self.translate_language("Video is now playing.")
        else:
            return self.translate_language("Thank you for visiting InCollege.")
        
    def post_job(self,username):
        if len(self.job_posts) >= 5:
            print(self.translate_language("Maximum number of jobs posted. Please try again later."))
            return

        title = input(self.translate_language("Enter job title: "))
        description = input(self.translate_language("Enter job description: "))
        employer = input(self.translate_language("Enter employer: "))
        location = input(self.translate_language("Enter location: "))
        salary = input(self.translate_language("Enter salary: "))

        self.job_posts.append({
            'title': title,
            'description': description,
            'employer': employer,
            'location': location,
            'salary': salary,
            'username': username
        })

        print(self.translate_language("Job posted successfully."))
    
    def find_person(self):
        first_name = input(self.translate_language("Enter the first name of the person you are looking for: "))
        last_name = input(self.translate_language("Enter the last name of the person you are looking for: "))

        for user_info in self.user_credentials.values():
            if user_info['first_name'].lower() == first_name and user_info['last_name'].lower() == last_name:
                return self.translate_language("They are a part of the InCollege system.")
        return self.translate_language("They are not a part of the InCollege system.")
    
    def main_menu(self):
        self.choose_language()
        menu_options = [
            "Welcome to InCollege",
            "Main Menu",
            "1. Create Account",
            "2. Login",
            "3. View Success Story and Video",
            "4. Exit"
        ]
        menu = "\n".join(menu_options)
        print(self.translate_language(menu))

        choice = input(self.translate_language("\nSelect an option: "))

        if choice == "1":
            username = input(self.translate_language("Enter your username: "))
            password = input(self.translate_language("Enter your password: "))
            print(self.create_account(username, password))
        elif choice == "2":
            username = input(self.translate_language("Enter your username: "))
            password = input(self.translate_language("Enter your password: "))
            login_result = self.login(username, password)
            print(self.translate_language(login_result))
            if login_result == "You have successfully logged in":
                print(self.get_post_login_options())
                option = input(self.translate_language("Select an option: "))
                print(self.select_option(option, username))
        elif choice == "3":
            print(self.translate_language(self.display_success_story_and_video_option()))
        elif choice == "4":
            print(self.translate_language("Thank you for visiting InCollege."))
        else:
            print(self.translate_language("Invalid Option"))

#---------------- epic 3 -----------------#

    def translate_language(self, msg):
        if self.language.lower() == 'spanish':
            translated = GoogleTranslator(source='en', target='es').translate(msg)
            return translated
        else:    
            return msg
        
    def choose_language(self):
        language = input("Choose a language: ")
        if language.lower() in ['english', 'spanish']:
            self.language = language
            return f"Language has been set to {language}."
        else:
            return "Invalid language. Please choose English or Spanish."
        
# to test code functionality
        

#task 4 example code
# test = InCollegeApp()
# test.choose_language()
# print(test.translate_language("Hello"))
# print(test.create_account("user1", "ValidPass123!"))