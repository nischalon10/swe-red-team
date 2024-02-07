import re

class InCollegeApp:
    def __init__(self):
        self.user_credentials = {}  # Dictionary to store username and password
        self.MAX_ACCOUNTS = 5  # Maximum number of accounts

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
        
        # Check if username already exists
        self.user_credentials[username] = [password, 0]
        return "Account created successfully"

    def login(self, username, password):
        # Check if username and password match
        if username in self.user_credentials and self.user_credentials[username][0] == password:
            self.user_credentials[username][1] += 1
            return "You have successfully logged in"
        return "Incorrect username / password, please try again."

    #---------------------------------#

    def get_post_login_options(self):
        return ["1. Job search/Internship", "2. Find someone you know", "3. Learn a wew skills", "4. Return to Previous Level"]

    def select_option(self, option_number):
        under_construction_message = "Under construction."

        if option_number == "1":
            return under_construction_message
        elif option_number == "2":
            return under_construction_message
        elif option_number == "3":
            return self.list_skills()
        elif option_number == "4":
            return "Returned to previous level"
        else:
            return "Invalid Option"

    def list_skills(self):
        skills = [
            "1. Programming",
            "2. Data Analysis",
            "3. Graphic Design",
            "4. Digital Marketing",
            "5. Project Management"
        ]
        skill_options = "\n".join(skills)
        skill_options += "\n6. Return to Previous Level"
        return skill_options + "\nSelect a skill to learn."
