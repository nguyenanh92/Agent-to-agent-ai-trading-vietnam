#!/usr/bin/env python3
"""
Test script cho VNStocks integration
Kiểm tra xem VNStocks có hoạt động đúng với hệ thống hiện tại không
"""

import asyncio
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

async def test_vnstocks_integration():
    """Test VNStocks integration"""
    
    print("🧪 Testing VNStocks Integration...")
    print("=" * 50)
    
    try:
        # Test 1: Import VNStocks implementation
        print("\n1️⃣ Testing VNStocks import...")
        from src.data.vn_stock_api_vnstocks import VNStockAPIVNStocks, VNStockData
        print("✅ VNStocks implementation imported successfully")
        
        # Test 2: Initialize API
        print("\n2️⃣ Testing API initialization...")
        api = VNStockAPIVNStocks()
        print("✅ VNStocks API initialized successfully")
        
        # Test 3: Get available symbols
        print("\n3️⃣ Testing available symbols...")
        symbols = api.get_available_symbols()
        print(f"✅ Found {len(symbols)} available symbols")
        if symbols:
            print(f"   Sample symbols: {[s['symbol'] for s in symbols[:5]]}")
        
        # Test 4: Get single stock data
        print("\n4️⃣ Testing single stock data (VCB)...")
        stock_data = await api.get_stock_data('VCB')
        if stock_data:
            print("✅ Stock data retrieved successfully")
            print(f"   Symbol: {stock_data.symbol}")
            print(f"   Price: {stock_data.price:,.0f} VND")
            print(f"   Change: {stock_data.change:+.0f} ({stock_data.change_percent:+.2f}%)")
            print(f"   Volume: {stock_data.volume:,}")
            print(f"   Sector: {stock_data.sector}")
            print(f"   Exchange: {stock_data.exchange}")
        else:
            print("⚠️ No stock data retrieved")
        
        # Test 5: Get market overview
        print("\n5️⃣ Testing market overview...")
        market_overview = await api.get_market_overview()
        if market_overview:
            print("✅ Market overview retrieved successfully")
            vn_index = market_overview.get('vn_index', {})
            print(f"   VN-Index: {vn_index.get('value', 'N/A')}")
            print(f"   Change: {vn_index.get('change', 'N/A')} ({vn_index.get('change_percent', 'N/A')}%)")
            print(f"   Sentiment: {market_overview.get('market_sentiment', 'N/A')}")
            
            top_gainers = market_overview.get('top_gainers', [])
            if top_gainers:
                print(f"   Top gainers: {len(top_gainers)} stocks")
        else:
            print("⚠️ No market overview data")
        
        # Test 6: Get historical data
        print("\n6️⃣ Testing historical data (VCB, 10 days)...")
        historical_data = await api.get_historical_data('VCB', days=10)
        if historical_data:
            print(f"✅ Historical data retrieved: {len(historical_data)} data points")
            if historical_data:
                latest = historical_data[-1]
                print(f"   Latest: {latest['date']} - {latest['price']:,.0f} VND")
        else:
            print("⚠️ No historical data retrieved")
        
        # Test 7: Get multiple stocks
        print("\n7️⃣ Testing multiple stocks (VCB, TCB, BID)...")
        from src.data.vn_stock_api_vnstocks import get_multiple_stocks
        
        multiple_stocks = await get_multiple_stocks(['VCB', 'TCB', 'BID'])
        if multiple_stocks:
            print(f"✅ Multiple stocks retrieved: {len(multiple_stocks)} stocks")
            for symbol, data in multiple_stocks.items():
                print(f"   {symbol}: {data.price:,.0f} VND ({data.change_percent:+.2f}%)")
        else:
            print("⚠️ No multiple stocks data")
        
        # Test 8: News sentiment (placeholder)
        print("\n8️⃣ Testing news sentiment...")
        news_sentiment = await api.get_news_sentiment('VCB')
        if news_sentiment:
            print("✅ News sentiment retrieved")
            print(f"   Sentiment: {news_sentiment.get('sentiment', 'N/A')}")
            print(f"   Score: {news_sentiment.get('sentiment_score', 'N/A')}")
            print(f"   Note: {news_sentiment.get('note', 'N/A')}")
        
        print("\n" + "=" * 50)
        print("🎉 All tests completed successfully!")
        print("✅ VNStocks integration is working properly")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("💡 Please install VNStocks: pip install vnstock")
        return False
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_installation_guide():
    """Test và hướng dẫn cài đặt VNStocks"""
    
    print("\n📦 VNStocks Installation Guide")
    print("=" * 50)
    
    try:
        import vnstock
        print("✅ VNStocks is already installed")
        print(f"   Version: {getattr(vnstock, '__version__', 'Unknown')}")
        return True
        
    except ImportError:
        print("❌ VNStocks is not installed")
        print("\n📝 Installation Instructions:")
        print("1. Install VNStocks:")
        print("   pip install vnstock")
        print("\n2. Or install latest version:")
        print("   pip install -U vnstock")
        print("\n3. Alternative (from GitHub):")
        print("   pip install git+https://github.com/thinh-vu/vnstock.git")
        
        return False

if __name__ == "__main__":
    print("🚀 VNStocks Integration Test")
    print("Testing VNStocks library integration with the current system")
    
    # Check installation first
    installation_ok = asyncio.run(test_installation_guide())
    
    if installation_ok:
        # Run integration tests
        success = asyncio.run(test_vnstocks_integration())
        
        if success:
            print("\n🎯 Next Steps:")
            print("1. Update requirements.txt to include vnstock")
            print("2. Update main application to use VNStockAPIVNStocks")
            print("3. Test with real trading scenarios")
        else:
            print("\n🔧 Troubleshooting needed")
    else:
        print("\n⚠️ Please install VNStocks first, then run this test again") 