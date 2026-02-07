# BrainBolt - Adaptive Infinite Quiz Platform

BrainBolt is a real-time, adaptive quiz platform built with Python FastAPI, PostgreSQL, and Redis.

## Features
*   **Adaptive Difficulty**: Questions get harder as you answer correctly, easier if you miss.
*   **Streak System**: Consecutive correct answers multiply your score.
*   **Streak Decay**: Inactivity (>24h) halves your streak.
*   **Real-time Leaderboards**: Redis-backed leaderboards for Top Scores and Longest Streaks.
*   **Daily Accuracy**: Your daily performance impacts your score multiplier.

## Tech Stack
*   **Service**: Python 3.11 + FastAPI
*   **Database**: PostgreSQL 15 (Async SQLAlchemy)
*   **Cache/Leaderboard**: Redis 7
*   **Infrastructure**: Docker Compose

## Data Model
*   **Users**: stores basic user info
*   **UserStates**: stores user state
*   **UserSubmissions**: stores user submissions
*   **Questions**: stores questions (for this project have used the questions as a list but for production it will be a database table and we can use redis to cache the questions based on difficulty)

## Setup & Run

### Prerequisites
*   Docker & Docker Compose

### Running the Application
```bash
docker-compose up --build
```
The API will be available at `http://localhost:8000`.

### API Documentation
Once running, visit `http://localhost:8000/docs` for the interactive Swagger UI.

### Key Endpoints
*   `GET /v1/quiz/next?userId={uuid}`: Get next adaptive question.
*   `POST /v1/quiz/answer`: Submit answer.
*   `GET /v1/leaderboard/score`: Top global scores.
*   `GET /v1/leaderboard/streak`: Top global streaks.
*   `GET /v1/leaderboard/metrics/{userId}`: User specific metrics.

## Testing
### Load Testing (Locust)
Run the load test script to simulate user traffic:
```bash
pip install locust
locust -f locustfile.py
```
Open `http://localhost:8089` to start the test.

## Project Structure
```
BrainBolt/
├── app/
│   ├── api/            # API endpoints (v1)
│   ├── core/           # Configuration, Database, Redis config
│   ├── data/           # Static data (Questions)
│   ├── models/         # SQLModel database models
│   ├── schemas/        # Pydantic schemas for request/response
│   └── services/       # Business logic (Quiz, Leaderboard)
├── docker-compose.yml  # Docker orchestration
├── Dockerfile          # App container definition
├── requirements.txt    # Python dependencies
└── locustfile.py       # Load testing script
```

## Design Decisions
1.  **FastAPI & Async**: Chosen for high performance and native async support, crucial for handling concurrent quiz sessions.
2.  **Redis for Leaderboards**: Leverages Redis Sorted Sets (`ZSET`) for O(log(N)) ranking operations, ensuring real-time leaderboard updates even with high traffic.
3.  **PostgreSQL for Persistence**: User state and detailed submission history are stored in Postgres for reliability and complex querying if needed later.
4.  **Stateless API**: The API is stateless; all session context is passed via `userId` or stored in the database/cache, allowing easy horizontal scaling.
5.  **Gunicorn Process Manager**: Uses Gunicorn with Uvicorn workers in production to maximize CPU utilization and handle concurrent requests efficiently.

## Scalability
*   **Horizontal Scaling**: The stateless design allows deploying multiple instances of the app container behind a load balancer (e.g., Nginx, AWS ALB).
*   **Database Scaling**: Postgres can be scaled using connection pooling (pgbouncer) and read replicas.
*   **Cache Scaling**: Redis Cluster acts as a scalable layer for leaderboards and potentially ephemeral state.
*   **Worker Configuration**: Gunicorn is configured with `4` workers by default, scalable based on CPU cores.

## Adaptive Difficulty Logic
The game dynamically adjusts difficulty based on player performance:

### 1. Difficulty Scaling
*   **Increment (Correct)**: Difficulty increases by `1 / floor(Current Difficulty)`. This means it gets harder to advance at higher levels.
*   **Decrement (Incorrect)**: Difficulty decreases by `1 / floor(Current Difficulty)`.

### 2. Scoring System
*   **Base Score**: 10 points * Difficulty Level.
*   **Streak Multiplier**:
    *   Increases by **0.1x** per consecutive correct answer.
    *   Capped at **2.5x**.
*   **Accuracy Multiplier**: Your daily accuracy affects the score:
    *   **1.0x** (76-100% Accuracy)
    *   **0.9x** (51-75% Accuracy)
    *   **0.75x** (21-50% Accuracy)
    *   **0.5x** (0-20% Accuracy)

### 3. Penalties
*   **Incorrect Answers**: Deducts points based on **(1 - Daily Accuracy) * 20**. Mistakes cost more if your overall accuracy is low.