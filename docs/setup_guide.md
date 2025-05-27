# 🚀 Setup Guide - AI Trading Team Vietnam

Chi tiết hướng dẫn cài đặt và sử dụng hệ thống AI Trading Team Vietnam.

## 📋 Yêu cầu hệ thống

### Minimum Requirements
- **Python**: 3.8+ (Recommended: 3.9 hoặc 3.10)
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space
- **Internet**: Stable connection for API calls
- **OS**: Windows 10+, macOS 10.14+, Ubuntu 18.04+

### Recommended Setup
- **Python**: 3.10
- **RAM**: 16GB
- **CPU**: Multi-core processor
- **Storage**: SSD with 5GB+ free space
- **Internet**: Broadband connection

## 🛠️ Installation Steps

### Bước 1: Clone Repository

```bash
# Clone project
git clone https://github.com/your-username/ai-trading-team-vietnam.git
cd ai-trading-team-vietnam

# Check structure
ls -la
```

### Bước 2: Setup Python Environment

#### Option A: Using venv (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Verify activation
which python  # Should show path to venv
```

#### Option B: Using conda
```bash
# Create conda environment
conda create -n ai-trading python=3.10
conda activate ai-trading
```

### Bước 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# Verify installation
pip list | grep streamlit
pip list | grep google-generativeai
```

### Bước 4: Configuration Setup

#### 4.1: Create Configuration File
```bash
# Copy sample config
cp config.sample.json config.json

# Edit config file
nano config.json  # Linux/macOS
notepad config.json  # Windows
```

#### 4.2: Get Google GenAI API Key

1. **Truy cập Google AI Studio**:
   - Vào: https://makersuite.google.com/app/apikey
   - Đăng nhập với Google account

2. **Tạo API Key**:
   - Click "Create API Key"
   - Chọn project hoặc tạo mới
   - Copy API key (giữ bí mật!)

3. **Setup trong config**:
```json
{
  "api": {
    "google_genai_api_key": "YOUR_API_KEY_HERE"
  }
}
```

#### 4.3: Environment Variables (Optional)
```bash
# Create .env file
touch .env

# Add API key
echo "GOOGLE_GENAI_API_KEY=your_api_key_here" >> .env
echo "DEBUG_MODE=false" >> .env
```

### Bước 5: Test Installation

```bash
# Test basic imports
python -c "
import streamlit as st
import google.generativeai as genai
import pandas as pd
import plotly.graph_objects as go
print('✅ All imports successful!')
"

# Test file structure
python -c "
import sys
sys.path.append('src')
from agents.base_agent import BaseAgent
from data.vn_stock_api import VNStockAPI
print('✅ Project structure correct!')
"
```

### Bước 6: Launch Application

```bash
# Start Streamlit app
streamlit run app.py

# Or with custom configuration
streamlit run app.py --server.port 8080
```

## 🔧 Configuration Details

### config.json Structure
```json
{
  "api": {
    "google_genai_api_key": "your-key-here",
    "timeout": 30,
    "max_retries": 3
  },
  "agents": {
    "model_name": "gemini-pro",
    "max_tokens": 2048,
    "temperature": 0.7,
    "conversation_memory": 5
  },
  "ui": {
    "theme": "light",
    "page_title": "🇻🇳 AI Trading Team Vietnam",
    "layout": "wide"
  },
  "trading": {
    "max_position_size": 0.10,
    "max_sector_exposure": 0.30,
    "min_cash_reserve": 0.15
  },
  "debug_mode": false,
  "enable_caching": true,
  "cache_duration": 300
}
```

### Environment Variables
```bash
# .env file
GOOGLE_GENAI_API_KEY=your_api_key_here
DEBUG_MODE=false
CACHE_DURATION=300
LOG_LEVEL=INFO
```

## 🚨 Troubleshooting

### Common Issues & Solutions

