'use client'

import { useState } from 'react'

export default function ApiTest() {
    const [authStatus, setAuthStatus] = useState<string>('Not tested')
    const [strategyStatus, setStrategyStatus] = useState<string>('Not tested')
    const [registerResult, setRegisterResult] = useState<string>('')
    const [strategyResult, setStrategyResult] = useState<string>('')

    const testAuthService = async () => {
        setAuthStatus('Testing...')
        try {
            const response = await fetch('http://localhost:8001/health')
            const data = await response.json()
            setAuthStatus(`✅ Success: ${JSON.stringify(data, null, 2)}`)
        } catch (error) {
            setAuthStatus(`❌ Error: ${error}`)
        }
    }

    const testStrategyService = async () => {
        setStrategyStatus('Testing...')
        try {
            const response = await fetch('http://localhost:8002/health')
            const data = await response.json()
            setStrategyStatus(`✅ Success: ${JSON.stringify(data, null, 2)}`)
        } catch (error) {
            setStrategyStatus(`❌ Error: ${error}`)
        }
    }

    const testRegister = async () => {
        setRegisterResult('Registering...')
        try {
            const response = await fetch('http://localhost:8001/register', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    email: `test${Date.now()}@evalon.com`,
                    password: 'test123',
                    full_name: 'Test User'
                })
            })
            const data = await response.json()
            setRegisterResult(`✅ Success: ${JSON.stringify(data, null, 2)}`)
        } catch (error) {
            setRegisterResult(`❌ Error: ${error}`)
        }
    }

    const testCreateStrategy = async () => {
        setStrategyResult('Creating strategy...')
        try {
            const response = await fetch('http://localhost:8002/strategies', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    name: 'Moving Average Strategy',
                    description: 'Buy when 50 MA crosses above 200 MA',
                    rules: 'IF SMA(50) > SMA(200) THEN BUY',
                    user_id: 1
                })
            })
            const data = await response.json()
            setStrategyResult(`✅ Success: ${JSON.stringify(data, null, 2)}`)
        } catch (error) {
            setStrategyResult(`❌ Error: ${error}`)
        }
    }

    return (
        <div className="min-h-screen bg-gray-900 text-white p-8">
            <div className="max-w-4xl mx-auto">
                <h1 className="text-4xl font-bold mb-2">API Connection Test</h1>
                <p className="text-gray-400 mb-8">Test backend services connectivity</p>

                <a href="/" className="text-blue-400 hover:text-blue-300 mb-8 inline-block">
                    ← Back to Home
                </a>

                <div className="space-y-6">
                    {/* Auth Service Health */}
                    <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
                        <h2 className="text-2xl font-semibold mb-4">🔐 Auth Service</h2>
                        <div className="flex gap-4 mb-4">
                            <button
                                onClick={testAuthService}
                                className="bg-blue-600 hover:bg-blue-700 px-6 py-2 rounded-lg font-semibold transition-colors"
                            >
                                Test Health (Port 8001)
                            </button>
                            <button
                                onClick={testRegister}
                                className="bg-purple-600 hover:bg-purple-700 px-6 py-2 rounded-lg font-semibold transition-colors"
                            >
                                Test Register
                            </button>
                        </div>
                        <div className="space-y-2">
                            <p className="text-sm text-gray-400">Health Check:</p>
                            <pre className="bg-gray-900 p-4 rounded overflow-x-auto text-sm">
                                {authStatus}
                            </pre>
                            {registerResult && (
                                <>
                                    <p className="text-sm text-gray-400 mt-4">Register Result:</p>
                                    <pre className="bg-gray-900 p-4 rounded overflow-x-auto text-sm">
                                        {registerResult}
                                    </pre>
                                </>
                            )}
                        </div>
                    </div>

                    {/* Strategy Service Health */}
                    <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
                        <h2 className="text-2xl font-semibold mb-4">📈 Strategy Service</h2>
                        <div className="flex gap-4 mb-4">
                            <button
                                onClick={testStrategyService}
                                className="bg-green-600 hover:bg-green-700 px-6 py-2 rounded-lg font-semibold transition-colors"
                            >
                                Test Health (Port 8002)
                            </button>
                            <button
                                onClick={testCreateStrategy}
                                className="bg-orange-600 hover:bg-orange-700 px-6 py-2 rounded-lg font-semibold transition-colors"
                            >
                                Create Strategy
                            </button>
                        </div>
                        <div className="space-y-2">
                            <p className="text-sm text-gray-400">Health Check:</p>
                            <pre className="bg-gray-900 p-4 rounded overflow-x-auto text-sm">
                                {strategyStatus}
                            </pre>
                            {strategyResult && (
                                <>
                                    <p className="text-sm text-gray-400 mt-4">Strategy Result:</p>
                                    <pre className="bg-gray-900 p-4 rounded overflow-x-auto text-sm">
                                        {strategyResult}
                                    </pre>
                                </>
                            )}
                        </div>
                    </div>

                    {/* API Documentation Links */}
                    <div className="bg-blue-900/20 border border-blue-700 rounded-lg p-6">
                        <h3 className="text-xl font-semibold mb-4">📋 API Documentation</h3>
                        <div className="grid md:grid-cols-2 gap-4">
                            <a
                                href="http://localhost:8001/docs"
                                target="_blank"
                                className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg text-center transition-colors"
                            >
                                Auth Service Swagger UI
                            </a>
                            <a
                                href="http://localhost:8002/docs"
                                target="_blank"
                                className="bg-green-600 hover:bg-green-700 px-6 py-3 rounded-lg text-center transition-colors"
                            >
                                Strategy Service Swagger UI
                            </a>
                        </div>
                    </div>

                    {/* Instructions */}
                    <div className="bg-gray-800/50 border border-gray-700 rounded-lg p-6">
                        <h3 className="text-xl font-semibold mb-4">🚀 Quick Start</h3>
                        <ol className="list-decimal list-inside space-y-2 text-gray-300">
                            <li>Start PostgreSQL: <code className="bg-gray-700 px-2 py-1 rounded">docker-compose up -d postgres</code></li>
                            <li>Start Auth Service: <code className="bg-gray-700 px-2 py-1 rounded">cd backend/auth-service && python main.py</code></li>
                            <li>Start Strategy Service: <code className="bg-gray-700 px-2 py-1 rounded">cd backend/strategy-service && python main.py</code></li>
                            <li>Test connections using the buttons above</li>
                        </ol>
                    </div>
                </div>
            </div>
        </div>
    )
}
