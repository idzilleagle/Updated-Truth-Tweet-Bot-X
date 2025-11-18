import tweepy
import random
import os
from dotenv import load_dotenv

# This command loads the keys from your .env file
load_dotenv()

# Securely access the keys from the environment
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# --- CORE TWEET COMPONENTS ---
URL = "https://legalnamefraud.carrd.co"
BASE_HASHTAGS = "#BCCRSS #legalnamefraud #truthbillboards #crssnow #judgebows"

# --- TWEET VARIATION POOLS ---
OPENERS = [
    "The truth is simple:", "Quick reminder:", "They don't want you to know this:",
    "Did you know?", "Here's a thought for your day:", "Unplug from the matrix:",
    "Consider this:", "The system is based on this deception:", "Fact check this:",
    "It's hidden in plain sight:", "Time to wake up.", "Here's the truth:",
]
CORE_STATEMENTS = [
    "It's illegal to use a legal name.", "The legal name is crown copyright property.",
    "Using a legal name is participating in fraud.", "You are not a legal name.",
    "A birth certificate creates a dead corporate fiction, legal name.",
    "The legal name is the mark of the beast.", "Slavery by consent is still slavery.",
]
CALLS_TO_ACTION = [
    "Read the #BCCRSS to understand.", "Share this with everyone.",
    "Learn the facts, break the spell.", "Read and share the #BCCRSS.",
    "Remove your consent by understanding the fraud.", "Go to the website and learn more.",
]

def generate_tweet_text():
    """
    Generates a unique, length-compliant tweet from the component pools.
    This function is now simplified as we are not adding a trending hashtag.
    """
    while True:
        # Pick one component from each list to ensure variety
        components = [random.choice(OPENERS), random.choice(CORE_STATEMENTS), random.choice(CALLS_TO_ACTION)]
        random.shuffle(components)
        
        # Use 2 or 3 random components for the main message
        message = " ".join(components[:random.randint(2,3)])

        # Assemble the full tweet
        full_tweet = f"{message} {URL} {BASE_HASHTAGS}"
        
        # This check is still good practice, though less likely to fail now
        if len(full_tweet) <= 280:
            return full_tweet

def post_tweet():
    """Authenticates and posts a single tweet."""
    if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
        print("❌ ERROR: Missing Twitter credentials in .env file.")
        return
    try:
        print("Authenticating with Twitter network...")
        client = tweepy.Client(
            consumer_key=API_KEY, consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
        )
        print("Authentication successful.")

        # Generate the final tweet text. No extra steps needed.
        tweet_text = generate_tweet_text()
        
        print(f"\nBroadcasting this transmission:\n---\n{tweet_text}\n---")
        
        # Post the tweet
        response = client.create_tweet(text=tweet_text)
        print(f"✅ Transmission successful. Signal ID: {response.data['id']}")
        
    except Exception as e:
        print(f"❌ An error occurred during transmission: {e}")

if __name__ == "__main__":
    post_tweet()
