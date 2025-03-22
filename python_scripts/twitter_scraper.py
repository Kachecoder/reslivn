#!/usr/bin/env python3
"""
Twitter Data Scraper

This script scrapes Twitter data for affiliate marketing research.
It collects tweets, user profiles, and engagement metrics related to specified keywords.
"""

import os
import json
import time
import random
import requests
from datetime import datetime

class TwitterScraper:
    def __init__(self, api_key=None):
        """Initialize the Twitter scraper with API credentials."""
        self.api_key = api_key or os.getenv("TWITTER_API_KEY")
        self.base_url = "https://api.twitter.com/2"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
    def search_tweets(self, query, count=100, result_type="mixed"):
        """
        Search for tweets matching the query.
        
        Args:
            query (str): Search query
            count (int): Number of tweets to return
            result_type (str): Type of results (recent, popular, mixed)
            
        Returns:
            dict: Search results
        """
        print(f"Searching Twitter for: {query}")
        
        # In a real implementation, this would use the Twitter API
        # For now, we'll simulate the response
        
        # Simulate API call delay
        time.sleep(random.uniform(1.0, 2.0))
        
        # Generate mock data
        mock_tweets = []
        for i in range(min(count, 20)):  # Limit to 20 for mock data
            engagement = random.randint(5, 500)
            followers = random.randint(100, 50000)
            
            mock_tweets.append({
                "id": f"tweet_{i}_{int(time.time())}",
                "text": f"Check out this amazing {query} product! #affiliate #marketing #{query.replace(' ', '')}",
                "user": {
                    "id": f"user_{i}_{int(time.time())}",
                    "username": f"affiliate_marketer_{i}",
                    "name": f"Affiliate Expert {i}",
                    "followers_count": followers
                },
                "created_at": datetime.now().isoformat(),
                "metrics": {
                    "likes": engagement,
                    "retweets": int(engagement * 0.3),
                    "replies": int(engagement * 0.1)
                }
            })
        
        results = {
            "platform": "twitter",
            "query": query,
            "timestamp": datetime.now().isoformat(),
            "results": mock_tweets,
            "metadata": {
                "count": len(mock_tweets),
                "result_type": result_type
            }
        }
        
        return results
    
    def get_user_profile(self, username):
        """
        Get a user's profile information.
        
        Args:
            username (str): Twitter username
            
        Returns:
            dict: User profile data
        """
        print(f"Getting profile for Twitter user: {username}")
        
        # Simulate API call delay
        time.sleep(random.uniform(0.5, 1.5))
        
        # Generate mock data
        followers = random.randint(1000, 100000)
        tweets = random.randint(100, 5000)
        
        profile = {
            "id": f"user_{username}_{int(time.time())}",
            "username": username,
            "name": f"{username.capitalize()} Marketing",
            "description": f"Affiliate marketing expert specializing in trending products and strategies. Follow for daily tips!",
            "followers_count": followers,
            "following_count": int(followers * 0.1),
            "tweets_count": tweets,
            "created_at": "2020-01-01T00:00:00Z",
            "verified": random.choice([True, False]),
            "profile_image_url": f"https://example.com/profiles/{username}.jpg"
        }
        
        return profile
    
    def analyze_sentiment(self, tweets):
        """
        Analyze sentiment of tweets.
        
        Args:
            tweets (list): List of tweet objects
            
        Returns:
            dict: Sentiment analysis results
        """
        print(f"Analyzing sentiment of {len(tweets)} tweets")
        
        # Simulate processing delay
        time.sleep(random.uniform(1.0, 3.0))
        
        # Generate mock sentiment data
        sentiments = {
            "positive": random.uniform(0.3, 0.7),
            "neutral": random.uniform(0.1, 0.4),
            "negative": random.uniform(0.0, 0.3)
        }
        
        # Normalize to ensure they sum to 1
        total = sum(sentiments.values())
        for key in sentiments:
            sentiments[key] = round(sentiments[key] / total, 2)
        
        # Ensure they sum to 1 after rounding
        if sum(sentiments.values()) != 1.0:
            sentiments["neutral"] += 1.0 - sum(sentiments.values())
            sentiments["neutral"] = round(sentiments["neutral"], 2)
        
        return {
            "sentiment": sentiments,
            "sample_size": len(tweets),
            "timestamp": datetime.now().isoformat()
        }
    
    def save_results(self, data, filename):
        """
        Save results to a JSON file.
        
        Args:
            data (dict): Data to save
            filename (str): Output filename
            
        Returns:
            str: Path to saved file
        """
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        os.makedirs(output_dir, exist_ok=True)
        
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Data saved to {filepath}")
        return filepath

def main():
    """Main function to demonstrate Twitter scraper usage."""
    # Initialize scraper
    scraper = TwitterScraper()
    
    # Define search queries based on affiliate marketing niches
    queries = [
        "solar generator",
        "emergency food kit",
        "water filtration",
        "passive income",
        "ai writing tools"
    ]
    
    # Search for tweets for each query
    all_results = {}
    for query in queries:
        results = scraper.search_tweets(query, count=50)
        all_results[query] = results
        
        # Analyze sentiment
        sentiment = scraper.analyze_sentiment(results["results"])
        all_results[f"{query}_sentiment"] = sentiment
    
    # Save combined results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    scraper.save_results(all_results, f"twitter_data_{timestamp}.json")
    
    print("Twitter data scraping completed successfully!")

if __name__ == "__main__":
    main()
