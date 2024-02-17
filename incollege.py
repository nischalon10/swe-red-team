# incollege_app.py

import re

class InCollegeApp:
    def __init__(self):
        self.user_credentials = {
            "test" : {
                'password': "test",
                'first_name': "test",
                'last_name': "test",
                'login_status': False
            },
        }  # Dictionary to store username and password
        self.MAX_ACCOUNTS = 5  # Maximum number of accounts
        self.job_posts = []  # List to store job posts
        
        self.current_language = "English"  # Default language
        self.translations = {
            "English": {},
            "Spanish": {"Welcome to InCollege": "Bienvenida a en la universidad"}
        }

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
            'last_name': last_name,
            'login_status': True
        }

        print("Account created successfully")
        self.get_post_login_options()
        
        
        # [old code]
        # Check if username already exists
        # self.user_credentials[username] = [password, 0]
        # return "Account created successfully"
        

    def login(self, username, password):
        # Check if username and password match
        if username in self.user_credentials and self.user_credentials[username]['password'] == password:
            # [old code]
            # self.user_credentials[username][1] += 1
            self.user_credentials[username]['login_status'] = True
            return "You have successfully logged in"
        return "Incorrect username / password, please try again."
    
    #---------------- epic 1 -----------------#

    def get_post_login_options(self):
        
        # added a new option to the list #4 for epic#2
        options_list = [
            "1. Job search/Internship",
            "2. Find someone you know",
            "3. Learn a new skill",
            "4. Useful Links",
            "5. InCollege Important Links",
            "6. Log out"
        ]
        select_option = "\n".join(options_list)
        print(select_option)
        selected_option = input("Select an option: ")
        self.select_option(selected_option)
        

    def select_option(self, option_number):
        under_construction_message = "Under construction."

        # added a new option to the list #4 for epic#2
        if option_number == "1":
            return under_construction_message
        elif option_number == "2":
            self.find_person()
        elif option_number == "3":
            self.list_skills()
        elif option_number == "4":
            self.display_useful_links()
        elif option_number == "5":
            self.display_important_links()
        elif option_number == "6":
            print("You have successfully logged out.")
            self.main_menu()
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
        print(skill_options)
        print("\nSelect a skill to learn.")
        self.select_skill(input("Enter a number: "))
    
    def select_skill(self, skill_number):
        if skill_number in ["1", "2", "3", "4", "5"]:
            return self.under_construction()
        elif skill_number == "6":
            self.get_post_login_options()
        else:
            return "Invalid Option"
        
    #---------------- epic 2 -----------------#
        
    def display_success_story_and_video_option(self):
        success_story = "Meet Hideo Kojima, a recent graduate who landed their dream job at a top tech company using InCollege."
        print(success_story)

        play_video_option = input("Would you like to watch a video? (yes/no): ")
        if play_video_option.lower() == "yes":
            print("Video is now playing.")
            return
        else:
            return "Thank you for visiting InCollege."
        
    def post_job(self,username):
        if len(self.job_posts) >= 5:
            print("Maximum number of jobs posted. Please try again later.")
            return

        title = input("Enter job title: ")
        description = input("Enter job description: ")
        employer = input("Enter employer: ")
        location = input("Enter location: ")
        salary = input("Enter salary: ")

        self.job_posts.append({
            'title': title,
            'description': description,
            'employer': employer,
            'location': location,
            'salary': salary,
            'username': username
        })

        print("Job posted successfully.")
    
    def find_person(self):
        first_name = input("Enter the first name of the person you are looking for: ")
        last_name = input("Enter the last name of the person you are looking for: ")

        for user_info in self.user_credentials.values():
            if user_info['first_name'].lower() == first_name and user_info['last_name'].lower() == last_name:
                return "They are a part of the InCollege system."
        return "They are not a part of the InCollege system."
    
    def main_menu(self):
        menu_options = [
            self.translate_language("Welcome to InCollege"),
            self.translate_language("Main Menu"),
            "1. Create Account",
            "2. Login",
            "3. View Success Story and Video",
            "4. Exit",
            "5. Useful Links",
            "6. InCollege Important Links"
        ]
        menu = "\n".join(menu_options)
        print(menu)
        
        # print("\nWelcome to InCollege")
        # print("\nMain Menu")
        # print("\n1. Create Account")
        # print("\n2. Login")
        # print("\n3. View Success Story and Video")
        # print("\n4. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            self.create_account(username, password)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login_result = self.login(username, password)
            print(login_result)
            if login_result == "You have successfully logged in":
                self.get_post_login_options()
        elif choice == "3":
            self.display_success_story_and_video_option()
        elif choice == "4":
            print("Thank you for visiting InCollege.")
            return
        elif choice == "5":
            self.display_useful_links()
        elif choice == "6":
            self.display_important_links()
        else:
            return "Invalid Option"

    #---------------- epic 3 -----------------# task 1 and 2 from Kainan
    
    def any_user_logged_in(self):
        return any(user_info['login_status'] for user_info in self.user_credentials.values())

    def translate_language(self, message):
        return self.translations.get(self.current_language, {}).get(message, message)
    
    def under_construction(self):
        return self.translate_language("Under construction.")
    
    def display_useful_links(self):
        useful_links = [
            "1. General",
            "2. Browse InCollege",
            "3. Business Solutions",
            "4. Directories",
            "5. return to previous level"
        ]
        useful_links_options = "\n".join(useful_links)
        print(useful_links_options)
        print("\nSelect a link to view.")
        selected_link = input("Enter a number: ")
        self.select_useful_link(selected_link)
        
    def select_useful_link(self, link_number):
        if link_number == "1":
            self.display_general_links()
        elif link_number in ["2", "3", "4"]:
            return self.under_construction()
        elif link_number == "5":
            if self.any_user_logged_in():
                self.get_post_login_options()
            else:
                self.main_menu()
        else:
            return "Invalid Option"
        
    def display_general_links(self):
        general_links = [
            "1. Sign up",
            "2. Help Center",
            "3. About",
            "4. Press",
            "5. Blog",
            "6. Careers",
            "7. Developers",
            "8. Go back to previous level"
        ]
        general_links_options = "\n".join(general_links)
        print(general_links_options)
        print("\nSelect a link to view.")
        selected_link = input("Enter a number: ")
        self.select_general_link(selected_link)
        
    def select_general_link(self, link_number):
        if link_number == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            self.create_account(username, password)
        elif link_number == "2":
            print("\nWe're here to help")
        elif link_number == "3":
            print("\nIn College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
        elif link_number == "4":
            print("\nIn College Pressroom: Stay on top of the latest news, updates, and reports")
        elif link_number in ["5", "6", "7"]:
            return self.under_construction()
        elif link_number == "8":
            self.display_useful_links()
        else:
            return "Invalid Option"
    
    def display_important_links(self):
        important_links = [
            "1. Copyright Notice",
            "2. About",
            "3. Brand Policy",
            "4. Guest Controls",
            "5. Languages",
            "6. return to previous level"
        ]
        important_links_options = "\n".join(important_links)
        print(important_links_options)
        print("\nSelect a link to view.")
        selected_link = input("Enter a number: ")
        self.select_important_link(selected_link)
    
    def select_important_link(self, link_number):
        if link_number in ["1", "2", "3", "4"]:
            return self.under_construction()
        elif link_number == "5":
            self.display_languages()
        elif link_number == "6":
            if self.any_user_logged_in():
                self.get_post_login_options()
            else:
                self.main_menu()
        else:
            return "Invalid Option"
        
    def display_languages(self):
        languages = [
            "1. English",
            "2. Spanish"
        ]
        languages_options = "\n".join(languages)
        print(languages_options)
        print("\nSelect a language.")
        selected_language = input("Enter a number: ")
        self.select_language(selected_language)
        
    def select_language(self, language_number):
        if language_number in ["1", "2"]:
            return self.set_language(language_number)
        else:
            return "Invalid Option"
    
    def set_language(self, language_number):
        if language_number == "1":
            self.current_language = "English"
        elif language_number == "2":
            self.current_language = "Spanish"
        
        if self.any_user_logged_in():
            self.get_post_login_options()
        else:
            self.main_menu()