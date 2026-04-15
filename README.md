
# 🪁 Kite Lite: Real-Time Quant Stock Analyzer

**Kite Lite** is a high-performance, real-time Indian stock market dashboard. It features live WebSocket price streaming, dynamic market heatmaps, and a custom Quantitative Analysis engine that instantly calculates technical health scores. It delivers an institutional-grade trading visualization experience completely for free, without requiring paid broker APIs.

## ✨ Key Features
* **Real-Time Data Streaming:** Live price updates pushed via WebSockets (No manual refreshing).
* **Anti-Blocking Architecture:** Uses bulk-polling (`yahooquery`) and session spoofing to prevent IP bans from data providers.
* **Quantitative Analysis Engine:** Dynamically calculates RSI, MACD, and Simple Moving Averages (SMA) using pure Pandas.
* **Algorithmic Health Score:** Evaluates momentum and trend strength to generate a 0-100 score and classify stocks as BUY, HOLD, or WATCH.
* **Zero-Build Frontend:** Lightweight, blazing-fast UI built with vanilla JavaScript, Tailwind CSS, and Chart.js.

---

## 🏗️ System Architecture

The system follows a modular, decoupled architecture separating the real-time data ingestion from the heavy quantitative calculations.

```text
[ External APIs ]                      [ FastAPI Backend ]                       [ Frontend Client ]
                      
 Yahoo Finance  ====(Bulk Query)====> Market Data Service =======(WebSockets)======> Live Chart & 
 (Live Quotes)                        (State Management)                               Heatmap
                                                                                        ||
                                                                                        || (REST API)
                                                                                        \/
 Yahoo Finance  ====(Historical)====> Quant Analysis Engine ======(JSON)==========> AI Analysis 
 (1-Year Data)                        (Pandas, cachetools)                            Dashboard
```

### 🧰 Tech Stack
* **Backend:** Python 3.11, FastAPI, Uvicorn, Asyncio, WebSockets
* **Data & Quant:** Pandas, `yfinance`, `yahooquery`, `cachetools`
* **Frontend:** HTML5, Vanilla JavaScript, Tailwind CSS (via CDN), Chart.js

---

## 📁 Project Structure

```text
market_dash/
│
├── backend/
│   ├── main.py                 # FastAPI app & WebSocket connection manager
│   ├── requirements.txt        # Python dependencies
│   ├── services/
│   │   ├── __init__.py
│   │   └── market_data.py      # Real-time bulk polling via yahooquery
│   └── analysis/               
│       ├── __init__.py
│       ├── indicators.py       # Mathematical calculations (RSI, MACD, SMA)
│       ├── scoring.py          # Logic for the 0-100 Health Score
│       ├── report_engine.py    # Natural language insights generator
│       └── router.py           # REST endpoints and caching logic
│
├── frontend/
│   └── index.html              # Single-page UI application
│
└── README.md                   # Project documentation
```

---

## 🚀 Step-by-Step Setup Guide

Follow these instructions to run the project on your local machine.

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system. 

### 2. Install Backend Dependencies
Open your terminal, navigate to the `backend` folder, and set up your virtual environment:

```bash
# Navigate to backend directory
cd market_dash/backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

*(Ensure your `requirements.txt` includes: `fastapi`, `uvicorn`, `yfinance`, `yahooquery`, `pandas`, `websockets`, `cachetools`, `requests`)*

### 3. Start the FastAPI Server
Run the Uvicorn server. This will start both the REST API and the WebSocket stream.

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
You should see logs in your terminal indicating that the server has started and is successfully fetching data: `✅ Loaded RELIANCE.NS: ₹...`

### 4. Launch the Frontend UI
Because the frontend is a zero-build vanilla JS application, you do not need Node.js or Webpack.
Simply locate the `frontend/index.html` file in your file explorer and **double-click it to open it in your web browser** (Chrome/Edge/Firefox).

*(Alternatively, if using VS Code, you can use the "Live Server" extension to host the HTML file).*

---

## ⚙️ How It Works (Under the Hood)

1. **The Pulse (WebSocket Loop):** When the server starts, an asynchronous background task begins running. Every 5 seconds, it uses `yahooquery` to make a *single bulk request* for all 10 tracked NIFTY 50 stocks. It updates its internal dictionary (memory) and broadcasts this state to the frontend via WebSockets.
   
2. **The Brain (Analysis Router):** When a user clicks a stock on the frontend, a REST GET request is sent to `/api/analysis/{ticker}`. 
   * The backend downloads 1 year of historical daily data via `yfinance`.
   * **Pandas** calculates moving averages and momentum oscillators.
   * The result is cached using `cachetools` for 15 minutes to prevent redundant API calls and protect against IP rate-limiting.

3. **The Face (Frontend Render):** The frontend maintains a persistent WebSocket connection. As JSON payloads arrive, it surgically updates DOM elements (flashing text green/red) and pushes new data points to the **Chart.js** instance, maintaining a smooth 60fps experience without full-page reloads.
