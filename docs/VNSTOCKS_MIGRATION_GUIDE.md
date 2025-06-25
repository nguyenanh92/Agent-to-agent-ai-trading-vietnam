# 🔄 VNStocks Migration Guide

## Hướng dẫn chuyển đổi từ Mock Data sang VNStocks Real Data

### 📋 Tổng quan

Hệ thống hiện tại sử dụng mock data trong `src/data/vn_stock_api.py`. Với VNStocks, chúng ta có thể thay thế bằng dữ liệu thực từ thị trường chứng khoán Việt Nam.

---

## 🎯 Lợi ích của VNStocks

| **Tiêu chí** | **Mock Data (hiện tại)** | **VNStocks (mới)** |
|--------------|---------------------------|---------------------|
| **Dữ liệu** | Giả lập | Thực tế từ thị trường |
| **Cập nhật** | Không | Thời gian thực |
| **Chi phí** | Miễn phí | Miễn phí |
| **Độ tin cậy** | Thấp | Cao |
| **Tính năng** | Hạn chế | Đầy đủ (báo cáo tài chính, chỉ số, v.v.) |

---

## 🛠️ Cài đặt VNStocks

### 1. Cài đặt thư viện

```bash
# Cài đặt VNStocks
pip install vnstock

# Hoặc cài đặt phiên bản mới nhất
pip install -U vnstock

# Hoặc từ GitHub
pip install git+https://github.com/thinh-vu/vnstock.git
```

### 2. Kiểm tra cài đặt

```bash
# Chạy test script
python test_vnstocks_integration.py
```

---

## 🔄 Migration Steps

### Step 1: Backup hệ thống hiện tại

```bash
# Backup file hiện tại
cp src/data/vn_stock_api.py src/data/vn_stock_api_backup.py
```

### Step 2: Cập nhật import trong các file sử dụng

Tìm và thay thế trong các file:

**Từ:**
```python
from src.data.vn_stock_api import VNStockAPI
```

**Thành:**
```python
from src.data.vn_stock_api_vnstocks import VNStockAPIVNStocks as VNStockAPI
```

### Step 3: Cập nhật khởi tạo API

**Từ:**
```python
api = VNStockAPI()
```

**Thành:**
```python
api = VNStockAPIVNStocks()
```

### Step 4: Test từng chức năng

```python
# Test basic functionality
import asyncio
from src.data.vn_stock_api_vnstocks import VNStockAPIVNStocks

async def test_basic():
    api = VNStockAPIVNStocks()
    
    # Test stock data
    stock_data = await api.get_stock_data('VCB')
    print(f"VCB Price: {stock_data.price:,.0f} VND")
    
    # Test market overview
    market = await api.get_market_overview()
    print(f"VN-Index: {market['vn_index']['value']}")

# Run test
asyncio.run(test_basic())
```

---

## 📊 API Mapping

### Chức năng tương thích 100%

| **Chức năng** | **Interface** | **Status** |
|---------------|---------------|------------|
| `get_stock_data()` | Không đổi | ✅ Compatible |
| `get_market_overview()` | Không đổi | ✅ Compatible |
| `get_historical_data()` | Không đổi | ✅ Compatible |
| `get_available_symbols()` | Không đổi | ✅ Compatible |
| `get_news_sentiment()` | Không đổi | ⚠️ Placeholder |

### Chức năng mới với VNStocks

```python
# Báo cáo tài chính
from vnstock import Company, Finance

company = Company(symbol='VCB', source='VCI')
overview = company.overview()

finance = Finance(symbol='VCB', source='VCI')
balance_sheet = finance.balance_sheet(period='year')
income_statement = finance.income_statement(period='year')

# Bộ lọc cổ phiếu
from vnstock import Screener
screener = Screener()
filtered_stocks = screener.stock(params={"exchangeName": "HOSE"})

# Dữ liệu intraday
stock = Vnstock().stock(symbol='VCB', source='VCI')
intraday = stock.quote.intraday(page_size=1000)
```

---

## 🧪 Testing Strategy

### 1. Unit Tests

```python
# test_vnstocks_unit.py
import unittest
from src.data.vn_stock_api_vnstocks import VNStockAPIVNStocks

class TestVNStocksAPI(unittest.TestCase):
    def setUp(self):
        self.api = VNStockAPIVNStocks()
    
    def test_stock_data_structure(self):
        # Test data structure compatibility
        pass
    
    def test_error_handling(self):
        # Test error scenarios
        pass
```

### 2. Integration Tests

```python
# test_vnstocks_integration.py
async def test_full_workflow():
    """Test complete workflow with VNStocks"""
    api = VNStockAPIVNStocks()
    
    # Test multiple stocks
    symbols = ['VCB', 'TCB', 'BID']
    results = await get_multiple_stocks(symbols)
    
    assert len(results) == len(symbols)
    for symbol, data in results.items():
        assert data.price > 0
        assert data.symbol == symbol
```

