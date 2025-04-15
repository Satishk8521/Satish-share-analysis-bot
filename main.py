import yfinance as yf

def analyze_stock(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        name = info.get("longName", "N/A")
        price = info.get("currentPrice", "N/A")
        pe_ratio = info.get("trailingPE", "N/A")
        rec = info.get("recommendationKey", "N/A")

        result = f"""शेयर: {name}
प्राइस: ₹{price} | PE रेशियो: {pe_ratio} | सलाह: {rec.upper()}"""
        return result

    except Exception as e:
        return "कुछ गड़बड़ है, शेयर कोड जाँचें"

# Example run
print(analyze_stock("TCS.NS"))
