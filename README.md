# Evalon Financial Platform

## Project Description
AI-powered financial analysis and algorithmic trading platform for retail investors.

**Senior Design Project - 2025**

### Team Members
- Ali Berk Yeşilduman (Leader) - 20200808035
- Zehra Doğru - [Student No]
- Ahmet Faruk Tekeli - [Student No]
- Münevver Nur Topluyürek -20210808067

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

---

## 📱 Mobile Application

The Evalon mobile application is developed using the Flutter framework.

### Folder Structure

```
evalon_mobil/
├── lib/
│   ├── core/
│   │   └── theme/
│   │       └── app_theme.dart     # Theme and color definitions
│   ├── screens/
│   │   ├── splash_screen.dart     # Splash screen
│   │   ├── onboarding_screen.dart # Onboarding flow
│   │   ├── login_screen.dart      # Login screen
│   │   ├── home_screen.dart       # Home page
│   │   ├── dashboard_screen.dart  # Dashboard
│   │   ├── portfolio_screen.dart  # Portfolio management
│   │   ├── strategies_screen.dart # Strategy list
│   │   └── profile_screen.dart    # Profile settings
│   └── main.dart                  # Application entry point
├── android/                       # Android platform files
├── ios/                           # iOS platform files
└── pubspec.yaml                   # Flutter dependencies
```

### Technologies Used

- **Flutter 3.32+** - Cross-platform UI framework
- **Dart 3.8+** - Programming language
- **Google Fonts** - Typography (Inter font family)
- **fl_chart** - Charts and graph components

### Theme & Design

- **Dark Mode** - Premium dark theme
- **Glassmorphism** - Modern glass effect design
- **Gradient Colors** - Indigo/Purple gradient color palette
- **Micro-animations** - Smooth transition animations

### Running the Mobile App

```bash
# Navigate to project folder
cd evalon_mobil

# Install dependencies
flutter pub get

# Run on iOS Simulator
flutter run -d ios

# Run on Android Emulator
flutter run -d android

# Run on Chrome (web)
flutter run -d chrome
```

### Requirements

- Flutter SDK 3.32+
- Xcode 15+ (for iOS)
- Android Studio (for Android)
- Android SDK Command-line Tools

---