#### Issue 1: Import Errors
```bash
# Error: ModuleNotFoundError: No module named 'streamlit'
# Solution:
pip install --upgrade streamlit

# Error: No module named 'src.agents'
# Solution: Check you're running from project root
pwd  # Should show ai-trading-team-vietnam/
python app.py  # Not python src/app.py
```

#### Issue 2: API Key Problems
```bash
# Error: Invalid API key
# Solution:
1. Verify API key is correct (no extra spaces)
2. Check Google AI Studio for key status
3. Regenerate key if necessary
4. Ensure key has proper permissions
```

#### Issue 3: Port Already in Use
```bash
# Error: Port 8501 is already in use
# Solution:
streamlit run app.py --server.port 8080

# Or kill existing process:
lsof -ti:8501 | xargs kill -9  # macOS/Linux
netstat -ano | findstr :8501  # Windows
```

#### Issue 4: Memory Issues
```bash
# Error: Out of memory
# Solutions:
1. Close other applications
2. Reduce cache duration in config
3. Restart the application
4. Use lighter model settings
```

#### Issue 5: Permission Errors
```bash
# Error: Permission denied
# Solution on Linux/macOS:
sudo chown -R $USER:$USER .
chmod +x app.py

# Solution on Windows:
# Run terminal as Administrator
```

### Performance Optimization

#### 1. Caching Configuration
```json
{
  "enable_caching": true,
  "cache_duration": 300,
  "cache_dir": "data/cache"
}
```

#### 2. Memory Management
```python
# In config.json
{
  "agents": {
    "conversation_memory": 3,  # Reduce from 5
    "max_tokens": 1024         # Reduce from 2048
  }
}
```

#### 3. API Optimization
```json
{
  "api": {
    "timeout": 20,      # Reduce timeout
    "max_retries": 2    # Reduce retries
  }
}
```

## 🐳 Docker Setup (Advanced)

### Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Docker Commands
```bash
# Build image
docker build -t ai-trading-vietnam .

# Run container
docker run -p 8501:8501 \
  -e GOOGLE_GENAI_API_KEY=your_key_here \
  ai-trading-vietnam

# Run with volume mount
docker run -p 8501:8501 \
  -v $(pwd)/data:/app/data \
  -e GOOGLE_GENAI_API_KEY=your_key_here \
  ai-trading-vietnam
```

### Docker Compose
```yaml
# docker-compose.yml
version: '3.8'

services:
  ai-trading:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GOOGLE_GENAI_API_KEY=${GOOGLE_GENAI_API_KEY}
      - DEBUG_MODE=false
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    restart: unless-stopped

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

volumes:
  redis_data:
```

## 🌐 Deployment Options

### 1. Streamlit Cloud (Free)

#### Setup Steps:
1. **Push to GitHub**:
```bash
git add .
git commit -m "Initial deployment"
git push origin main
```

2. **Deploy on Streamlit Cloud**:
   - Vào: https://share.streamlit.io
   - Connect GitHub repository
   - Add secrets in dashboard:
     ```
     GOOGLE_GENAI_API_KEY = "your_api_key"
     ```

3. **Custom Domain** (Optional):
   - Add CNAME record pointing to your-app.streamlit.app

#### Streamlit Secrets Management:
```toml
# .streamlit/secrets.toml
[api]
google_genai_api_key = "your_api_key_here"

[trading]
max_position_size = 0.10
```

### 2. Heroku Deployment

#### Setup:
```bash
# Install Heroku CLI
curl https://cli-assets.heroku.com/install.sh | sh

# Login
heroku login

# Create app
heroku create ai-trading-vietnam

# Set environment variables
heroku config:set GOOGLE_GENAI_API_KEY=your_key_here

# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Deploy
git push heroku main
```

#### Heroku Configuration:
```json
// app.json
{
  "name": "AI Trading Team Vietnam",
  "description": "Vietnamese stock market analysis with AI agents",
  "keywords": ["vietnam", "stock", "ai", "trading"],
  "env": {
    "GOOGLE_GENAI_API_KEY": {
      "description": "Google GenAI API Key",
      "required": true
    }
  },
  "buildpacks": [
    {"url": "heroku/python"}
  ]
}
```

