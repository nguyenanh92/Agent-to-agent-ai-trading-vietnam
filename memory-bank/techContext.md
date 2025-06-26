# 💻 Technical Context - AI Trading Team Vietnam

## Technology Stack

### Core Technologies

#### **Python 3.8+**
- **Primary Language**: All backend logic and data processing
- **Version**: 3.8+ required for async features and type hints
- **Key Features Used**: AsyncIO, dataclasses, type hints, f-strings

#### **Google Gemini (GenAI)**
- **AI Engine**: Powers all three trading agents
- **Models Used**: 
  - Primary: `gemini-1.5-flash` (fast, cost-effective)
  - Fallback: `gemini-1.5-pro` (higher quality)
  - Last resort: `gemini-1.0-pro` (stable)
- **API**: google-generativeai>=0.3.0

#### **Streamlit**
- **Web Framework**: Modern UI with minimal code
- **Version**: >=1.28.0
- **Features**: Real-time updates, session state, custom CSS
- **Deployment**: Streamlit Cloud ready

#### **VNStocks**
- **Data Source**: Official Vietnamese stock market API
- **Version**: >=3.2.0  
- **Coverage**: HOSE, HNX, UPCOM exchanges
- **Features**: Real-time quotes, historical data, company info

### Supporting Libraries

#### **Data Processing**
```python
pandas>=2.0.0          # Data manipulation and analysis
numpy>=1.24.0          # Numerical computations
```

#### **Visualization**
```python
plotly>=5.17.0         # Interactive charts and graphs
```

#### **HTTP & Networking**
```python
requests>=2.31.0       # HTTP requests
aiohttp>=3.8.0         # Async HTTP client
```

#### **Configuration**
```python
python-dotenv>=1.0.0   # Environment variable management
```

#### **Async Support**
```python
asyncio-mqtt>=0.11.0   # Async MQTT (if needed for real-time data)
```

## Development Setup

### Environment Setup
```bash
# 1. Clone repository
git clone https://github.com/huudatscience/Agent-to-agent-ai-trading-vietnam
cd Agent-to-agent-ai-trading-vietnam

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt
```

### Required API Keys
1. **Google GenAI API Key**
   - Get from: https://makersuite.google.com/app/apikey
   - Required for AI agent functionality
   - Free tier available with quotas

### Running the Application
```bash
# Development
streamlit run app.py

# Production
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

### Project Structure
```
Agent-to-agent-ai-trading-vietnam/
├── app.py                          # Main entry point
├── requirements.txt                # Dependencies
├── README.md                       # Project documentation
├── memory-bank/                    # Memory bank files
├── docs/                          # Additional documentation
└── src/                           # Source code
    ├── agents/                    # AI agents
    │   ├── base_agent.py          # Base agent class
    │   ├── market_analyst.py      # Market analysis agent
    │   ├── risk_manager.py        # Risk management agent
    │   └── portfolio_manager.py   # Portfolio management agent
    ├── data/                      # Data layer
    │   ├── vn_stock_api_vnstocks.py  # VNStocks integration
    │   └── vn_stock_api.py           # Legacy API (deprecated)
    ├── ui/                        # User interface
    │   ├── main_dashboard.py      # Main dashboard
    │   ├── components.py          # UI components
    │   └── styles.py              # CSS styling
    └── utils/                     # Utilities
        ├── config.py              # Configuration
        └── helpers.py             # Helper functions
