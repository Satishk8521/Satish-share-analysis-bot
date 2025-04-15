from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.form.get("Body", "").strip().upper()
    return analyze_stock(incoming_msg)

def analyze_stock(stock):
    # Simple demo logic
    analysis = {
        "RVNL": ("BUY", "Infra sector growth & strong order book."),
        "TCS": ("HOLD", "Stable IT performance, long-term investment."),
        "YESBANK": ("SELL", "Weak fundamentals, avoid for now.")
    }

    if stock in analysis:
        action, reason = analysis[stock]
        reply = f"Stock: {stock}\nAction: {action}\nReason: {reason}"
    else:
        reply = f"Sorry, analysis for '{stock}' not found."

    return f"""<Response><Message>{reply}</Message></Response>"""

if __name__ == "__main__":
    app.run()
