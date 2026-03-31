import pandas as pd
import sklearn.ensemble 
import RandomForestClassifier

# --- STEP 1: THE DATA ---
# We create a small "Knowledge Base" for the AI
data = {
    'url': [
        'google.com', 'github.com', 'wikipedia.org', 'amazon.in', 
        'secure-login-bank.net', 'verify-update-paypal.com', 'win-free-giftcard.biz', 'update-password.info'
    ],
    # Features: [Length, Dot_Count, Has_Hyphen]
    'length': [10, 10, 13, 9, 21, 24, 21, 20],
    'dots': [1, 1, 1, 1, 1, 2, 1, 1],
    'hyphen': [0, 0, 0, 0, 1, 1, 1, 1],
    'label': [0, 0, 0, 0, 1, 1, 1, 1]  # 0 = Safe, 1 = Phishing
}

df = pd.DataFrame(data)

# --- STEP 2: THE AI TRAINING ---
X = df[['length', 'dots', 'hyphen']]
y = df['label']

model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)

# --- STEP 3: THE PREDICTOR ---
def check_url(url):
    # This turns the URL string into numbers the AI understands
    length = len(url)
    dots = url.count('.')
    hyphen = 1 if '-' in url else 0
    
    prediction = model.predict([[length, dots, hyphen]])
    return "⚠️ PHISHING" if prediction[0] == 1 else "✅ SAFE"

# --- STEP 4: INTERACTIVE DEMO ---
if __name__ == "__main__":
    print("--- 🛡️ Simple AI Phishing Detector ---")
    user_input = input("Enter a URL to check: ")
    result = check_url(user_input)
    print(f"Prediction: {result}")