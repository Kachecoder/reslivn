import Image from "next/image";

export default function Home() {
  return (
    <div className="space-y-12">
      <section className="text-center">
        <h1 className="text-4xl font-bold mb-4">Kache Affiliate Marketing AI</h1>
        <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto">
          Your AI-powered assistant for reaching $10,000 monthly affiliate income
        </p>
      </section>

      <section className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-3">Data-Driven Insights</h2>
          <p className="text-gray-600 dark:text-gray-300">
            Leverage AI-powered analysis of market trends, competitor strategies, and consumer behavior to identify the most profitable opportunities.
          </p>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-3">Target Niches</h2>
          <p className="text-gray-600 dark:text-gray-300">
            Focus on high-potential niches: Survival & Emergency Preparedness, DIY & Home Improvement, 
            Personal Finance, E-Learning, and AI Tools.
          </p>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-3">Social Media Integration</h2>
          <p className="text-gray-600 dark:text-gray-300">
            Seamlessly integrate with your Pinterest, Twitter, and TikTok accounts to maximize reach and engagement with your target audience.
          </p>
        </div>
      </section>

      <section className="bg-blue-50 dark:bg-blue-900/20 p-8 rounded-lg">
        <h2 className="text-2xl font-bold mb-4">How It Works</h2>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div className="text-center">
            <div className="bg-blue-100 dark:bg-blue-800 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-3">
              <span className="font-bold">1</span>
            </div>
            <h3 className="font-medium mb-2">Data Collection</h3>
            <p className="text-sm">Gather market data from social media and affiliate networks</p>
          </div>
          
          <div className="text-center">
            <div className="bg-blue-100 dark:bg-blue-800 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-3">
              <span className="font-bold">2</span>
            </div>
            <h3 className="font-medium mb-2">Trend Analysis</h3>
            <p className="text-sm">Identify emerging trends and profitable opportunities</p>
          </div>
          
          <div className="text-center">
            <div className="bg-blue-100 dark:bg-blue-800 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-3">
              <span className="font-bold">3</span>
            </div>
            <h3 className="font-medium mb-2">Strategy Development</h3>
            <p className="text-sm">Create data-driven marketing strategies</p>
          </div>
          
          <div className="text-center">
            <div className="bg-blue-100 dark:bg-blue-800 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-3">
              <span className="font-bold">4</span>
            </div>
            <h3 className="font-medium mb-2">Income Growth</h3>
            <p className="text-sm">Track progress toward $10,000 monthly income</p>
          </div>
        </div>
      </section>
    </div>
  );
}
