# 🏗️ System Patterns - AI Trading Team Vietnam

## Architecture Overview

### High-Level Architecture
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit UI  │ ←→ │  Agent Manager   │ ←→ │  Data Sources   │
│   (Frontend)    │    │   (Core Logic)   │    │  (VNStocks API) │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         ↓                       ↓                       ↓
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Components    │    │   AI Agents      │    │   Data Models   │
│   (UI Widgets)  │    │  (3 Specialists) │    │  (VNStockData)  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Core Design Patterns

#### 1. Multi-Agent Pattern
**Purpose**: Simulate collaborative investment team decision-making

```python
class BaseAgent(ABC):
    """Abstract base for all trading agents"""
    - personality: AgentPersonality
    - model: GenerativeModel
    - conversation_history: List
    
    @abstractmethod
    async def analyze(context, team_discussion) -> AgentResponse
```

**Specialized Agents**:
- `MarketAnalystAgent`: Technical and fundamental analysis
- `RiskManagerAgent`: Risk assessment and position sizing  
- `PortfolioManagerAgent`: Portfolio optimization and allocation

#### 2. Agent Manager Pattern
**Purpose**: Orchestrate multi-agent discussions and consensus building

```python
class AgentManager:
    """Facilitates agent interactions and discussions"""
    - agents: Dict[str, BaseAgent]
    - facilitate_discussion(context, rounds=3) -> List[AgentResponse]
    - get_team_summary() -> Dict
```

**Discussion Flow**:
1. **Round 1**: Initial analysis from each agent
2. **Round 2**: Agents respond to each other's views
3. **Round 3**: Final consensus and recommendations

#### 3. Data Layer Pattern
**Purpose**: Abstracted data access with caching and fallback

```python
class VNStockAPIVNStocks:
    """Real-time Vietnamese stock market data"""
    - cache: Dict (5-minute TTL)
    - get_stock_data(symbol) -> VNStockData
    - get_market_overview() -> MarketContext
    - get_historical_data(symbol, days) -> List[Dict]
```

**Fallback Strategy**:
1. Try VNStocks API (real data)
2. Use cached data if available
3. Generate realistic mock data
4. Basic fallback data

#### 4. Component-Based UI Pattern
**Purpose**: Modular, reusable UI components

```python
# UI Components Structure
src/ui/
├── main_dashboard.py     # Main orchestrator
├── components.py         # Reusable widgets
└── styles.py            # CSS and styling
```

**Key Components**:
- `render_agent_card()`: Individual agent display
- `render_stock_chart()`: Interactive price charts
- `render_performance_metrics()`: Financial metrics display

## Component Relationships

### 1. Data Flow Architecture
```
VNStocks API → VNStockAPIVNStocks → MarketContext → AgentManager → Agents → UI
     ↓              ↓                    ↓             ↓         ↓      ↓
  Real Data    Cached/Processed    Context Object   Analysis   Results  Display
```

### 2. Agent Interaction Pattern
```
User Input → Agent Manager → [Agent 1, Agent 2, Agent 3] → Discussion Rounds → Consensus
                ↓                      ↓                        ↓              ↓
            Market Context        Individual Analysis     Cross-Agent Debate   Final Recommendation
```

### 3. State Management
```python
# Streamlit Session State
st.session_state = {
    'conversation_history': List[Dict],
    'portfolio_data': List[Dict], 
    'agent_manager': AgentManager,
    'selected_stock_input': str
}
```

## Key Technical Decisions

### 1. Asynchronous Processing
**Decision**: Use async/await for all data fetching and AI generation
**Rationale**: 
- Improves UI responsiveness
- Allows concurrent agent processing
- Better handling of API timeouts

```python
async def generate_response(self, prompt: str) -> str:
    response = await asyncio.to_thread(
        self.model.generate_content, full_prompt
    )
```

### 2. Caching Strategy
**Decision**: 5-minute cache for market data, no cache for agent responses
**Rationale**:
- Market data changes slowly during trading hours
- Agent responses should be fresh for each analysis
- Balances performance with accuracy

### 3. Error Handling Philosophy
**Decision**: Graceful degradation with fallbacks
**Rationale**:
- System remains functional even with API failures
- Users get value even with limited data
- Transparent about data quality/source

```python
try:
    real_data = await vnstocks_api_call()
    return real_data
except Exception:
    logger.warning("API failed, using fallback")
    return generate_realistic_mock()
```

### 4. Agent Personality System
**Decision**: Rich personality definitions with speaking styles
**Rationale**:
- Creates engaging, differentiated agent interactions
- Educational value through diverse perspectives
- More realistic simulation of team dynamics

```python
@dataclass
class AgentPersonality:
    name: str
    role: str
    experience: str
    personality_traits: List[str]
    speaking_style: str
    background: str
    strengths: List[str]
    weaknesses: List[str]
```

## Integration Patterns

### 1. Google Gemini Integration
**Pattern**: Model fallback with error handling
```python
model_names = [
    'gemini-1.5-flash',    # Primary
    'gemini-1.5-pro',      # Fallback 1
    'gemini-1.0-pro'       # Fallback 2
]
```

### 2. VNStocks Integration
**Pattern**: Data transformation and validation
```python
# API returns prices in thousands, convert to VND
price = float(current_price) * 1000
market_cap = (issue_share * current_price * 1000) / 1_000_000_000
```

### 3. Streamlit Integration
**Pattern**: Component-based rendering with state management
```python
def main():
    initialize_session_state()
    dashboard = TradingDashboard()
    dashboard.render_header()
    dashboard.render_sidebar()
    # ... other components
```

## Performance Optimizations

### 1. Concurrent Agent Processing
```python
# Process agents in parallel
tasks = [agent.analyze(context) for agent in agents]
responses = await asyncio.gather(*tasks)
```

### 2. Smart Caching
- Market data: 5-minute cache
- Historical data: 15-minute cache
- News sentiment: 30-minute cache

### 3. Progressive Loading
- Show market overview immediately
- Load agent analysis progressively
- Display results as they become available

## Security Patterns

### 1. API Key Management
- User-provided API keys (not stored)
- Input validation and sanitization
- Secure handling in session state

### 2. Data Validation
```python
def validate_stock_symbol(symbol: str) -> bool:
    return (
        len(symbol) >= 3 and 
        len(symbol) <= 5 and 
        symbol.isalpha()
    )
```

### 3. Error Information Disclosure
- Log detailed errors for debugging
- Show user-friendly messages to users
- No sensitive information in UI errors

## Scalability Considerations

### 1. Stateless Design
- Each analysis is independent
- No persistent user state
- Easy horizontal scaling

### 2. Configurable Agents
- Agent personalities loaded from config
- Easy to add new agents
- Modular agent capabilities

### 3. Data Source Abstraction
- Easy to swap data providers
- Multiple fallback sources
- Consistent data interface

## Testing Patterns

### 1. Component Testing
- Individual agent testing
- Data layer testing
- UI component testing

### 2. Integration Testing
- End-to-end analysis flows
- API integration testing
- Multi-agent interaction testing

### 3. Mock Data Testing
- Fallback data generation
- Edge case handling
- Performance under load 