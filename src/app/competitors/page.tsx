import React from 'react';

export default function CompetitorsPage() {
  return (
    <div className="space-y-8">
      <section>
        <h1 className="text-3xl font-bold mb-4">Competitor Analysis</h1>
        <p className="text-gray-600 dark:text-gray-300 mb-6">
          Monitor your competitors across different niches and platforms. Analyze their strategies, content, and performance metrics.
        </p>
      </section>
      
      <section className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4">Top Competitors</h3>
          <div className="space-y-4">
            {[
              { name: 'SurvivalPrepper', platform: 'Pinterest', followers: '125K', engagement: '4.8%' },
              { name: 'EmergencyReady', platform: 'TikTok', followers: '98K', engagement: '5.2%' },
              { name: 'PassiveIncomeGuru', platform: 'Twitter', followers: '76K', engagement: '3.7%' },
              { name: 'DIYHomestead', platform: 'Pinterest', followers: '112K', engagement: '4.2%' },
              { name: 'AIToolMaster', platform: 'TikTok', followers: '65K', engagement: '6.1%' },
            ].map((competitor, index) => (
              <div key={index} className="flex justify-between items-center pb-2 border-b border-gray-100 dark:border-gray-700">
                <div>
                  <p className="font-medium">{competitor.name}</p>
                  <p className="text-sm text-gray-500 dark:text-gray-400">{competitor.platform}</p>
                </div>
                <div className="text-right">
                  <p className="font-medium">{competitor.followers} followers</p>
                  <p className="text-sm text-green-600">{competitor.engagement} engagement</p>
                </div>
              </div>
            ))}
          </div>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4">Competitor Strategies</h3>
          <div className="space-y-4">
            <div className="pb-2 border-b border-gray-100 dark:border-gray-700">
              <p className="font-medium">Content Strategy</p>
              <p className="text-sm text-gray-600 dark:text-gray-300">Top competitors post 3-5 times per week with a mix of educational content (60%) and product reviews (40%)</p>
            </div>
            <div className="pb-2 border-b border-gray-100 dark:border-gray-700">
              <p className="font-medium">Platform Focus</p>
              <p className="text-sm text-gray-600 dark:text-gray-300">Pinterest dominates for Survival and DIY niches, while TikTok leads for AI Tools and E-Learning</p>
            </div>
            <div className="pb-2 border-b border-gray-100 dark:border-gray-700">
              <p className="font-medium">Monetization Methods</p>
              <p className="text-sm text-gray-600 dark:text-gray-300">Amazon Associates (45%), Direct affiliate programs (35%), ClickBank (20%)</p>
            </div>
            <div className="pb-2 border-b border-gray-100 dark:border-gray-700">
              <p className="font-medium">Content Types</p>
              <p className="text-sm text-gray-600 dark:text-gray-300">How-to guides, product comparisons, emergency preparation checklists, tool reviews</p>
            </div>
          </div>
        </div>
      </section>
      
      <section className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
        <h3 className="text-lg font-semibold mb-4">Competitor Content Analysis</h3>
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
            <thead>
              <tr>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Content Type</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Avg. Engagement</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Conversion Rate</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Best Platform</th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Opportunity</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200 dark:divide-gray-700">
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">Product Reviews</td>
                <td className="px-4 py-3 whitespace-nowrap">4.2%</td>
                <td className="px-4 py-3 whitespace-nowrap">3.8%</td>
                <td className="px-4 py-3 whitespace-nowrap">Pinterest</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <div className="flex items-center">
                    <span className="text-yellow-500">★★★★☆</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">How-to Guides</td>
                <td className="px-4 py-3 whitespace-nowrap">5.7%</td>
                <td className="px-4 py-3 whitespace-nowrap">2.9%</td>
                <td className="px-4 py-3 whitespace-nowrap">TikTok</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <div className="flex items-center">
                    <span className="text-yellow-500">★★★★★</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">Comparison Posts</td>
                <td className="px-4 py-3 whitespace-nowrap">3.9%</td>
                <td className="px-4 py-3 whitespace-nowrap">4.5%</td>
                <td className="px-4 py-3 whitespace-nowrap">Pinterest</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <div className="flex items-center">
                    <span className="text-yellow-500">★★★★★</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">Emergency Checklists</td>
                <td className="px-4 py-3 whitespace-nowrap">6.2%</td>
                <td className="px-4 py-3 whitespace-nowrap">3.2%</td>
                <td className="px-4 py-3 whitespace-nowrap">Pinterest</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <div className="flex items-center">
                    <span className="text-yellow-500">★★★★☆</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3 whitespace-nowrap">Tool Demonstrations</td>
                <td className="px-4 py-3 whitespace-nowrap">7.1%</td>
                <td className="px-4 py-3 whitespace-nowrap">3.7%</td>
                <td className="px-4 py-3 whitespace-nowrap">TikTok</td>
                <td className="px-4 py-3 whitespace-nowrap">
                  <div className="flex items-center">
                    <span className="text-yellow-500">★★★★★</span>
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
