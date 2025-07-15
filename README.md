# 🐦 Twitter Bot using Python & Tweepy

This project is a simple Twitter bot built using **Python** and the **Tweepy** library. It can be extended to perform various automated tasks like posting tweets, liking, retweeting, and following users — all from your own Twitter developer account.

---

## 🚀 Features

- ✅ Post tweets from your Python script  
- ✅ Secure credential handling using `.gitignore`  
- ✅ Modular file structure  
- ✅ Beginner-friendly and customizable  

---

## 📁 Project Structure

```
Twitter-Bot/
├── twitterbot_post_tweet.py       # Main script to post tweets
├── credentials_template.py        # Sample credentials file (safe to share)
├── .gitignore                     # Prevents sensitive files from being uploaded
```

---

## 🔐 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/pihu-4454/Twitter-Bot.git
cd Twitter-Bot
```

### 2. Install Dependencies
```
pip install tweepy
```

### 3. Add Your Twitter API Credentials
```
cp credentials_template.py credentials.py
```

Then edit credentials.py with your real tokens:
```
consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-secret'
access_token = 'your-access-token'
access_token_secret = 'your-access-token-secret'
```

### 🧪 Running the Bot
```
python twitterbot_post_tweet.py
```

### ✨ Author
Swathi Sahani
GitHub: @pihu-4454




