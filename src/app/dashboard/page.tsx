import React from 'react';

export default function DashboardPage() {
  return (
    <div className="space-y-8">
      <section>
        <h1 className="text-3xl font-bold mb-4">Dashboard</h1>
        <p className="text-gray-600 dark:text-gray-300 mb-6">
          Welcome to your Affiliate Marketing AI Agent dashboard. Here you can monitor your data collection,
          trend analysis, competitor research, and progress toward your $10,000 monthly income goal.
        </p>
      </section>
      
      <section className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-2">Income Progress</h3>
          <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded-full mb-2">
            <div className="h-4 bg-blue-600 rounded-full" style={{ width: '35%' }}></div>
          </div>
          <p className="text-sm text-gray-500 dark:text-gray-400">$3,500 of $10,000 monthly goal</p>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-2">Top Performing Niche</h3>
          <p className="text-xl font-bold text-blue-600 mb-1">Survival & Emergency</p>
          <p className="text-sm text-gray-500 dark:text-gray-400">42% of total revenue</p>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-2">Active Campaigns</h3>
          <p className="text-xl font-bold text-blue-600 mb-1">12</p>
          <p className="text-sm text-gray-500 dark:text-gray-400">Across 5 target niches</p>
        </div>
      </section>
      
      <section className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
        <h3 className="text-lg font-semibold mb-4">Recent Activity</h3>
        <div className="space-y-3">
          <div className="flex items-center justify-between pb-2 border-b border-gray-100 dark:border-gray-700">
            <div>
              <p className="font-medium">New trend detected: Solar generators</p>
              <p className="text-sm text-gray-500 dark:text-gray-400">Survival & Emergency niche</p>
            </div>
            <span className="text-sm text-gray-500 dark:text-gray-400">2 hours ago</span>
          </div>
          
          <div className="flex items-center justify-between pb-2 border-b border-gray-100 dark:border-gray-700">
            <div>
              <p className="font-medium">Competitor analysis completed</p>
              <p className="text-sm text-gray-500 dark:text-gray-400">5 new competitors identified</p>
            </div>
            <span className="text-sm text-gray-500 dark:text-gray-400">5 hours ago</span>
          </div>
          
          <div className="flex items-center justify-between pb-2 border-b border-gray-100 dark:border-gray-700">
            <div>
              <p className="font-medium">Pinterest data scraping completed</p>
              <p className="text-sm text-gray-500 dark:text-gray-400">1,250 pins analyzed</p>
            </div>
            <span className="text-sm text-gray-500 dark:text-gray-400">1 day ago</span>
          </div>
        </div>
      </section>
      
      <section className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4">Top Products</h3>
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <p className="font-medium">Emergency Food Kit (30-day)</p>
              <p className="font-bold text-green-600">$1,200</p>
            </div>
            <div className="flex items-center justify-between">
              <p className="font-medium">Solar Power Generator</p>
              <p className="font-bold text-green-600">$850</p>
            </div>
            <div className="flex items-center justify-between">
              <p className="font-medium">AI Writing Assistant (Annual)</p>
              <p className="font-bold text-green-600">$720</p>
            </div>
          </div>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4">Platform Performance</h3>
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <p className="font-medium">Pinterest</p>
              <p className="font-bold text-blue-600">45%</p>
            </div>
            <div className="flex items-center justify-between">
              <p className="font-medium">TikTok</p>
              <p className="font-bold text-blue-600">32%</p>
            </div>
            <div className="flex items-center justify-between">
              <p className="font-medium">Twitter</p>
              <p className="font-bold text-blue-600">23%</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
