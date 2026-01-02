-- Evalon Database Initialization Script

-- Enable extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Set timezone
SET timezone = 'UTC';

-- Create schemas
CREATE SCHEMA IF NOT EXISTS auth;
CREATE SCHEMA IF NOT EXISTS strategy;
CREATE SCHEMA IF NOT EXISTS backtest;
CREATE SCHEMA IF NOT EXISTS market_data;

-- Grant permissions
GRANT ALL PRIVILEGES ON SCHEMA auth TO evalon;
GRANT ALL PRIVILEGES ON SCHEMA strategy TO evalon;
GRANT ALL PRIVILEGES ON SCHEMA backtest TO evalon;
GRANT ALL PRIVILEGES ON SCHEMA market_data TO evalon;

-- Create initial tables will be done by SQLAlchemy
-- This is just the initialization script

SELECT 'Database initialized successfully!' AS status;
