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
    ("1", "Under construction."),
    ("2", "Under construction."),
    ("3", "1. Programming\n2. Data Analysis\n3. Graphic Design\n4. Digital Marketing\n5. Project Management\n6. return to previous level\nSelect a skill to learn."),
    ("4", "You have been logged out."),
    ("5", "Invalid Option")  # Test an invalid option
])

def test_select_option(app, option_number, expected_result):
    result = app.select_option(option_number)
    assert result == expected_result, f"Response for option number '{option_number}' should be correct"

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


def test_main_menu_goodbye(app, monkeypatch):
    # monkeypatch.setattr('builtins.input', lambda msg: "1" if msg == "Select an option: " else "user1")
    monkeypatch.setattr('builtins.input', lambda _: "4")
    result = app.main_menu()
    assert result == None

def custom_main_menu_input(msg):
    if msg == "Select an option: ":
        return "1"
    elif msg == "Enter your username: ":
        return "user1"
    elif msg == "Enter your password: ":
        return "ValidPass123!"
    elif msg =="Would you like to watch a video? (yes/no): ":
        return "Yes"
    else:
        return "user1"

def test_main_menu_create_account(app, monkeypatch):
    monkeypatch.setattr('builtins.input', custom_main_menu_input)
    result = app.main_menu()
    assert result == "Account created successfully", "Account should be created successfully with valid credentials"

def test_main_menu_login(app, monkeypatch):
    
    monkeypatch.setattr('builtins.input', custom_main_menu_input)
    app.create_account("user1", "ValidPass123!")
    result = app.main_menu()

    assert result == "You have successfully logged in", "Login should be successful with correct credentials"

def test_main_menu_success_story(app, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3")
    result = app.main_menu()
    assert result == "Video is now playing.", "Success story should be correctly listed and video should be played"