### 3. Railway Deployment

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
railway deploy
```

### 4. VPS Deployment (Advanced)

#### Nginx Configuration:
```nginx
# /etc/nginx/sites-available/ai-trading
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }
}
```

#### Systemd Service:
```ini
# /etc/systemd/system/ai-trading.service
[Unit]
Description=AI Trading Team Vietnam
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/ai-trading-team-vietnam
Environment=PATH=/home/ubuntu/ai-trading-team-vietnam/venv/bin
ExecStart=/home/ubuntu/ai-trading-team-vietnam/venv/bin/streamlit run app.py --server.port 8501
Restart=always

[Install]
WantedBy=multi-user.target
```

## 📊 Monitoring & Logging

### Application Logs
```python
# Enable logging in config.json
{
  "debug_mode": true,
  "log_level": "INFO",
  "logs_dir": "logs"
}
```

### Log Files Structure:
```
logs/
├── app.log              # Main application log
├── agents.log           # AI agents interactions
├── api.log              # API calls and responses
└── errors.log           # Error tracking
```

### Performance Monitoring:
```python
# Add to config.json
{
  "monitoring": {
    "enable_metrics": true,
    "metrics_interval": 60,
    "performance_tracking": true
  }
}
```

## 🔒 Security Best Practices

### 1. API Key Security
```bash
# Never commit API keys
echo "*.env" >> .gitignore
echo "config.json" >> .gitignore
echo "*.key" >> .gitignore

# Use environment variables
export GOOGLE_GENAI_API_KEY="your_key"
```

### 2. Application Security
```python
# In production, add rate limiting
RATE_LIMIT = {
    "requests_per_minute": 60,
    "requests_per_hour": 1000
}

# Add HTTPS in production
SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block"
}
```

### 3. Data Privacy
- Không lưu trữ personal financial data
- Cache chỉ chứa public market data
- Logs không chứa sensitive information

## 📱 Mobile Optimization

### Responsive Design:
```python
# Mobile-friendly settings
MOBILE_CONFIG = {
    "sidebar_default_collapsed": True,
    "chart_height": 300,
    "table_max_rows": 10
}
```

### PWA Support (Progressive Web App):
```html
<!-- In custom HTML -->
<link rel="manifest" href="manifest.json">
<meta name="viewport" content="width=device-width, initial-scale=1">
```

## 🧪 Testing Setup

### Unit Tests:
```bash
# Install test dependencies
pip install pytest pytest-asyncio pytest-cov

# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=src tests/

# Run specific test
python -m pytest tests/test_agents.py::test_market_analyst
```

### Integration Tests:
```bash
# Test API connections
python -m pytest tests/integration/

# Test UI components
python -m pytest tests/ui/
```

## 🆘 Support & Resources

### Getting Help:
1. **Documentation**: Check `/docs` folder
2. **GitHub Issues**: Report bugs và feature requests
3. **Community**: Join discussion on GitHub
4. **Email**: Contact maintainers

### Useful Commands:
```bash
# Check system info
python --version
pip --version
streamlit version

# Clear cache
streamlit cache clear

# Reset configuration
rm config.json && cp config.sample.json config.json

# Update dependencies
pip install --upgrade -r requirements.txt
```

### Development Tools:
```bash
# Code formatting
pip install black isort flake8
black src/
isort src/
flake8 src/

# Pre-commit hooks
pip install pre-commit
pre-commit install
```

---

**🎉 Congratulations!** 

Bạn đã setup thành công AI Trading Team Vietnam. Giờ có thể bắt đầu phân tích chứng khoán với đội ngũ AI chuyên nghiệp!

**Next Steps:**
1. Thử phân tích một vài cổ phiếu yêu thích
2. Explore các tính năng advanced
3. Customize agents theo sở thích
4. Share feedback để improve system