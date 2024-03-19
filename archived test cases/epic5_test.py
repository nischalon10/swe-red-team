import pytest
from unittest.mock import patch
from incollege import InCollegeApp
# make sure to run `pytest epic5_test.py` in the terminal to test the code

@pytest.fixture
def app():
    return InCollegeApp()

def test_create_profile_success(app, capsys):
    app.user_credentials = {'test1': 'password123'}
    username = 'test1'
    profile_title = 'Software Engineer'
    major = 'computer science'
    university = 'mit'
    about = 'Passionate developer'
    experience = ['Internship at Google', 'Part-time job at local IT company']
    education = 'BSc in Computer Science'

    app.create_profile(username, profile_title, major, university, about, experience, education)

    captured = capsys.readouterr()
    assert "Profile saved for test1:" in captured.out
    assert app.profiles[username]['profile_title'] == profile_title
    assert app.profiles[username]['major'] == major.capitalize()
    assert app.profiles[username]['university'] == university.capitalize()
    assert app.profiles[username]['about'] == about
    assert app.profiles[username]['experience'] == experience[:3]
    assert app.profiles[username]['education'] == education

def test_create_profile_nonexistent_user(app, capsys):
    username = 'test2'
    profile_title = 'Data Scientist'
    major = 'statistics'
    university = 'stanford'

    app.create_profile(username, profile_title, major, university)

    captured = capsys.readouterr()
    assert f"Error: User with username '{username}' does not exist." in captured.out
    assert username not in app.profiles

def test_view_existing_profile(app):
    username = 'test3'
    profile_data = {
        'profile_title': 'Software Engineer',
        'major': 'Computer Science',
        'university': 'MIT',
        'about': 'Enthusiastic programmer',
        'experience': [],
        'education': 'BSc in Computer Science'
    }
    app.profiles[username] = profile_data

    profile = app.view_profile(username)
    assert profile == profile_data

def test_view_nonexistent_profile(app):
    username = 'test4'
    profile = app.view_profile(username)
    assert profile == {}
