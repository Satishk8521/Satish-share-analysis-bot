from flask import Flask, request
import yfinance as yf

app = Flask(__name__)

def analyze_stock(stock_symbol):
    try:
        stock = yf.Ticker(stock_symbol)
        hist = stock.history(period="6mo")
        info = stock.info

        current_price = info.get("currentPrice", 0)
        pe_ratio = info.get("trailingPE", 0)
        market_cap = info.get("marketCap", 0)
        recommendation = info.get("recommendationKey", "none")

        response = f"Stock: {stock_symbol.upper()}\n"
        response += f"Current Price: ₹{current_price}\n"
        response += f"P/E Ratio: {pe_ratio}\n"
        response += f"Market Cap: ₹{market_cap}\n"
        response += f"Recommendation: {recommendation.upper()}\n"

        if recommendation in ["buy", "strong_buy"]:
            response += "Advice: BUY for long term."
        elif recommendation in ["sell", "strong_sell"]:
            response += "Advice: SELL or AVOID."
        else:
            response += "Advice: HOLD or watch carefully."

        return response

    except Exception as e:
        return f"Error fetching data for {stock_symbol}. Try again."

@app.route("/webhook/stock_alerts_user001", methods=["POST"])
def stock_webhook():
    incoming_msg = request.values.get("Body", "").strip()
    response_msg = analyze_stock(incoming_msg)
    return response_msg, 200

if __name__ == "__main__":
    app.run(debug=True)
