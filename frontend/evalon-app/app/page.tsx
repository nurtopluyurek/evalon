export default function Home() {
    return (
        <main className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
            {/* Hero Section */}
            <div className="container mx-auto px-4 py-20">
                <div className="text-center mb-16">
                    <h1 className="text-6xl font-bold text-white mb-4">
                        Evalon Financial Platform
                    </h1>
                    <p className="text-xl text-gray-300 mb-8">
                        AI-Powered Trading Strategies for Everyone
                    </p>
                    <div className="flex gap-4 justify-center">
                        <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-semibold transition-colors duration-200">
                            Get Started
                        </button>
                        <button className="bg-gray-700 hover:bg-gray-600 text-white px-8 py-3 rounded-lg font-semibold transition-colors duration-200">
                            Learn More
                        </button>
                    </div>
                </div>

                {/* Features Grid */}
                <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mt-20">
                    <FeatureCard
                        icon="🎯"
                        title="Strategy Builder"
                        description="Create trading strategies with drag-and-drop or natural language"
                    />
                    <FeatureCard
                        icon="🧠"
                        title="AI Analysis"
                        description="Get insights from AI-powered market analysis"
                    />
                    <FeatureCard
                        icon="📊"
                        title="Backtesting"
                        description="Test your strategies on historical data"
                    />
                    <FeatureCard
                        icon="❤️"
                        title="Psychology Tracking"
                        description="Understand and improve your trading behavior"
                    />
                </div>

                {/* Stats Section */}
                <div className="grid md:grid-cols-3 gap-8 mt-20">
                    <StatCard number="4" label="Microservices" />
                    <StatCard number="2" label="Databases" />
                    <StatCard number="100%" label="Cloud Native" />
                </div>

                {/* Navigation Links */}
                <div className="mt-16 text-center">
                    <a
                        href="/api-test"
                        className="text-blue-400 hover:text-blue-300 underline text-lg"
                    >
                        → Go to API Test Page
                    </a>
                </div>
            </div>
        </main>
    )
}

function FeatureCard({ icon, title, description }: {
    icon: string
    title: string
    description: string
}) {
    return (
        <div className="bg-white/10 backdrop-blur-lg rounded-xl p-6 hover:bg-white/20 transition-all duration-300 border border-white/20">
            <div className="text-5xl mb-4">{icon}</div>
            <h3 className="text-xl font-bold text-white mb-2">{title}</h3>
            <p className="text-gray-300 text-sm">{description}</p>
        </div>
    )
}

function StatCard({ number, label }: { number: string; label: string }) {
    return (
        <div className="bg-white/5 backdrop-blur-lg rounded-xl p-8 text-center border border-white/10">
            <div className="text-5xl font-bold text-blue-400 mb-2">{number}</div>
            <div className="text-gray-300">{label}</div>
        </div>
    )
}
