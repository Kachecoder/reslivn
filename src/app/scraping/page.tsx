import React from 'react';

export default function ScrapingPage() {
  return (
    <div className="space-y-8">
      <section>
        <h1 className="text-3xl font-bold mb-4">Data Scraping</h1>
        <p className="text-gray-600 dark:text-gray-300 mb-6">
          Configure and manage data scraping tasks across social media platforms and affiliate networks.
        </p>
      </section>
      
      <section className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4">Social Media</h3>
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span>Pinterest</span>
              <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Active</span>
            </div>
            <div className="flex items-center justify-between">
              <span>Twitter</span>
              <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Active</span>
            </div>
            <div className="flex items-center justify-between">
              <span>TikTok</span>
              <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Active</span>
            </div>
            <div className="flex items-center justify-between">
              <span>Instagram</span>
              <span className="px-2 py-1 bg-gray-100 text-gray-800 text-xs rounded-full">Inactive</span>
            </div>
            <div className="flex items-center justify-between">
              <span>Facebook</span>
              <span className="px-2 py-1 bg-gray-100 text-gray-800 text-xs rounded-full">Inactive</span>
            </div>
          </div>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4">Affiliate Networks</h3>
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span>Amazon Associates</span>
              <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Active</span>
            </div>
            <div className="flex items-center justify-between">
              <span>ClickBank</span>
              <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Active</span>
            </div>
            <div className="flex items-center justify-between">
              <span>ShareASale</span>
              <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Active</span>
            </div>
            <div className="flex items-center justify-between">
              <span>CJ Affiliate</span>
              <span className="px-2 py-1 bg-gray-100 text-gray-800 text-xs rounded-full">Inactive</span>
            </div>
            <div className="flex items-center justify-between">
              <span>Rakuten</span>
              <span className="px-2 py-1 bg-gray-100 text-gray-800 text-xs rounded-full">Inactive</span>
            </div>
          </div>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4">Scraping Stats</h3>
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span>Last Run</span>
              <span className="font-medium">2 hours ago</span>
            </div>
            <div className="flex items-center justify-between">
              <span>Data Points</span>
              <span className="font-medium">12,450</span>
            </div>
            <div className="flex items-center justify-between">
              <span>Products Found</span>
              <span className="font-medium">342</span>
            </div>
            <div className="flex items-center justify-between">
              <span>Trends Identified</span>
              <span className="font-medium">28</span>
            </div>
            <div className="flex items-center justify-between">
              <span>Next Run</span>
              <span className="font-medium">22 minutes</span>
            </div>
          </div>
        </div>
      </section>
      
      <section className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
        <h3 className="text-lg font-semibold mb-4">Recent Scraping Tasks</h3>
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
            <thead>
              <tr>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Task ID</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Source</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Target</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Status</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Results</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Time</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200 dark:divide-gray-700">
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">task_1679423</td>
                <td className="px-4 py-3 whitespace-nowrap">Pinterest</td>
                <td className="px-4 py-3 whitespace-nowrap">solar generator</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Completed</span>
                </td>
                <td className="px-4 py-3 whitespace-nowrap">245 pins</td>
                <td className="px-4 py-3 whitespace-nowrap">2 hours ago</td>
              </tr>
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">task_1679422</td>
                <td className="px-4 py-3 whitespace-nowrap">Twitter</td>
                <td className="px-4 py-3 whitespace-nowrap">emergency food</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Completed</span>
                </td>
                <td className="px-4 py-3 whitespace-nowrap">178 tweets</td>
                <td className="px-4 py-3 whitespace-nowrap">3 hours ago</td>
              </tr>
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">task_1679421</td>
                <td className="px-4 py-3 whitespace-nowrap">TikTok</td>
                <td className="px-4 py-3 whitespace-nowrap">ai writing tools</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Completed</span>
                </td>
                <td className="px-4 py-3 whitespace-nowrap">312 videos</td>
                <td className="px-4 py-3 whitespace-nowrap">5 hours ago</td>
              </tr>
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">task_1679420</td>
                <td className="px-4 py-3 whitespace-nowrap">Amazon</td>
                <td className="px-4 py-3 whitespace-nowrap">water filtration</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Completed</span>
                </td>
                <td className="px-4 py-3 whitespace-nowrap">87 products</td>
                <td className="px-4 py-3 whitespace-nowrap">6 hours ago</td>
              </tr>
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">task_1679419</td>
                <td className="px-4 py-3 whitespace-nowrap">ClickBank</td>
                <td className="px-4 py-3 whitespace-nowrap">passive income</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Completed</span>
                </td>
                <td className="px-4 py-3 whitespace-nowrap">42 products</td>
                <td className="px-4 py-3 whitespace-nowrap">8 hours ago</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
      
      <section className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
        <h3 className="text-lg font-semibold mb-4">Configure New Scraping Task</h3>
        <form className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Source</label>
              <select className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800">
                <option>Pinterest</option>
                <option>Twitter</option>
                <option>TikTok</option>
                <option>Amazon Associates</option>
                <option>ClickBank</option>
                <option>ShareASale</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Target Keywords</label>
              <input type="text" className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800" placeholder="e.g., solar generator, emergency food" />
            </div>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Niche</label>
              <select className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800">
                <option>Survival & Emergency</option>
                <option>DIY & Home Improvement</option>
                <option>Personal Finance</option>
                <option>E-Learning</option>
                <option>AI & Automation</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Data Limit</label>
              <select className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800">
                <option>100 results</option>
                <option>250 results</option>
                <option>500 results</option>
                <option>1000 results</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Schedule</label>
              <select className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800">
                <option>Run Once</option>
                <option>Daily</option>
                <option>Weekly</option>
                <option>Monthly</option>
              </select>
            </div>
          </div>
          <div className="flex justify-end">
            <button type="button" className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
              Start Scraping Task
            </button>
          </div>
        </form>
      </section>
    </div>
  );
}
