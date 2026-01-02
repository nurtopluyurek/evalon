# Evalon Setup Guide

## Prerequisites
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- PostgreSQL 15+ (if running locally)

## Local Development Setup

### 1. Clone Repository
```bash
git clone https://github.com/[username]/evalon-financial-platform.git
cd evalon-financial-platform
```

### 2. Backend Setup

#### Auth Service
```bash
cd backend/auth-service
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

#### Strategy Service
```bash
cd backend/strategy-service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### 3. Frontend Setup
```bash
cd frontend/evalon-app
npm install
npm run dev
```

### 4. Database Setup
```bash
# Using Docker
docker-compose up -d postgres

# Or install PostgreSQL locally
# Create database: evalon_db
# User: evalon, Password: evalon123
```

## Docker Deployment

### Build and Run All Services
```bash
docker-compose up --build
```

### Access Services
- Auth Service: http://localhost:8001/docs
- Strategy Service: http://localhost:8002/docs
- Frontend: http://localhost:3000

## Testing

### Test Auth Service
```bash
curl -X POST http://localhost:8001/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@evalon.com","password":"test123","full_name":"Test User"}'
```

### Test Strategy Service
```bash
curl -X POST http://localhost:8002/strategies \
  -H "Content-Type: application/json" \
  -d '{"name":"My Strategy","description":"Test","rules":"Buy low sell high","user_id":1}'
```

## Troubleshooting

### Port Already in Use
```bash
# Kill process on port
lsof -ti:8001 | xargs kill -9
```

### Database Connection Error
- Check if PostgreSQL is running
- Verify DATABASE_URL in config
- Check firewall settings
