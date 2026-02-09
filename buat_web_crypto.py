import httpx

# Konfigurasi API
URL = "https://coinranking1.p.rapidapi.com/coins"
HEADERS = {
    "x-rapidapi-host": "coinranking1.p.rapidapi.com",
    "x-rapidapi-key": "f0021db587msh781fb1cbef39856p11c183jsn45521d5d1c85"
}

KURS_IDR = 15800

def build_standalone_web():
    try:
        print("[*] Mengambil data koin terbaru...")
        response = httpx.get(URL, headers=HEADERS)
        coins = response.json()['data']['coins'][:15]

        html_content = f"""
        <!DOCTYPE html>
        <html lang="id">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>BRI Crypto Monitor - Real-Time Price</title>
            
            <meta name="description" content="Monitor harga crypto terbaru dalam Rupiah secara real-time. Dapatkan analisis harga koin terbaik dan daftar bursa terpercaya di sini.">
            <meta name="keywords" content="crypto, bitcoin, harga idr, indodax, binance, bri crypto monitor, investasi digital">
            <meta name="author" content="BRI">
            
            <style>
                body {{ font-family: 'Segoe UI', sans-serif; margin: 0; background: #0f172a; color: #f8fafc; }}
                .header {{ background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 30px; text-align: center; border-bottom: 2px solid #38bdf8; }}
                .container {{ max-width: 900px; margin: 20px auto; padding: 10px; }}
                .card {{ background: #1e293b; border-radius: 12px; padding: 15px; margin-bottom: 10px; display: flex; align-items: center; justify-content: space-between; border: 1px solid #334155; }}
                .coin-info {{ display: flex; align-items: center; }}
                .coin-info img {{ width: 35px; height: 35px; margin-right: 15px; }}
                .price-idr {{ font-size: 16px; font-weight: bold; color: #f1f5f9; display: block; }}
                .change {{ font-size: 12px; padding: 2px 6px; border-radius: 4px; }}
                .up {{ background: #064e3b; color: #34d399; }}
                .down {{ background: #450a0a; color: #fb7185; }}

                /* STYLE TOMBOL AFFILIATE */
                .affiliate-section {{ margin-top: 30px; padding: 20px; background: #1e293b; border-radius: 15px; border: 1px dashed #38bdf8; text-align: center; }}
                .btn-cuan {{ display: inline-block; background: #38bdf8; color: #0f172a; padding: 15px 25px; border-radius: 10px; font-weight: bold; text-decoration: none; margin: 10px; transition: 0.3s; }}
                .btn-cuan:hover {{ background: #7dd3fc; transform: scale(1.05); }}
                .footer {{ text-align: center; padding: 20px; font-size: 11px; color: #64748b; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>💰 BRI Crypto Monitor</h1>
                <p>Harga Real-Time & Peluang Investasi Terbaik</p>
            </div>
            <div class="container">
        """

        for coin in coins:
            price_usd = float(coin['price'])
            price_idr = price_usd * KURS_IDR
            change = float(coin['change'])
            status_class = "up" if change > 0 else "down"

            html_content += f"""
                <div class="card">
                    <div class="coin-info">
                        <img src="{coin['iconUrl']}" alt="{coin['name']}">
                        <div>
                            <div class="coin-name">{coin['name']}</div>
                            <small style="color:#94a3b8">{coin['symbol']}</small>
                        </div>
                    </div>
                    <div class="price-box" style="text-align:right">
                        <span class="price-idr">Rp {price_idr:,.0f}</span>
                        <div class="change {status_class}">{change}%</div>
                    </div>
                </div>
            """

        # BAGIAN TOMBOL AFFILIATE
        html_content += """
                <div class="affiliate-section">
                    <h3>🚀 Mau Mulai Trading & Dapat Bonus?</h3>
                    <p>Daftar di bursa terpercaya melalui link di bawah ini untuk mendapatkan bonus pendaftaran!</p>

                    <a href="https://indodax.onelink.me/qyYY/referral?deep_link_value=page:register,id:Rieki11" class="btn-cuan">Daftar Indodax (IDR)</a>
                    <a href="https://www.binance.com/id/register?ref=GOLIBRI" class="btn-cuan">Daftar Binance (Global)</a>
                </div>

                <div class="footer">
                    © 2026 BRI Crypto Monitor | Update Otomatis Setiap Hari
                </div>
            </div>
        </body>
        </html>
        """

        with open("index.html", "w") as f:
            f.write(html_content)

        print("[✅] Website + Meta Tags Berhasil Dibuat!")

    except Exception as e:
        print(f"[❌] Error: {e}")

if __name__ == "__main__":
    build_standalone_web()

