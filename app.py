# app.py

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load tweet data from the JSON file
with open('tweets.json', 'r') as file:
    tweets_data = json.load(file)

# 2.) Hello World at the base URL
@app.route('/')
def hello_world():
    return 'Hello World!'

# 3.) GET endpoint to return ALL tweets
@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    return jsonify(tweets_data)

# 4.) Modify the above endpoint to filter tweets using a query parameter
@app.route('/tweets_filtered', methods=['GET'])
def get_filtered_tweets():
    keyword = request.args.get('keyword')
    filtered_tweets = [tweet for tweet in tweets_data if keyword.lower() in tweet['text'].lower()]
    return jsonify(filtered_tweets)

# 5.) GET endpoint for a specific tweet by ID
@app.route('/tweet/<int:tweet_id>', methods=['GET'])
def get_tweet_by_id(tweet_id):
    try:
        tweet = next(tweet for tweet in tweets_data if tweet['id'] == tweet_id)
        return jsonify(tweet)
    except StopIteration:
        return jsonify({'error': 'Tweet not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# 6.) Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

# 7.) Curl requests to test endpoints:
"""
# Hello World
curl http://localhost:5000/

# Get all tweets
curl http://localhost:5000/tweets

# Get filtered tweets
curl http://localhost:5000/tweets_filtered?keyword=winter

# Get tweet by ID (replace 1 with the desired tweet ID)
curl http://localhost:5000/tweet/1
"""