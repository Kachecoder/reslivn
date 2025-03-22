import React from 'react';

export default function TrendsPage() {
  return (
    <div className="space-y-8">
      <section>
        <h1 className="text-3xl font-bold mb-4">Trend Research</h1>
        <p className="text-gray-600 dark:text-gray-300 mb-6">
          Analyze market trends across your target niches to identify profitable opportunities and emerging markets.
        </p>
      </section>
      
      <section className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4">Trending Niches</h3>
          <div className="space-y-4">
            <div>
              <div className="flex justify-between mb-1">
                <span className="font-medium">Survival & Emergency</span>
                <span className="text-green-600">+24%</span>
              </div>
              <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded-full">
                <div className="h-2 bg-green-600 rounded-full" style={{ width: '85%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between mb-1">
                <span className="font-medium">AI & Automation Tools</span>
                <span className="text-green-600">+18%</span>
              </div>
              <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded-full">
                <div className="h-2 bg-green-600 rounded-full" style={{ width: '72%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between mb-1">
                <span className="font-medium">E-Learning & Skill-Building</span>
                <span className="text-green-600">+12%</span>
              </div>
              <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded-full">
                <div className="h-2 bg-green-600 rounded-full" style={{ width: '65%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between mb-1">
                <span className="font-medium">DIY & Home Improvement</span>
                <span className="text-green-600">+8%</span>
              </div>
              <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded-full">
                <div className="h-2 bg-green-600 rounded-full" style={{ width: '58%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between mb-1">
                <span className="font-medium">Personal Finance</span>
                <span className="text-green-600">+5%</span>
              </div>
              <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded-full">
                <div className="h-2 bg-green-600 rounded-full" style={{ width: '52%' }}></div>
              </div>
            </div>
          </div>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4">Trending Keywords</h3>
          <div className="flex flex-wrap gap-2">
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">solar generator</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">emergency food</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">water filtration</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">ai writing</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">passive income</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">coding bootcamp</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">homesteading</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">diy solar</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">budget tools</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">automation</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">emergency kit</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">online courses</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">power outage</span>
            <span className="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">investing</span>
          </div>
        </div>
      </section>
      
      <section className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
        <h3 className="text-lg font-semibold mb-4">Trending Products</h3>
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
            <thead>
              <tr>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Product</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Niche</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Growth</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Commission</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Potential</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200 dark:divide-gray-700">
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">Bluetti Portable Power Station</td>
                <td className="px-4 py-3 whitespace-nowrap">Survival & Emergency</td>
                <td className="px-4 py-3 whitespace-nowrap text-green-600">+32%</td>
                <td className="px-4 py-3 whitespace-nowrap">$75-120</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <div className="flex items-center">
                    <span className="text-yellow-500">★★★★★</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">Jasper AI Writing Assistant</td>
                <td className="px-4 py-3 whitespace-nowrap">AI & Automation</td>
                <td className="px-4 py-3 whitespace-nowrap text-green-600">+28%</td>
                <td className="px-4 py-3 whitespace-nowrap">$40-200</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <div className="flex items-center">
                    <span className="text-yellow-500">★★★★★</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">Readywise Emergency Food Kit</td>
                <td className="px-4 py-3 whitespace-nowrap">Survival & Emergency</td>
                <td className="px-4 py-3 whitespace-nowrap text-green-600">+25%</td>
                <td className="px-4 py-3 whitespace-nowrap">$50-150</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <div className="flex items-center">
                    <span className="text-yellow-500">★★★★☆</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">Codecademy Pro Membership</td>
                <td className="px-4 py-3 whitespace-nowrap">E-Learning</td>
                <td className="px-4 py-3 whitespace-nowrap text-green-600">+22%</td>
                <td className="px-4 py-3 whitespace-nowrap">$30-120</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <div className="flex items-center">
                    <span className="text-yellow-500">★★★★☆</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">Berkey Water Filter System</td>
                <td className="px-4 py-3 whitespace-nowrap">Survival & Emergency</td>
                <td className="px-4 py-3 whitespace-nowrap text-green-600">+20%</td>
                <td className="px-4 py-3 whitespace-nowrap">$45-90</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <div className="flex items-center">
                    <span className="text-yellow-500">★★★★☆</span>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}
