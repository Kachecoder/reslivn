import React from 'react';

export default function StrategyPage() {
  return (
    <div className="space-y-8">
      <section>
        <h1 className="text-3xl font-bold mb-4">Marketing Strategy</h1>
        <p className="text-gray-600 dark:text-gray-300 mb-6">
          Develop and optimize your affiliate marketing strategies to reach your $10,000 monthly income goal.
        </p>
      </section>
      
      <section className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4">Income Goal Progress</h3>
          <div className="space-y-4">
            <div>
              <div className="flex justify-between mb-1">
                <span className="font-medium">Current Monthly Income</span>
                <span className="font-medium">$3,500</span>
              </div>
              <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded-full">
                <div className="h-4 bg-blue-600 rounded-full" style={{ width: '35%' }}></div>
              </div>
              <div className="flex justify-between mt-1 text-sm text-gray-500">
                <span>$0</span>
                <span>$10,000</span>
              </div>
            </div>
            
            <div className="grid grid-cols-2 gap-4 mt-4">
              <div className="bg-blue-50 dark:bg-blue-900/20 p-3 rounded-lg">
                <p className="text-sm text-gray-600 dark:text-gray-300">Monthly Growth</p>
                <p className="text-xl font-bold text-blue-600">+18%</p>
              </div>
              <div className="bg-blue-50 dark:bg-blue-900/20 p-3 rounded-lg">
                <p className="text-sm text-gray-600 dark:text-gray-300">Projected Date</p>
                <p className="text-xl font-bold text-blue-600">Nov 2025</p>
              </div>
            </div>
          </div>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4">Niche Allocation</h3>
          <div className="space-y-4">
            <div>
              <div className="flex justify-between mb-1">
                <span className="font-medium">Survival & Emergency</span>
                <span className="font-medium">42%</span>
              </div>
              <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded-full">
                <div className="h-2 bg-blue-600 rounded-full" style={{ width: '42%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between mb-1">
                <span className="font-medium">AI & Automation Tools</span>
                <span className="font-medium">25%</span>
              </div>
              <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded-full">
                <div className="h-2 bg-blue-600 rounded-full" style={{ width: '25%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between mb-1">
                <span className="font-medium">E-Learning & Skill-Building</span>
                <span className="font-medium">18%</span>
              </div>
              <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded-full">
                <div className="h-2 bg-blue-600 rounded-full" style={{ width: '18%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between mb-1">
                <span className="font-medium">DIY & Home Improvement</span>
                <span className="font-medium">10%</span>
              </div>
              <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded-full">
                <div className="h-2 bg-blue-600 rounded-full" style={{ width: '10%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between mb-1">
                <span className="font-medium">Personal Finance</span>
                <span className="font-medium">5%</span>
              </div>
              <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded-full">
                <div className="h-2 bg-blue-600 rounded-full" style={{ width: '5%' }}></div>
              </div>
            </div>
          </div>
        </div>
      </section>
      
      <section className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
        <h3 className="text-lg font-semibold mb-4">Recommended Strategies</h3>
        <div className="space-y-6">
          <div className="border-l-4 border-blue-500 pl-4">
            <h4 className="font-medium text-lg mb-2">Increase Pinterest Content for Survival Niche</h4>
            <p className="text-gray-600 dark:text-gray-300 mb-2">
              Pinterest shows the highest conversion rates for survival and emergency preparedness products. 
              Increase pin creation frequency to 5 pins per week focusing on solar generators and water filtration systems.
            </p>
            <div className="flex space-x-2">
              <span className="px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full">High Impact</span>
              <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Easy Implementation</span>
            </div>
          </div>
          
          <div className="border-l-4 border-blue-500 pl-4">
            <h4 className="font-medium text-lg mb-2">Create TikTok Demonstrations for AI Tools</h4>
            <p className="text-gray-600 dark:text-gray-300 mb-2">
              Short-form video demonstrations of AI writing tools and automation software perform exceptionally well on TikTok.
              Create 3 videos per week showing real-time results and benefits.
            </p>
            <div className="flex space-x-2">
              <span className="px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full">High Impact</span>
              <span className="px-2 py-1 bg-yellow-100 text-yellow-800 text-xs rounded-full">Medium Implementation</span>
            </div>
          </div>
          
          <div className="border-l-4 border-blue-500 pl-4">
            <h4 className="font-medium text-lg mb-2">Develop Product Comparison Content</h4>
            <p className="text-gray-600 dark:text-gray-300 mb-2">
              Competitor analysis shows product comparison content has the highest conversion rates.
              Create detailed comparisons for top 5 products in each niche with clear affiliate links.
            </p>
            <div className="flex space-x-2">
              <span className="px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full">High Impact</span>
              <span className="px-2 py-1 bg-yellow-100 text-yellow-800 text-xs rounded-full">Medium Implementation</span>
            </div>
          </div>
          
          <div className="border-l-4 border-blue-500 pl-4">
            <h4 className="font-medium text-lg mb-2">Expand to CJ Affiliate Network</h4>
            <p className="text-gray-600 dark:text-gray-300 mb-2">
              CJ Affiliate offers higher commission rates for emergency preparedness products.
              Apply to their program and integrate their top-converting products into your content strategy.
            </p>
            <div className="flex space-x-2">
              <span className="px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full">High Impact</span>
              <span className="px-2 py-1 bg-red-100 text-red-800 text-xs rounded-full">Complex Implementation</span>
            </div>
          </div>
        </div>
      </section>
      
      <section className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
        <h3 className="text-lg font-semibold mb-4">Action Plan</h3>
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
            <thead>
              <tr>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Action</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Platform</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Frequency</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Expected Impact</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200 dark:divide-gray-700">
              <tr>
                <td className="px-4 py-3">Create solar generator pins</td>
                <td className="px-4 py-3">Pinterest</td>
                <td className="px-4 py-3">5 per week</td>
                <td className="px-4 py-3">+$450/month</td>
                <td className="px-4 py-3">
                  <span className="px-2 py-1 bg-yellow-100 text-yellow-800 text-xs rounded-full">In Progress</span>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3">AI tool demonstrations</td>
                <td className="px-4 py-3">TikTok</td>
                <td className="px-4 py-3">3 per week</td>
                <td className="px-4 py-3">+$320/month</td>
                <td className="px-4 py-3">
                  <span className="px-2 py-1 bg-yellow-100 text-yellow-800 text-xs rounded-full">In Progress</span>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3">Product comparison articles</td>
                <td className="px-4 py-3">All</td>
                <td className="px-4 py-3">2 per week</td>
                <td className="px-4 py-3">+$280/month</td>
                <td className="px-4 py-3">
                  <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Completed</span>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3">CJ Affiliate application</td>
                <td className="px-4 py-3">CJ Affiliate</td>
                <td className="px-4 py-3">One-time</td>
                <td className="px-4 py-3">+$500/month</td>
                <td className="px-4 py-3">
                  <span className="px-2 py-1 bg-gray-100 text-gray-800 text-xs rounded-full">Not Started</span>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3">Emergency checklist lead magnets</td>
                <td className="px-4 py-3">Pinterest</td>
                <td className="px-4 py-3">1 per week</td>
                <td className="px-4 py-3">+$150/month</td>
                <td className="px-4 py-3">
                  <span className="px-2 py-1 bg-gray-100 text-gray-800 text-xs rounded-full">Not Started</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}
