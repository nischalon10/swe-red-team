import pytest
from unittest.mock import patch
from incollege import InCollegeApp
# make sure to run `pytest epic6_test.py` in the terminal to test the code

@pytest.fixture
def app():
    return InCollegeApp()

def test_job_search_by_company(app):
    
    app.job_posts = [
        {'id': 1, 'employer': 'Company A', 'role': 'Developer', 'experience_level': 'Mid'},
        {'id': 2, 'employer': 'Company B', 'role': 'Designer', 'experience_level': 'Senior'},
    ]
    filtered_jobs = app.job_search(company='Company A')
    assert len(filtered_jobs) == 1
    assert filtered_jobs[0]['employer'] == 'Company A'

def test_job_search_with_multiple_filters(app):
    
    app.job_posts = [
        {'id': 1, 'employer': 'Company A', 'role': 'Developer', 'experience_level': 'Entry'},
        {'id': 2, 'employer': 'Company B', 'role': 'Designer', 'experience_level': 'Senior'},
        {'id': 3, 'employer': 'Company A', 'role': 'Developer', 'experience_level': 'Senior'},
    ]
    filtered_jobs = app.job_search(company='Company A', role='Developer', experience_level='Senior')
    assert len(filtered_jobs) == 1
    assert filtered_jobs[0]['id'] == 3

def test_apply_for_job_updates_applied_jobs(app):
    
    with patch.object(app, 'applied_jobs', new={}):
        app.apply_for_job(
            username='user1',
            job_title='Developer',
            job_description='Develop stuff',
            employer='Company A',
            location='Location A',
            salary=50000,
            role='Developer',
            experience_level='Mid'
        )
        assert 'user1' in app.applied_jobs
        assert len(app.applied_jobs['user1']) == 1
        assert app.applied_jobs['user1'][0]['employer'] == 'Company A'

def test_apply_for_job_nonexistent_user(app):
    
    username = 'new_user'
    app.apply_for_job(
        username=username,
        job_title='QA Engineer',
        job_description='Quality assurance engineering tasks',
        employer='Company C',
        location='Location C',
        salary=70000,
        role='QA',
        experience_level='Mid'
    )
    assert username in app.applied_jobs
    assert len(app.applied_jobs[username]) == 1

def test_save_job_updates_saved_jobs(app):
    
    with patch.object(app, 'saved_jobs', new={}):
        app.save_job(
            username='user2',
            job_title='Designer',
            job_description='Design stuff',
            employer='Company B',
            location='Location B',
            salary=60000,
            role='Designer',
            experience_level='Senior'
        )
        assert 'user2' in app.saved_jobs
        assert len(app.saved_jobs['user2']) == 1
        assert app.saved_jobs['user2'][0]['employer'] == 'Company B'

def test_save_job_for_existing_user(app):
    
    username = 'existing_user'
    app.saved_jobs[username] = [
        {'title': 'Existing Job', 'employer': 'Existing Company'}
    ]
    app.save_job(
        username=username,
        job_title='New Job',
        job_description='New job description',
        employer='New Company',
        location='New Location',
        salary=80000,
        role='New Role',
        experience_level='New Level'
    )
    assert len(app.saved_jobs[username]) == 2
    assert app.saved_jobs[username][1]['title'] == 'New Job'

def test_calculate_jobs_not_applied(app):
    
    app.job_posts = [{'id': 1}]
    app.all_jobs = {1: {'details': 'Details of Job 1'}, 2: {'details': 'Details of Job 2'}}
    with patch.object(app, 'apply_for_job') as mocked_apply:
        app.apply_for_job(
            username='user1',
            job_title='Developer',
            job_description='Develop stuff',
            employer='Company A',
            location='Location A',
            salary=50000,
            role='Developer',
            experience_level='Mid'
        )
    jobs_not_applied = app.calculate_jobs_not_applied()
    assert len(jobs_not_applied) == 1

def test_calculate_jobs_not_applied_with_no_applications(app):
    app.all_jobs = {
        1: {'details': 'Details of Job 1'},
        2: {'details': 'Details of Job 2'}
    }
    # Assuming no jobs have been applied for
    app.job_posts = []
    jobs_not_applied = app.calculate_jobs_not_applied()
    assert len(jobs_not_applied) == len(app.all_jobs)
