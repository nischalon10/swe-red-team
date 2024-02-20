import pytest
from unittest.mock import patch
from incollege import InCollegeApp


@pytest.fixture
def app():
    return InCollegeApp()

# ----------------- Epic 1 ----------------- #
def test_successful_account_creation(app, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "User1")
    result = app.create_account("user1", "ValidPass123!")
    assert result == "Account created successfully", "Account should be created successfully with valid credentials"

def test_account_creation_with_invalid_password(app):
    result = app.create_account("user2", "pass")
    assert "Password must" in result, "Account should not be created with an invalid password"

def test_account_creation_with_invalid_password_CAPITAL(app):
    result = app.create_account("user2", "pass1234!")
    assert "Password must" in result, "Account should not be created with an invalid password"

def test_account_creation_with_invalid_password_digit(app):
    result = app.create_account("user2", "passWord!")
    assert "Password must" in result, "Account should not be created with an invalid password"

def test_account_creation_with_invalid_password_special(app):
    result = app.create_account("user2", "passW0rds")
    assert "Password must" in result, "Account should not be created with an invalid password"

def test_account_creation_limit(app, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "User1")
    for i in range(1, 6):
        app.create_account(f"user{i}", "ValidPass123!")

    result = app.create_account("user6", "ValidPass123!")
    assert result == "Maximum number of student accounts created.", "Should not allow creating more than 5 accounts"

def test_successful_login(app, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "user1")
    app.create_account("user1", "ValidPass123!")
    result = app.login("user1", "ValidPass123!")
    assert result == "You have successfully logged in", "Login should be successful with correct credentials"

def test_failed_login(app):
    result = app.login("nonexistent_user", "wrongpassword")
    assert result == "Incorrect username / password, please try again.", "Login should fail with incorrect credentials"

def test_post_login_options(app):
    result = app.get_post_login_options()
    assert result == "1. Job search/Internship\n2. Find someone you know\n3. Learn a new skill\n4. Log out / return to previous level", "Post-login options should be correctly listed"

@pytest.mark.parametrize("option_number, expected_result", [
    ("1", None),
    ("2", "part of the InCollege system."),
    ("3", "1. Programming\n2. Data Analysis\n3. Graphic Design\n4. Digital Marketing\n5. Project Management\n6. return to previous level\nSelect a skill to learn."),
    ("4", "You have been logged out."),
    ("5", "Invalid Option")  # Test an invalid option
])

def test_select_option(app, option_number, expected_result, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "user1")
    app.create_account("user1", "ValidPass123!")
    result = app.select_option(option_number, "user1")
    assert result == expected_result or expected_result in result, f"Response for option number '{option_number}' should be correct"

def test_select_skill(app):
    result = app.select_skill("1")
    assert result == "Under construction.", "Selecting a skill should be under construction"

    result = app.select_skill("6")
    assert result == "1. Job search/Internship\n2. Find someone you know\n3. Learn a new skill\n4. Log out / return to previous level", "Selecting the last skill should return to previous level"

    result = app.select_skill("7")
    assert result == "Invalid Option", "Selecting an invalid skill should return an invalid option message"

# ----------------- Epic 2 ----------------- #

def test_view_success_story_and_video(app,monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "yes")
    result = app.display_success_story_and_video_option()
    assert result == "Video is now playing.", "Success story should be correctly listed and video should be played"

    
def test_view_success_story_and_no_video(app,monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "no")
    result = app.display_success_story_and_video_option()
    assert result == "Thank you for visiting InCollege.", "Success story should be correctly listed and thank you message should be displayed"

def custom_post_job_input(msg):
    if msg == "Enter your username: ":
        return "user1"
    else:
        return "user1"


def test_post_job(app, capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "user1")
    result = app.post_job("user1")
    out, err = capfd.readouterr()
    assert "Job posted successfully." in out, "Job should be posted successfully"
    

def test_post_job_max_limit(app, capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "user1")
    app.create_account("user1", "ValidPass123!")
    
    
    for i in range(1, 6):
        app.post_job("user1")
        out, err = capfd.readouterr()
        assert "Job posted successfully." in out, "Should allow posting up to 5 jobs"

    app.post_job("user1")
    out, err = capfd.readouterr()
    assert "Maximum number of jobs posted. Please try again later." in out, "Should not allow posting more than 5 jobs"

def custom_find_person_input(msg):
    if msg == "Enter the first name of the person you are looking for: ":
        return "user1"
    elif msg == "Enter the last name of the person you are looking for: ":
        return "user1"
    else:
        return "user1"

def test_find_person_fail(app, monkeypatch):
    monkeypatch.setattr('builtins.input', custom_find_person_input)
    result = app.find_person()
    assert result == "They are not a part of the InCollege system.", "Find person should fail if the person is not found"

