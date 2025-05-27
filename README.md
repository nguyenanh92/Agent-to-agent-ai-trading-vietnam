# 🇻🇳 AI Trading Team Vietnam

Hệ thống phân tích đầu tư chứng khoán Việt Nam với 3 AI Agents chuyên nghiệp, sử dụng Google GenAI để mô phỏng cuộc thảo luận thực tế của một investment team.

![AI Trading Team Vietnam](https://img.shields.io/badge/Vietnam-Stock%20Market-red?style=for-the-badge&logo=vietnam)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Google AI](https://img.shields.io/badge/Google_AI-Gemini-4285F4?style=for-the-badge&logo=google)

## 🌟 Tính năng chính

### 👥 3 AI Agents chuyên nghiệp
- **🔍 Nguyễn Minh Anh** - Senior Market Analyst (CFA, 8 năm kinh nghiệm)
- **⚠️ Trần Quốc Bảo** - Senior Risk Manager (FRM, 12 năm kinh nghiệm)  
- **💼 Lê Thị Mai** - Portfolio Manager (MBA INSEAD, 10 năm quản lý fund)

### 🚀 Tính năng nổi bật
- ✅ **Real-time Analysis**: Phân tích real-time với dữ liệu thị trường VN
- ✅ **Multi-Agent Discussion**: Agents tương tác và tranh luận như team thật
- ✅ **Vietnamese Market Focus**: Tối ưu hoá cho HOSE, HNX, UPCOM
- ✅ **Risk Management**: Tích hợp position sizing và risk assessment
- ✅ **Beautiful UI**: Giao diện đẹp với Streamlit
- ✅ **Export Results**: Xuất phân tích dưới dạng JSON

## 🏗️ Kiến trúc hệ thống

```
ai-trading-team-vietnam/
│
├── 📁 src/                          # Source code chính
│   ├── 📁 agents/                   # AI Agents
│   │   ├── base_agent.py           # Base class
│   │   ├── market_analyst.py       # Market Analyst Agent
│   │   ├── risk_manager.py         # Risk Manager Agent
│   │   └── portfolio_manager.py    # Portfolio Manager Agent
│   │
│   ├── 📁 data/                     # Data handling
│   │   ├── vn_stock_api.py         # VN stock market APIs
│   │   ├── news_scraper.py         # News sentiment analysis
│   │   └── market_data.py          # Market data processing
│   │
│   ├── 📁 ui/                       # User Interface
│   │   ├── main_dashboard.py       # Main Streamlit app
│   │   ├── components.py           # UI components
│   │   └── styles.py               # CSS styling
│   │
│   └── 📁 utils/                    # Utilities
│       ├── config.py               # Configuration management
│       ├── helpers.py              # Helper functions
│       └── constants.py            # VN market constants
│
├── 📁 data/                         # Data storage
├── 📁 tests/                        # Unit tests
├── 📁 docs/                         # Documentation
├── requirements.txt                 # Dependencies
├── app.py                          # Main entry point
└── README.md                       # This file
```

## 🚀 Quick Start

### 1. Cài đặt Dependencies

```bash
# Clone repository
git clone https://github.com/your-username/ai-trading-team-vietnam.git
cd ai-trading-team-vietnam

# Tạo virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Lấy Google GenAI API Key

1. Truy cập [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Đăng nhập với Google account
3. Tạo API key mới
4. Copy và giữ bí mật API key

### 3. Chạy ứng dụng

```bash
streamlit run app.py
```

### 4. Sử dụng

1. Mở browser tại `http://localhost:8501`
2. Nhập Google GenAI API key ở sidebar
3. Chọn cổ phiếu muốn phân tích
4. Thiết lập số tiền và mức độ rủi ro
5. Bấm "🚀 Bắt đầu phân tích"
6. Xem cuộc thảo luận của AI team

## 📊 Supported Stocks

Hệ thống hỗ trợ các bluechips chính của thị trường Việt Nam:

### 🏦 Banking
- **VCB** - Vietcombank
- **BID** - BIDV  
- **CTG** - VietinBank
- **TCB** - Techcombank
- **ACB** - ACB

### 🏢 Real Estate
- **VIC** - Vingroup
- **VHM** - Vinhomes
- **VRE** - Vincom Retail
- **DXG** - Dat Xanh Group

### 🛒 Consumer
- **MSN** - Masan Group
- **MWG** - Mobile World
- **VNM** - Vinamilk
- **SAB** - Sabeco

### 🏭 Industrial & Utilities
- **HPG** - Hoa Phat Group
- **GAS** - PetroVietnam Gas
- **PLX** - Petrolimex

### 💻 Technology  
- **FPT** - FPT Corporation

## 🔧 Configuration

### Environment Variables
```bash
# .env file
GOOGLE_GENAI_API_KEY=your_api_key_here
DEBUG_MODE=false
CACHE_DURATION=300
```

### Config File
```json
{
  "api": {
    "google_genai_api_key": "your-api-key",
    "timeout": 30,
    "max_retries": 3
  },
  "trading": {
    "max_position_size": 0.10,
    "max_sector_exposure": 0.30,
    "min_cash_reserve": 0.15
  }
}
```

## 🎯 Workflow của AI Team

### 1. Market Analyst (Minh Anh) 🔍
- Phân tích technical: RSI, MACD, Bollinger Bands
- Fundamental analysis: P/E, P/B, growth metrics
- Volume analysis và money flow
- Sector comparison và relative strength

### 2. Risk Manager (Quốc Bảo) ⚠️
- Position sizing calculations (Kelly Criterion)
- Risk assessment: VaR, maximum drawdown
- Portfolio correlation analysis
- Stop-loss và exit strategy
- Stress testing scenarios

### 3. Portfolio Manager (Thị Mai) 💼
- Synthesis team inputs
- Final investment decision
- Strategic asset allocation
- Performance attribution
- Stakeholder communication

## 📈 Sample Analysis Output

```json
{
  "stock": "VCB",
  "final_recommendation": "BUY",
  "confidence_level": 8.5,
  "consensus_level": "HIGH",
  "team_analysis": {
    "market_analyst": {
      "recommendation": "BUY",
      "confidence": 9,
      "key_points": ["Technical breakout", "Strong volume", "Sector leader"]
    },
    "risk_manager": {
      "recommendation": "BUY",
      "confidence": 7,
      "position_size": "5% of portfolio",
      "stop_loss": "80,000 VND"
    },
    "portfolio_manager": {
      "recommendation": "BUY", 
      "confidence": 9,
      "strategy": "Core holding for banking exposure"
    }
  }
}
```

## 🧪 Testing

```bash
# Run unit tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_agents.py

# Run with coverage
python -m pytest --cov=src tests/
```

## 🚀 Deployment

### Streamlit Cloud
1. Push code lên GitHub
2. Vào [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub repository
4. Add API key vào Secrets

### Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.headless", "true"]
```

### Heroku
```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT --server.headless=true" > Procfile

# Deploy
git push heroku main
```

## 🎓 Educational Value

### Cho Newbie Investors
- Hiểu cách đọc P/E, P/B ratios
- Risk management cơ bản
- Portfolio diversification
- Technical analysis introduction

### Cho Experienced Traders  
- Advanced position sizing techniques
- Multi-factor analysis approach
- Risk-adjusted returns calculation
- Professional decision-making process

### Cho Developers
- Multi-agent AI system design
- Streamlit advanced patterns
- API integration best practices
- Vietnamese market data handling

## 🤝 Contributing

Chúng tôi welcome contributions! Xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết chi tiết.

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Setup pre-commit hooks
pre-commit install

# Run linting
black src/
flake8 src/
```

## 📝 License

Dự án này được licensed dưới [MIT License](LICENSE).

## ⚠️ Disclaimer

- **Không phải lời khuyên đầu tư**: Đây là công cụ hỗ trợ phân tích, không thay thế judgment cá nhân
- **Đầu tư có rủi ro**: Có thể mất một phần hoặc toàn bộ vốn đầu tư
- **Due diligence**: Luôn thực hiện nghiên cứu riêng trước khi đầu tư
- **Demo purposes**: Một số data là simulated cho mục đích demo

## 🆘 Support & Contact

- **GitHub Issues**: [Report bugs và feature requests](https://github.com/your-username/ai-trading-team-vietnam/issues)
- **Email**: your-email@example.com
- **Documentation**: [Xem docs đầy đủ](https://your-docs-site.com)

## 🏆 Roadmap

### Version 2.0
- [ ] Real-time WebSocket data feeds
- [ ] Advanced charting với TradingView
- [ ] Backtesting engine
- [ ] Portfolio optimization algorithms
- [ ] Mobile responsive design

### Version 3.0
- [ ] Crypto trading support
- [ ] Options và derivatives analysis
- [ ] ESG scoring integration
- [ ] Social trading features
- [ ] AI-powered news summarization

### Version 4.0
- [ ] Multi-language support (English)
- [ ] Regional markets expansion (Thailand, Singapore)
- [ ] Advanced ML models
- [ ] Automated trading execution
- [ ] Institutional features

## 🎉 Acknowledgments

- **Google AI** - For providing Gemini API
- **Vietnamese Stock Exchanges** - HOSE, HNX, UPCOM
- **Open Source Community** - For amazing libraries
- **Vietnamese Investor Community** - For feedback và support

## 📚 References & Resources

### Vietnamese Stock Market
- [State Securities Commission of Vietnam](https://www.ssc.gov.vn/)
- [Ho Chi Minh Stock Exchange (HOSE)](https://www.hsx.vn/)
- [Hanoi Stock Exchange (HNX)](https://www.hnx.vn/)

### Financial Education
- [CFA Institute](https://www.cfainstitute.org/)
- [FRM Certification](https://www.garp.org/frm)
- [Investopedia Vietnam](https://www.investopedia.com/)

### Technical Resources  
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google AI Documentation](https://ai.google.dev/)
- [Plotly Python](https://plotly.com/python/)

---

**Made with ❤️ for Vietnamese Investors**

*Disclaimer: This is an educational tool and should not be considered as financial advice. Always consult with qualified financial advisors and conduct your own research before making investment decisions.*