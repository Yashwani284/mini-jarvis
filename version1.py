import webbrowser as wb
import wikipedia as wk
import datetime as dt
import joblib

# Load trained ML model & vectorizer
model = joblib.load("intent_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

print("🤖 Mini Jarvis with ML started. Type 'exit' to stop.")

while True:
    command = input("\nEnter command: ").lower()

    if command == "exit":
        print("Goodbye!")
        break

    # Convert text → numerical vector
    X = vectorizer.transform([command])

    # Predict intent
    intent = model.predict(X)[0]

    # Intent-based execution
    if intent == "time":
        now = dt.datetime.now().strftime("%H:%M:%S")
        print("Current time is:", now)

    elif intent == "open_app":
        site = command.replace("open", "").strip()
        if site == "":
            print("Please specify website")
        else:
            wb.open(f"https://{site}.com")
            print(f"Opening {site}")

    elif intent == "info":
        topic = command.replace("info", "").strip()
        try:
            summary = wk.summary(topic, sentences=2)
            print(summary)
        except:
            print("No information found")

    elif intent == "calculate":
        expr = command.replace("calculate", "").strip()
        try:
            result = eval(expr)
            print("Result:", result)
        except:
            print("Invalid calculation")

    else:
        print("Sorry, I didn't understand that.")
