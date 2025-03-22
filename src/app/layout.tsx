import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Kache Affiliate Marketing AI",
  description: "AI-powered affiliate marketing platform for reaching $10,000 monthly income",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <header className="bg-white dark:bg-gray-800 shadow-sm">
          <div className="container mx-auto px-4 py-4">
            <nav className="flex justify-between items-center">
              <div className="text-xl font-bold">Kache Affiliate</div>
              <div className="flex space-x-4">
                <a href="/" className="hover:text-blue-600">Home</a>
                <a href="/dashboard" className="hover:text-blue-600">Dashboard</a>
                <a href="/trends" className="hover:text-blue-600">Trends</a>
                <a href="/competitors" className="hover:text-blue-600">Competitors</a>
                <a href="/scraping" className="hover:text-blue-600">Data</a>
                <a href="/strategy" className="hover:text-blue-600">Strategy</a>
              </div>
            </nav>
          </div>
        </header>
        <main className="container mx-auto px-4 py-8">
          {children}
        </main>
        <footer className="bg-white dark:bg-gray-800 shadow-sm mt-8">
          <div className="container mx-auto px-4 py-4 text-center text-gray-500">
            &copy; {new Date().getFullYear()} Kache Affiliate Marketing AI
          </div>
        </footer>
      </body>
    </html>
  );
}
