import google.generativeai as genai

# Test API key
genai.configure(api_key="AIzaSyBm1tqAKxixAIGL7j4UzwMY4FXkCiBX5mw")
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Hello")
print(response.text)