```

## Technical Constraints

### API Limitations

#### **Google Gemini**
- **Rate Limits**: 
  - Free tier: 15 requests/minute, 1500 requests/day
  - Paid tier: Higher limits based on plan
- **Token Limits**: 
  - Input: 1M tokens per request
  - Output: 8192 tokens per response
- **Latency**: 2-5 seconds per request

#### **VNStocks**
- **Rate Limits**: No official limits, but respectful usage recommended
- **Data Freshness**: 15-minute delay for free data
- **Market Hours**: Data availability during Vietnamese trading hours
- **Reliability**: Occasional API timeouts handled with fallbacks

### Performance Constraints

#### **Memory Usage**
- **Streamlit Session State**: Limited by browser memory
- **Data Caching**: 5-minute TTL to balance performance vs freshness
- **Historical Data**: Limited to 90 days for technical analysis

#### **Response Times**
- **Agent Analysis**: 3-5 seconds per agent (parallel processing)
- **Data Fetching**: 1-2 seconds for market data
- **Total Analysis Time**: 8-15 seconds for complete analysis

### Platform Constraints

#### **Streamlit Limitations**
- **Single-threaded**: UI updates block during processing
- **Session State**: Data lost on page refresh
- **File Upload**: Limited to 200MB per file
- **Deployment**: Limited to Streamlit Cloud specifications

#### **Browser Compatibility**
- **Modern Browsers**: Chrome 90+, Firefox 88+, Safari 14+
- **Mobile**: Responsive design but optimized for desktop
- **JavaScript**: Minimal JS requirements (Streamlit handles most)

## Data Architecture

### Data Models

#### **VNStockData**
```python
@dataclass
class VNStockData:
    symbol: str
    price: float                    # Price in VND
    change: float                   # Change in VND
    change_percent: float           # Percentage change
    volume: int                     # Trading volume
    market_cap: float              # Market cap in billion VND
    pe_ratio: Optional[float]       # P/E ratio
    pb_ratio: Optional[float]       # P/B ratio
    sector: str                     # Business sector
    exchange: str                   # HOSE, HNX, UPCOM
    # Technical indicators
    rsi: Optional[float]
    sma_20: Optional[float]
    sma_50: Optional[float]
    # Additional metrics...
```

#### **MarketContext**
```python
@dataclass
class MarketContext:
    symbol: str
    current_price: float
    market_cap: float
    volume: float
    pe_ratio: Optional[float]
    pb_ratio: Optional[float]
    sector: str
    market_trend: str
    news_sentiment: str
```

### Caching Strategy
```python
# Cache configuration
self.cache_duration = 300  # 5 minutes
self.cache = {
    'stock_data': {},      # Individual stock data
    'market_overview': {}, # Market overview
    'historical_data': {}  # Historical price data
}
```

## Security Considerations

### API Key Security
- **User-Provided**: API keys entered by users, not stored
- **Session-Only**: Keys exist only in Streamlit session state
- **No Logging**: API keys never logged or persisted

### Data Privacy
- **No User Data Storage**: No personal information collected
- **Session-Based**: All data cleared on session end
- **Local Processing**: Analysis happens locally, not stored remotely

### Input Validation
```python
def validate_stock_symbol(symbol: str) -> bool:
    """Validate stock symbol format"""
    return (
        len(symbol) >= 3 and 
        len(symbol) <= 5 and 
        symbol.isalpha() and
        symbol.isupper()
    )
```

## Deployment Architecture

### Local Development
- **Streamlit Dev Server**: `streamlit run app.py`
- **Hot Reload**: Automatic reloading on file changes
- **Debug Mode**: Detailed error messages and stack traces

### Production Deployment
- **Streamlit Cloud**: Primary deployment platform
- **Environment Variables**: API keys and configuration
- **Resource Limits**: CPU and memory constraints
- **HTTPS**: Automatic SSL certificate

### Alternative Deployment Options
- **Docker**: Containerized deployment
- **Heroku**: Platform-as-a-Service deployment
- **AWS/GCP**: Cloud infrastructure deployment

## Monitoring and Logging

### Application Logging
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Usage patterns
logger.info("✅ Agent analysis completed")
logger.warning("⚠️ API timeout, using cached data")
logger.error("❌ Failed to fetch market data")
```

### Performance Monitoring
- **Response Times**: Track agent analysis duration
- **API Success Rates**: Monitor VNStocks and Gemini availability
- **Error Rates**: Track and categorize errors
- **Cache Hit Rates**: Monitor caching effectiveness

### User Analytics (Privacy-Friendly)
- **Usage Patterns**: Popular stocks analyzed
- **Feature Usage**: Which components used most
- **Performance Metrics**: Load times and error rates
- **No Personal Data**: No user identification or tracking

## Development Guidelines

### Code Style
- **PEP 8**: Python style guide compliance
- **Type Hints**: All functions have return type annotations
- **Docstrings**: Google-style docstrings for all classes/functions
- **Comments**: Vietnamese comments for business logic

### Error Handling
```python
try:
    result = risky_operation()
    return result
except SpecificException as e:
    logger.warning(f"Expected error: {e}")
    return fallback_result()
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise
```

### Testing Strategy
- **Unit Tests**: Individual component testing
- **Integration Tests**: API integration testing
- **UI Tests**: Streamlit component testing
- **Manual Testing**: End-to-end user journey testing

### Version Control
- **Git**: Version control with meaningful commit messages
- **Branching**: Feature branches for new development
- **Documentation**: Update memory bank with significant changes 