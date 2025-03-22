#!/usr/bin/env python3
"""
TikTok Data Scraper

This script scrapes TikTok data for affiliate marketing research.
It collects videos, user profiles, and engagement metrics related to specified keywords.
"""

import os
import json
import time
import random
import requests
from datetime import datetime

class TikTokScraper:
    def __init__(self, api_key=None):
        """Initialize the TikTok scraper with API credentials."""
        self.api_key = api_key or os.getenv("TIKTOK_API_KEY")
        self.base_url = "https://api.tiktok.com/v2"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
    def search_videos(self, query, count=100):
        """
        Search for videos matching the query.
        
        Args:
            query (str): Search query
            count (int): Number of videos to return
            
        Returns:
            dict: Search results
        """
        print(f"Searching TikTok for: {query}")
        
        # In a real implementation, this would use the TikTok API
        # For now, we'll simulate the response
        
        # Simulate API call delay
        time.sleep(random.uniform(1.0, 2.0))
        
        # Generate mock data
        mock_videos = []
        for i in range(min(count, 20)):  # Limit to 20 for mock data
            views = random.randint(1000, 1000000)
            likes = int(views * random.uniform(0.05, 0.2))
            comments = int(likes * random.uniform(0.01, 0.1))
            shares = int(likes * random.uniform(0.01, 0.05))
            
            mock_videos.append({
                "id": f"video_{i}_{int(time.time())}",
                "description": f"Check out this amazing {query} review! #affiliate #marketing #{query.replace(' ', '')}",
                "video_url": f"https://example.com/tiktok/{query.replace(' ', '-')}-{i}.mp4",
                "thumbnail_url": f"https://example.com/thumbnails/{query.replace(' ', '-')}-{i}.jpg",
                "creator": {
                    "id": f"user_{i}_{int(time.time())}",
                    "username": f"tiktok_marketer_{i}",
                    "name": f"TikTok Expert {i}",
                    "followers": random.randint(1000, 1000000)
                },
                "metrics": {
                    "views": views,
                    "likes": likes,
                    "comments": comments,
                    "shares": shares
                },
                "created_at": datetime.now().isoformat(),
                "duration": random.randint(15, 60)
            })
        
        results = {
            "platform": "tiktok",
            "query": query,
            "timestamp": datetime.now().isoformat(),
            "results": mock_videos,
            "metadata": {
                "count": len(mock_videos)
            }
        }
        
        return results
    
    def get_user_profile(self, username):
        """
        Get a user's profile information.
        
        Args:
            username (str): TikTok username
            
        Returns:
            dict: User profile data
        """
        print(f"Getting profile for TikTok user: {username}")
        
        # Simulate API call delay
        time.sleep(random.uniform(0.5, 1.5))
        
        # Generate mock data
        followers = random.randint(1000, 5000000)
        videos = random.randint(50, 500)
        
        profile = {
            "id": f"user_{username}_{int(time.time())}",
            "username": username,
            "name": f"{username.capitalize()} TikTok",
            "bio": f"Affiliate marketing expert sharing product reviews and tips. Follow for daily content!",
            "followers_count": followers,
            "following_count": int(followers * 0.1),
            "likes_count": followers * random.randint(1, 10),
            "videos_count": videos,
            "created_at": "2020-01-01T00:00:00Z",
            "verified": random.choice([True, False]),
            "profile_image_url": f"https://example.com/profiles/{username}.jpg"
        }
        
        return profile
    
    def analyze_engagement(self, videos):
        """
        Analyze engagement metrics of videos.
        
        Args:
            videos (list): List of video objects
            
        Returns:
            dict: Engagement analysis results
        """
        print(f"Analyzing engagement of {len(videos)} videos")
        
        # Simulate processing delay
        time.sleep(random.uniform(1.0, 3.0))
        
        # Calculate average engagement metrics
        total_views = sum(video["metrics"]["views"] for video in videos)
        total_likes = sum(video["metrics"]["likes"] for video in videos)
        total_comments = sum(video["metrics"]["comments"] for video in videos)
        total_shares = sum(video["metrics"]["shares"] for video in videos)
        
        avg_views = total_views / len(videos) if videos else 0
        avg_likes = total_likes / len(videos) if videos else 0
        avg_comments = total_comments / len(videos) if videos else 0
        avg_shares = total_shares / len(videos) if videos else 0
        
        # Calculate engagement rates
        engagement_rate = (total_likes + total_comments + total_shares) / total_views if total_views else 0
        
        # Generate time-based engagement patterns
        time_patterns = {
            "morning": random.uniform(0.1, 0.4),
            "afternoon": random.uniform(0.2, 0.5),
            "evening": random.uniform(0.3, 0.6),
            "night": random.uniform(0.1, 0.3)
        }
        
        # Normalize to ensure they sum to 1
        total = sum(time_patterns.values())
        for key in time_patterns:
            time_patterns[key] = round(time_patterns[key] / total, 2)
        
        # Ensure they sum to 1 after rounding
        if sum(time_patterns.values()) != 1.0:
            time_patterns["evening"] += 1.0 - sum(time_patterns.values())
            time_patterns["evening"] = round(time_patterns["evening"], 2)
        
        return {
            "average_metrics": {
                "views": int(avg_views),
                "likes": int(avg_likes),
                "comments": int(avg_comments),
                "shares": int(avg_shares)
            },
            "engagement_rate": round(engagement_rate * 100, 2),  # as percentage
            "time_patterns": time_patterns,
            "sample_size": len(videos),
            "timestamp": datetime.now().isoformat()
        }
    
    def identify_trending_hashtags(self, videos):
        """
        Identify trending hashtags from videos.
        
        Args:
            videos (list): List of video objects
            
        Returns:
            dict: Trending hashtags analysis
        """
        print(f"Identifying trending hashtags from {len(videos)} videos")
        
        # Simulate processing delay
        time.sleep(random.uniform(1.0, 2.0))
        
        # Generate mock trending hashtags
        hashtags = [
            "affiliate", "marketing", "solarpower", "emergencyprep",
            "survival", "passiveincome", "aitools", "homeimprovement",
            "diy", "prepping", "financetips", "onlinecourses"
        ]
        
        trending_hashtags = {}
        for hashtag in hashtags:
            trending_hashtags[hashtag] = {
                "count": random.randint(5, len(videos)),
                "engagement_rate": round(random.uniform(0.01, 0.1), 3),
                "growth": round(random.uniform(-0.1, 0.5), 2)
            }
        
        # Sort by count (descending)
        sorted_hashtags = {k: v for k, v in sorted(
            trending_hashtags.items(), 
            key=lambda item: item[1]["count"], 
            reverse=True
        )}
        
        return {
            "trending_hashtags": sorted_hashtags,
            "sample_size": len(videos),
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
    """Main function to demonstrate TikTok scraper usage."""
    # Initialize scraper
    scraper = TikTokScraper()
    
    # Define search queries based on affiliate marketing niches
    queries = [
        "solar generator",
        "emergency food kit",
        "water filtration",
        "passive income",
        "ai writing tools"
    ]
    
    # Search for videos for each query
    all_results = {}
    all_videos = []
    
    for query in queries:
        results = scraper.search_videos(query, count=50)
        all_results[query] = results
        all_videos.extend(results["results"])
    
    # Analyze engagement
    engagement = scraper.analyze_engagement(all_videos)
    all_results["engagement_analysis"] = engagement
    
    # Identify trending hashtags
    hashtags = scraper.identify_trending_hashtags(all_videos)
    all_results["trending_hashtags"] = hashtags
    
    # Save combined results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    scraper.save_results(all_results, f"tiktok_data_{timestamp}.json")
    
    print("TikTok data scraping completed successfully!")

if __name__ == "__main__":
    main()