### 3. Performance Tests

```python
# test_performance.py
import time
import asyncio

async def benchmark_api_calls():
    """Benchmark VNStocks API performance"""
    api = VNStockAPIVNStocks()
    
    start_time = time.time()
    
    # Test concurrent calls
    tasks = [api.get_stock_data(symbol) for symbol in ['VCB', 'TCB', 'BID']]
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"3 concurrent calls took: {end_time - start_time:.2f} seconds")
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Import Error
```
ImportError: No module named 'vnstock'
```
**Solution:**
```bash
pip install vnstock
```

#### 2. Network Timeout
```
TimeoutError: Request timed out
```
**Solution:**
```python
# Increase timeout in VNStocks calls
# Hoặc implement retry mechanism
import asyncio

async def retry_api_call(func, *args, max_retries=3):
    for attempt in range(max_retries):
        try:
            return await func(*args)
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            await asyncio.sleep(1)
```

#### 3. Data Format Issues
```
KeyError: 'expected_field'
```
**Solution:**
```python
# Robust data extraction
def safe_get(data, key, default=None):
    return data.get(key, default) if isinstance(data, dict) else default

market_cap = safe_get(company_info, 'marketCap', 0)
```

#### 4. Rate Limiting
```
HTTP 429: Too Many Requests
```
**Solution:**
```python
# Implement caching and rate limiting
import time

class RateLimitedAPI:
    def __init__(self, calls_per_minute=60):
        self.calls_per_minute = calls_per_minute
        self.last_call_times = []
    
    def wait_if_needed(self):
        now = time.time()
        # Remove calls older than 1 minute
        self.last_call_times = [t for t in self.last_call_times if now - t < 60]
        
        if len(self.last_call_times) >= self.calls_per_minute:
            sleep_time = 60 - (now - self.last_call_times[0])
            time.sleep(sleep_time)
        
        self.last_call_times.append(now)
```

---

## 📈 Performance Optimization

### 1. Caching Strategy

```python
# Enhanced caching
import redis
import json
from datetime import datetime, timedelta

class RedisCache:
    def __init__(self, redis_url='redis://localhost:6379'):
        self.redis_client = redis.from_url(redis_url)
    
    def get(self, key):
        data = self.redis_client.get(key)
        return json.loads(data) if data else None
    
    def set(self, key, value, ttl=300):
        self.redis_client.setex(key, ttl, json.dumps(value))
```

### 2. Async Optimization

```python
# Batch processing
async def get_multiple_stocks_optimized(symbols, batch_size=5):
    """Process stocks in batches to avoid overwhelming the API"""
    results = {}
    
    for i in range(0, len(symbols), batch_size):
        batch = symbols[i:i+batch_size]
        batch_tasks = [api.get_stock_data(symbol) for symbol in batch]
        batch_results = await asyncio.gather(*batch_tasks, return_exceptions=True)
        
        for symbol, result in zip(batch, batch_results):
            if not isinstance(result, Exception):
                results[symbol] = result
        
        # Small delay between batches
        await asyncio.sleep(0.5)
    
    return results
```

---

## 🚀 Deployment Checklist

### Pre-deployment

- [ ] VNStocks installed and tested
- [ ] All unit tests passing
- [ ] Integration tests passing
- [ ] Performance tests acceptable
- [ ] Error handling tested
- [ ] Backup of current system created

### Deployment

- [ ] Update requirements.txt
- [ ] Deploy new API implementation
- [ ] Monitor for errors
- [ ] Verify data accuracy
- [ ] Check performance metrics

### Post-deployment

- [ ] Monitor API usage
- [ ] Check error rates
- [ ] Validate data quality
- [ ] Gather user feedback
- [ ] Performance optimization if needed

---

## 📚 Additional Resources

### VNStocks Documentation
- [Official Documentation](https://vnstocks.com/docs)
- [GitHub Repository](https://github.com/thinh-vu/vnstock)
- [API Examples](https://vnstocks.com/docs/examples)

### Support
- [VNStocks Community](https://t.me/vnstock_community)
- [GitHub Issues](https://github.com/thinh-vu/vnstock/issues)

---

## 🎯 Next Steps

1. **Install VNStocks**: `pip install vnstock`
2. **Run Tests**: `python test_vnstocks_integration.py`
3. **Update Code**: Replace imports and test
4. **Deploy**: Follow deployment checklist
5. **Monitor**: Watch for issues and optimize

---

**🎉 Chúc mừng! Bạn đã sẵn sàng chuyển đổi sang VNStocks real data!** 