def test_find_person_success(app, capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', custom_find_person_input)
    app.create_account("user1", "ValidPass123!")
    result = app.find_person()
    assert result == "They are a part of the InCollege system." , "Find person should succeed if the person is found"

def custom_main_menu_input_for_create_account(msg):
    if msg == "\nSelect an option: ":
        return "1"
    elif msg == "Enter your username: ":
        return "user1"
    elif msg == "Enter your password: ":
        return "ValidPass123!"
    else:
        return "user1"


def test_main_menu_create_account(app, capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', custom_main_menu_input_for_create_account)
    result = app.main_menu()
    out, err = capfd.readouterr()
    assert "Account created successfully" in out, "Create account should be successful with valid credentials"


def custom_main_menu_input_for_login_and_job_post(msg):
    if msg == "\nSelect an option: ": #for main menu option
        return "2"
    if msg == "Select an option: ": #for post login option
        return "1"
    elif msg == "Enter your username: ":
        return "user1"
    elif msg == "Enter your password: ":
        return "ValidPass123!"
    else:
        return "user1"
    
def test_main_menu_login_and_job_post(app, capfd, monkeypatch):
    
    monkeypatch.setattr('builtins.input', custom_main_menu_input_for_login_and_job_post)

    app.create_account("user1", "ValidPass123!")
    result = app.main_menu()
    out, err = capfd.readouterr()
    assert "Job posted successfully." in out, "Login should be successful and job post should be successful"

def custom_main_menu_input_for_login_and_didnt_find_person(msg):
    if msg == "\nSelect an option: ": #for main menu option
        return "2"
    if msg == "Select an option: ": #for post login option
        return "2"
    elif msg == "Enter your username: ":
        return "user1"
    elif msg == "Enter your password: ":
        return "ValidPass123!"
    elif msg == "Enter the first name of the person you are looking for: ":
        return "user2"
    elif msg == "Enter the last name of the person you are looking for: ":
        return "user2"
    else:
        return "user1"
    
def test_main_menu_login_and_didnt_find_person(app, capfd, monkeypatch):
    
    monkeypatch.setattr('builtins.input', custom_main_menu_input_for_login_and_didnt_find_person)

    app.create_account("user1", "ValidPass123!")
    result = app.main_menu()
    out, err = capfd.readouterr()
    assert "They are not a part of the InCollege system." in out, "Login should be successful and find person should be successful"

def custom_main_menu_input_for_login_and_find_person(msg):
    if msg == "\nSelect an option: ": #for main menu option
        return "2"
    if msg == "Select an option: ": #for post login option
        return "2"
    elif msg == "Enter your username: ":
        return "user1"
    elif msg == "Enter your password: ":
        return "ValidPass123!"
    elif msg == "Enter the first name of the person you are looking for: ":
        return "user1"
    elif msg == "Enter the last name of the person you are looking for: ":
        return "user1"
    else:
        return "user1"
    
def test_main_menu_login_and_find_person(app, capfd, monkeypatch):
    
    monkeypatch.setattr('builtins.input', custom_main_menu_input_for_login_and_find_person)

    app.create_account("user1", "ValidPass123!")
    result = app.main_menu()
    out, err = capfd.readouterr()
    assert "They are not a part of the InCollege system." in out, "Login should be successful and find person should be successful"

def custom_main_menu_input_success_story_and_video(msg):
    if msg == "\nSelect an option: ":
        return "3"
    elif msg =="Would you like to watch a video? (yes/no): ":
        return "Yes"
    else:
        return "user1"


def test_main_menu_success_story_and_video(app, capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', custom_main_menu_input_success_story_and_video)
    result = app.main_menu()
    out, err = capfd.readouterr()
    assert "Video is now playing." in out, "Success story should be correctly listed and video should be played"

def custom_main_menu_input_success_story_without_video(msg):
    if msg == "\nSelect an option: ":
        return "3"
    elif msg =="Would you like to watch a video? (yes/no): ":
        return "No"
    else:
        return "user1"

def test_main_menu_success_story_without_video(app, capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', custom_main_menu_input_success_story_without_video)
    result = app.main_menu()
    out, err = capfd.readouterr()
    assert "Thank you for visiting InCollege." in out, "Success story should be correctly listed and thank you message should be displayed"

def test_main_menu_goodbye(app, capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "4")
    result = app.main_menu()
    out, err = capfd.readouterr()
    assert "Thank you for visiting InCollege." in out, "Goodbye message should be displayed"

def test_main_menu_invalid(app, capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "5")
    result = app.main_menu()
    out, err = capfd.readouterr()
    assert "Invalid Option" in out, "Invalid option should be handled correctly"

# ----------------- Epic 3 ----------------- #

def test_any_user_logged_in(self, app_instance):
        # Ensure the method returns a boolean value
        result = app_instance.any_user_logged_in()
        assert isinstance(result, bool)

def test_translate_language(self, app_instance):
        # Ensure the method returns a string
        msg = "Hello, World!"
        result = app_instance.translate_language(msg)
        assert isinstance(result, str)

def test_under_construction(self, app_instance):
        # Ensure the method returns a string
        result = app_instance.under_construction()
        assert isinstance(result, str)

def test_display_useful_links(self, app_instance, capsys, monkeypatch):
        # Simulate user input to select a link
        monkeypatch.setattr('builtins.input', lambda _: "1")
        app_instance.display_useful_links()

        # Capture the output and check if it contains the expected options menu
        captured = capsys.readouterr()
        assert "1. General" in captured.out  # Adjust based on actual output


def test_select_useful_link(self, app_instance, monkeypatch, capsys):
        # Simulate user input to select a link
        monkeypatch.setattr('builtins.input', lambda _: "1")
      
        # Check if the method performs the expected action
        app_instance.select_useful_link("1")
      
        # Capture the output and check if it contains the expected options menu
        captured = capsys.readouterr()
        assert "1. Sign up" in captured.out  # Adjust based on actual output

