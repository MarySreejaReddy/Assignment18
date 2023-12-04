import json
from main import app

client = app.test_client()

def test_create_tweet_success():
    response = client.post('/tweets', json={'text': 'This is a new tweet', 'user': 'test_user'})
    assert response.status_code == 201  
    #assert 'id' in response.get_json()

def test_create_tweet_failure():
    response = client.post('/tweets', json={})
    assert response.status_code == 400  

def test_create_tweet_missing_user():
    response = client.post('/tweets', json={'text': 'This is a new tweet'})
    assert response.status_code == 400