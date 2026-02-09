import httpx

# Konfigurasi API
URL = "https://coinranking1.p.rapidapi.com/coins"
HEADERS = {
    "x-rapidapi-host": "coinranking1.p.rapidapi.com",
    "x-rapidapi-key": "f0021db587msh781fb1cbef39856p11c183jsn45521d5d1c85"
}

# Kurs Rupiah hari ini (Bisa diupdate manual atau ambil API lain nanti)
KURS_IDR = 15800 

def build_standalone_web():
    try:
        print("[*] Mengambil data dari satelit Coinranking...")
        response = httpx.get(URL, headers=HEADERS)
        coins = response.json()['data']['coins'][:15] # Ambil 15 koin biar ramai
        
        html_content = f"""
        <!DOCTYPE html>
        <html lang="id">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>BRI Crypto Live - Data Akurat</title>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; background: #0f172a; color: #f8fafc; }}
                .header {{ background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 30px; text-align: center; border-bottom: 2px solid #38bdf8; }}
                h1 {{ margin: 0; color: #38bdf8; font-size: 24px; }}
                .container {{ max-width: 900px; margin: 20px auto; padding: 10px; }}
                .card {{ background: #1e293b; border-radius: 12px; padding: 15px; margin-bottom: 10px; display: flex; align-items: center; justify-content: space-between; border: 1px solid #334155; }}
                .coin-info {{ display: flex; align-items: center; }}
                .coin-info img {{ width: 35px; height: 35px; margin-right: 15px; }}
                .coin-name {{ font-weight: bold; font-size: 16px; }}
                .coin-symbol {{ color: #94a3b8; font-size: 12px; text-transform: uppercase; }}
                .price-box {{ text-align: right; }}
                .price-usd {{ font-size: 14px; color: #38bdf8; }}
                .price-idr {{ font-size: 16px; font-weight: bold; color: #f1f5f9; display: block; }}
                .change {{ font-size: 12px; margin-top: 4px; border-radius: 4px; padding: 2px 6px; display: inline-block; }}
                .up {{ background: #064e3b; color: #34d399; }}
                .down {{ background: #450a0a; color: #fb7185; }}
                .footer {{ text-align: center; padding: 20px; font-size: 11px; color: #64748b; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>💰 BRI Crypto Monitor</h1>
                <p style="font-size: 12px; color: #94a3b8;">Harga Real-Time & Akurat (USD & IDR)</p>
            </div>
            <div class="container">
        """

        for coin in coins:
            price_usd = float(coin['price'])
            price_idr = price_usd * KURS_IDR
            change = float(coin['change'])
            status_class = "up" if change > 0 else "down"
            trend = "▲" if change > 0 else "▼"
            
            html_content += f"""
                <div class="card">
                    <div class="coin-info">
                        <img src="{coin['iconUrl']}" alt="{coin['name']}">
                        <div>
                            <div class="coin-name">{coin['name']}</div>
                            <div class="coin-symbol">{coin['symbol']}</div>
                        </div>
                    </div>
                    <div class="price-box">
                        <span class="price-idr">Rp {price_idr:,.0f}</span>
                        <span class="price-usd">${price_usd:,.2f}</span>
                        <div class="change {status_class}">{trend} {abs(change)}%</div>
                    </div>
                </div>
            """

        html_content += """
                <div class="footer">
                    Pembaruan Otomatis via Termux Engine | BRI Project 2026
                </div>
            </div>
        </body>
        </html>
        """

        with open("index.html", "w") as f:
            f.write(html_content)
        
        print("[✅] Website Khusus Berhasil Dibuat!")
        print("[*] Lokasi: ~/website_ku/KOINKRIPTO/index.html")

    except Exception as e:
        print(f"[❌] Terjadi kesalahan: {e}")

if __name__ == "__main__":
    build_standalone_web()

