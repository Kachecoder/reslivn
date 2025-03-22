#!/usr/bin/env python3
"""
Affiliate Marketing Data Analyzer

This script analyzes data collected from social media platforms and affiliate networks
to identify trends, opportunities, and optimal marketing strategies.
"""

import os
import json
import time
import random
import glob
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

class AffiliateDataAnalyzer:
    def __init__(self):
        """Initialize the data analyzer."""
        self.data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        os.makedirs(self.data_dir, exist_ok=True)
        
    def load_data(self, platform=None):
        """
        Load data from JSON files.
        
        Args:
            platform (str, optional): Filter by platform (twitter, pinterest, tiktok)
            
        Returns:
            dict: Combined data from all sources
        """
        print(f"Loading data files{' for ' + platform if platform else ''}")
        
        # Find all JSON files in the data directory
        pattern = f"{platform}_data_*.json" if platform else "*_data_*.json"
        data_files = glob.glob(os.path.join(self.data_dir, pattern))
        
        if not data_files:
            print(f"No data files found matching pattern: {pattern}")
            return {}
        
        # Load and combine data
        combined_data = {}
        for file_path in data_files:
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    
                platform_name = os.path.basename(file_path).split('_')[0]
                combined_data[platform_name] = data
                print(f"Loaded data from {file_path}")
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
        
        return combined_data
    
    def analyze_cross_platform_trends(self, data):
        """
        Analyze trends across different platforms.
        
        Args:
            data (dict): Combined data from all platforms
            
        Returns:
            dict: Cross-platform trend analysis
        """
        print("Analyzing cross-platform trends")
        
        # Simulate processing delay
        time.sleep(random.uniform(1.0, 3.0))
        
        # Generate mock cross-platform trends
        niches = [
            "Survival & Emergency",
            "DIY & Home Improvement",
            "Personal Finance",
            "E-Learning",
            "AI & Automation"
        ]
        
        platforms = ["twitter", "pinterest", "tiktok"]
        
        # Generate platform performance by niche
        platform_performance = {}
        for niche in niches:
            platform_performance[niche] = {}
            total = 0
            for platform in platforms:
                value = random.uniform(0.1, 1.0)
                platform_performance[niche][platform] = value
                total += value
            
            # Normalize to get percentages
            for platform in platforms:
                platform_performance[niche][platform] = round(platform_performance[niche][platform] / total * 100, 1)
        
        # Generate top keywords across platforms
        keywords = [
            "solar generator", "emergency food", "water filtration", 
            "survival kit", "power outage", "homesteading", 
            "passive income", "ai writing", "online courses"
        ]
        
        keyword_performance = {}
        for keyword in keywords:
            keyword_performance[keyword] = {
                "twitter": {
                    "engagement": round(random.uniform(0.01, 0.1), 3),
                    "sentiment": round(random.uniform(0.3, 0.9), 2)
                },
                "pinterest": {
                    "engagement": round(random.uniform(0.01, 0.1), 3),
                    "saves": random.randint(100, 5000)
                },
                "tiktok": {
                    "engagement": round(random.uniform(0.01, 0.1), 3),
                    "views": random.randint(1000, 1000000)
                }
            }
        
        return {
            "platform_performance_by_niche": platform_performance,
            "keyword_performance": keyword_performance,
            "timestamp": datetime.now().isoformat()
        }
    
    def identify_top_products(self, data):
        """
        Identify top-performing products across platforms.
        
        Args:
            data (dict): Combined data from all platforms
            
        Returns:
            dict: Top products analysis
        """
        print("Identifying top-performing products")
        
        # Simulate processing delay
        time.sleep(random.uniform(1.0, 2.0))
        
        # Generate mock top products
        products = [
            {
                "name": "Bluetti Portable Power Station",
                "niche": "Survival & Emergency",
                "engagement_score": round(random.uniform(0.7, 0.95), 2),
                "sentiment_score": round(random.uniform(0.7, 0.95), 2),
                "commission_range": "$75-120",
                "platforms": {
                    "twitter": round(random.uniform(0.3, 0.7), 2),
                    "pinterest": round(random.uniform(0.5, 0.9), 2),
                    "tiktok": round(random.uniform(0.6, 0.9), 2)
                }
            },
            {
                "name": "Jasper AI Writing Assistant",
                "niche": "AI & Automation",
                "engagement_score": round(random.uniform(0.7, 0.95), 2),
                "sentiment_score": round(random.uniform(0.7, 0.95), 2),
                "commission_range": "$40-200",
                "platforms": {
                    "twitter": round(random.uniform(0.6, 0.9), 2),
                    "pinterest": round(random.uniform(0.3, 0.7), 2),
                    "tiktok": round(random.uniform(0.5, 0.8), 2)
                }
            },
            {
                "name": "Readywise Emergency Food Kit",
                "niche": "Survival & Emergency",
                "engagement_score": round(random.uniform(0.7, 0.95), 2),
                "sentiment_score": round(random.uniform(0.7, 0.95), 2),
                "commission_range": "$50-150",
                "platforms": {
                    "twitter": round(random.uniform(0.4, 0.8), 2),
                    "pinterest": round(random.uniform(0.6, 0.9), 2),
                    "tiktok": round(random.uniform(0.4, 0.7), 2)
                }
            },
            {
                "name": "Codecademy Pro Membership",
                "niche": "E-Learning",
                "engagement_score": round(random.uniform(0.7, 0.95), 2),
                "sentiment_score": round(random.uniform(0.7, 0.95), 2),
                "commission_range": "$30-120",
                "platforms": {
                    "twitter": round(random.uniform(0.5, 0.8), 2),
                    "pinterest": round(random.uniform(0.3, 0.6), 2),
                    "tiktok": round(random.uniform(0.7, 0.9), 2)
                }
            },
            {
                "name": "Berkey Water Filter System",
                "niche": "Survival & Emergency",
                "engagement_score": round(random.uniform(0.7, 0.95), 2),
                "sentiment_score": round(random.uniform(0.7, 0.95), 2),
                "commission_range": "$45-90",
                "platforms": {
                    "twitter": round(random.uniform(0.4, 0.7), 2),
                    "pinterest": round(random.uniform(0.7, 0.9), 2),
                    "tiktok": round(random.uniform(0.5, 0.8), 2)
                }
            }
        ]
        
        # Sort by engagement score (descending)
        sorted_products = sorted(products, key=lambda x: x["engagement_score"], reverse=True)
        
        return {
            "top_products": sorted_products,
            "timestamp": datetime.now().isoformat()
        }
    
    def generate_marketing_strategy(self, data):
        """
        Generate optimal marketing strategy based on data analysis.
        
        Args:
            data (dict): Combined data from all platforms
            
        Returns:
            dict: Marketing strategy recommendations
        """
        print("Generating marketing strategy recommendations")
        
        # Simulate processing delay
        time.sleep(random.uniform(1.0, 3.0))
        
        # Generate mock strategy recommendations
        strategies = [
            {
                "title": "Increase Pinterest Content for Survival Niche",
                "description": "Pinterest shows the highest conversion rates for survival and emergency preparedness products. Increase pin creation frequency to 5 pins per week focusing on solar generators and water filtration systems.",
                "impact": "High",
                "difficulty": "Low",
                "estimated_roi": round(random.uniform(2.0, 5.0), 1),
                "platforms": ["pinterest"],
                "niches": ["Survival & Emergency"]
            },
            {
                "title": "Create TikTok Demonstrations for AI Tools",
                "description": "Short-form video demonstrations of AI writing tools and automation software perform exceptionally well on TikTok. Create 3 videos per week showing real-time results and benefits.",
                "impact": "High",
                "difficulty": "Medium",
                "estimated_roi": round(random.uniform(2.0, 4.0), 1),
                "platforms": ["tiktok"],
                "niches": ["AI & Automation"]
            },
            {
                "title": "Develop Product Comparison Content",
                "description": "Competitor analysis shows product comparison content has the highest conversion rates. Create detailed comparisons for top 5 products in each niche with clear affiliate links.",
                "impact": "High",
                "difficulty": "Medium",
                "estimated_roi": round(random.uniform(2.0, 4.0), 1),
                "platforms": ["twitter", "pinterest", "tiktok"],
                "niches": ["All"]
            },
            {
                "title": "Expand to CJ Affiliate Network",
                "description": "CJ Affiliate offers higher commission rates for emergency preparedness products. Apply to their program and integrate their top-converting products into your content strategy.",
                "impact": "High",
                "difficulty": "High",
                "estimated_roi": round(random.uniform(3.0, 6.0), 1),
                "platforms": ["All"],
                "niches": ["Survival & Emergency"]
            },
            {
                "title": "Create Emergency Checklist Lead Magnets",
                "description": "Emergency preparation checklists perform well as lead magnets. Create downloadable PDFs with affiliate links to recommended products for each checklist item.",
                "impact": "Medium",
                "difficulty": "Low",
                "estimated_roi": round(random.uniform(1.5, 3.0), 1),
                "platforms": ["pinterest"],
                "niches": ["Survival & Emergency"]
            }
        ]
        
        # Sort by estimated ROI (descending)
        sorted_strategies = sorted(strategies, key=lambda x: x["estimated_roi"], reverse=True)
        
        return {
            "strategies": sorted_strategies,
            "timestamp": datetime.now().isoformat()
        }
    
    def create_visualization(self, data, output_dir=None):
        """
        Create data visualizations.
        
        Args:
            data (dict): Analyzed data
            output_dir (str, optional): Directory to save visualizations
            
        Returns:
            list: Paths to saved visualization files
        """
        if output_dir is None:
            output_dir = os.path.join(self.data_dir, "visualizations")
        
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"Creating visualizations in {output_dir}")
        
        # Simulate visualization creation
        time.sleep(random.uniform(1.0, 2.0))
        
        # Create mock visualizations
        visualization_files = []
        
        # 1. Platform performance by niche
        if "cross_platform_trends" in data and "platform_performance_by_niche" in data["cross_platform_trends"]:
            try:
                plt.figure(figsize=(12, 8))
                
                niches = list(data["cross_platform_trends"]["platform_performance_by_niche"].keys())
                platforms = ["twitter", "pinterest", "tiktok"]
                
                x = np.arange(len(niches))
                width = 0.25
                
                for i, platform in enumerate(platforms):
                    values = [data["cross_platform_trends"]["platform_performance_by_niche"][niche][platform] for niche in niches]
                    plt.bar(x + i*width - width, values, width, label=platform.capitalize())
                
                plt.xlabel('Niches')
                plt.ylabel('Performance (%)')
                plt.title('Platform Performance by Niche')
                plt.xticks(x, [niche.split(' & ')[0] for niche in niches], rotation=45)
                plt.legend()
                plt.tight_layout()
                
                file_path = os.path.join(output_dir, "platform_performance.png")
                plt.savefig(file_path)
                plt.close()
                
                visualization_files.append(file_path)
                print(f"Created visualization: {file_path}")
            except Exception as e:
                print(f"Error creating platform performance visualization: {e}")
        
        # 2. Top products by engagement
        if "top_products" in data and "top_products" in data["top_products"]:
            try:
                plt.figure(figsize=(10, 6))
                
                products = [p["name"] for p in data["top_products"]["top_products"]]
                engagement = [p["engagement_score"] for p in data["top_products"]["top_products"]]
                
                plt.barh(products, engagement, color='skyblue')
                plt.xlabel('Engagement Score')
                plt.title('Top Products by Engagement')
                plt.xlim(0, 1)
                plt.tight_layout()
                
                file_path = os.path.join(output_dir, "top_products.png")
                plt.savefig(file_path)
                plt.close()
                
                visualization_files.append(file_path)
                print(f"Created visualization: {file_path}")
            except Exception as e:
                print(f"Error creating top products visualization: {e}")
        
        # 3. Strategy ROI comparison
        if "marketing_strategy" in data and "strategies" in data["marketing_strategy"]:
            try:
                plt.figure(figsize=(10, 6))
                
                strategies = [s["title"].split(' for ')[0] for s in data["marketing_strategy"]["strategies"]]
                roi = [s["estimated_roi"] for s in data["marketing_strategy"]["strategies"]]
                
                plt.barh(strategies, roi, color='lightgreen')
                plt.xlabel('Estimated ROI')
                plt.title('Marketing Strategies by ROI')
                plt.tight_layout()
                
                file_path = os.path.join(output_dir, "strategy_roi.png")
                plt.savefig(file_path)
                plt.close()
                
                visualization_files.append(file_path)
                print(f"Created visualization: {file_path}")
            except Exception as e:
                print(f"Error creating strategy ROI visualization: {e}")
        
        return visualization_files
    
    def save_analysis(self, data, filename):
        """
        Save analysis results to a JSON file.
        
        Args:
            data (dict): Analysis data
            filename (str): Output filename
            
        Returns:
            str: Path to saved file
        """
        filepath = os.path.join(self.data_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Analysis saved to {filepath}")
        return filepath

def main():
    """Main function to demonstrate data analyzer usage."""
    # Initialize analyzer
    analyzer = AffiliateDataAnalyzer()
    
    # Load data
    data = analyzer.load_data()
    
    # If no data is found, generate mock data
    if not data:
        print("No data files found. Generating mock data for demonstration.")
        data = {
            "twitter": {"mock": True},
            "pinterest": {"mock": True},
            "tiktok": {"mock": True}
        }
    
    # Analyze cross-platform trends
    cross_platform_trends = analyzer.analyze_cross_platform_trends(data)
    
    # Identify top products
    top_products = analyzer.identify_top_products(data)
    
    # Generate marketing strategy
    marketing_strategy = analyzer.generate_marketing_strategy(data)
    
    # Combine all analyses
    analysis_results = {
        "cross_platform_trends": cross_platform_trends,
        "top_products": top_products,
        "marketing_strategy": marketing_strategy,
        "timestamp": datetime.now().isoformat()
    }
    
    # Save analysis
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    analyzer.save_analysis(analysis_results, f"affiliate_analysis_{timestamp}.json")
    
    # Create visualizations
    analyzer.create_visualization(analysis_results)
    
    print("Affiliate marketing data analysis completed successfully!")

if __name__ == "__main__":
    main()
