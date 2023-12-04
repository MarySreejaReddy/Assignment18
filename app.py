from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load or initialize tweets
try:
    with open('100tweets.json') as f:
        tweets = json.load(f)
except FileNotFoundError:
    tweets = []

# Save tweets to a JSON file
def save_tweets():
    with open('100tweets.json', 'w') as outfile:
        json.dump(tweets, outfile, indent=2)

# Endpoint to return "Hello World"
@app.route('/')
def hello_world():
    return 'Hello World.'

# Endpoint to return all tweets
@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    return jsonify(tweets)

# Endpoint to filter tweets based on a hashtag
@app.route('/tweets_filtered', methods=['GET'])
def get_filtered_tweets():
    try:
        hashtag = request.args.get('hashtag')
        if hashtag is None:
            raise ValueError("Missing 'hashtag' parameter")
        
        filtered_tweets = [tweet for tweet in tweets if hashtag.lower() in tweet.get('hashtags', '').lower()]
        return jsonify(filtered_tweets)
    except ValueError as e:
        return str(e), 400  # Bad Request

# Endpoint to return a specific tweet by ID
@app.route('/tweet/<int:tweet_id>', methods=['GET'])
def get_tweet_by_id(tweet_id):
    try:
        tweet = next((t for t in tweets if t['id_str'] == tweet_id), None)
        if tweet:
            return jsonify(tweet)
        else:
            raise ValueError("Tweet not found")
    except ValueError as e:
        return str(e), 404  # Not Found

if __name__ == '__main__':
    app.run(debug=True)

#My curl commands
#curl http://localhost:5000/          (returns the message "Hello World.")
#curl http://localhost:5000/tweets    (returns ALL of the tweets)
#curl http://localhost:5000/tweets_filtered?hashtag=THEkarliehustle    (the tweets returned by a hashtag query parameter)
#curl http://localhost:5000/tweet/1360000000000000000    (returns the JSON data for that particular id tweet)
