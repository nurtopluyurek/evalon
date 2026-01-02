# Evalon Financial Platform

## Project Description
AI-powered financial analysis and algorithmic trading platform for retail investors.

**Senior Design Project - 2025**

### Team Members
- Ali Berk Yeşilduman (Leader) - [Student No]
- Zehra Doğru - [Student No]
- Ahmet Faruk Tekeli - [Student No]
- Münevver Nur Topluyürek - [Student No]

**Advisor:** Alper Özcan

---

## Project Architecture

Evalon uses a microservices architecture with the following components:

### Backend Services
- **Auth Service** (Port 8001): User authentication and authorization
- **Strategy Service** (Port 8002): Trading strategy management
- **Backtest Service** (Port 8003): Strategy backtesting engine
- **Market Data Service** (Port 8004): Market data ingestion and storage

### Frontend
- **Next.js Application** (Port 3000): User interface

### Infrastructure
- **PostgreSQL + TimescaleDB**: Hybrid database for relational and time-series data
- **Redis**: Caching and message broker
- **Docker**: Containerization
- **Kubernetes**: Orchestration (planned)

---

## Current Implementation Status (Interim Report)

### ✅ Completed
- [x] System architecture design
- [x] Database schema design
- [x] UML diagrams (Use Case, Class, Sequence, etc.)
- [x] Auth Service - Basic implementation
- [x] Strategy Service - Basic implementation
- [x] Frontend skeleton
- [x] Docker containerization setup
- [x] PostgreSQL database setup

### 🔄 In Progress
- [ ] Backtest engine logic
- [ ] Market data integration
- [ ] AI service (LLM integration)
- [ ] Frontend-backend integration

### 📅 Planned for Next Phase
- [ ] Kubernetes deployment
- [ ] CI/CD pipeline
- [ ] Investor psychology module
- [ ] Portfolio management features

---

## Tech Stack

**Backend:**
- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL + TimescaleDB

**Frontend:**
- Next.js 14
- TypeScript
- Tailwind CSS

**DevOps:**
- Docker
- Docker Compose
- Kubernetes (planned)
- GitHub Actions (planned)

---

## Project Structure

```
evalon/
├── backend/
│   ├── auth-service/          # User authentication
│   ├── strategy-service/      # Strategy management
│   ├── backtest-service/      # Backtesting engine
│   ├── market-data-service/   # Market data handling
│   └── shared/                # Shared utilities
├── frontend/
│   └── evalon-app/           # Next.js application
├── database/
│   ├── migrations/           # Database migrations
│   └── schemas/              # SQL schemas
├── docker/
│   └── docker-compose.yml
├── docs/
│   ├── architecture/         # Architecture diagrams
│   └── api/                  # API documentation
└── README.md
```

---

## Setup Instructions

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- PostgreSQL 15+

### Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/[your-username]/evalon-financial-platform.git
cd evalon-financial-platform
```

2. **Start backend services:**
```bash
cd backend/auth-service
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

3. **Start frontend:**
```bash
cd frontend/evalon-app
npm install
npm run dev
```

4. **Using Docker (Recommended):**
```bash
docker-compose up --build
```

---

## API Documentation

### Auth Service (Port 8001)
- `POST /register` - User registration
- `POST /login` - User login
- `GET /health` - Service health check

**Swagger UI:** http://localhost:8001/docs

### Strategy Service (Port 8002)
- `POST /strategies` - Create new strategy
- `GET /strategies` - List all strategies
- `GET /strategies/{id}` - Get strategy by ID
- `DELETE /strategies/{id}` - Delete strategy

**Swagger UI:** http://localhost:8002/docs

---

## Testing

```bash
# Run backend tests
cd backend/auth-service
pytest

# Test API endpoints
curl http://localhost:8001/health
```

---

## Contributing

This is a senior design project. For team members:
1. Create feature branch from `main`
2. Make changes
3. Create pull request
4. Wait for review before merging

---

## License
This project is developed as part of a senior design course requirement.

---

## Contact
For questions or issues, contact the project advisor or team leader.

**Last Updated:** January 2026
