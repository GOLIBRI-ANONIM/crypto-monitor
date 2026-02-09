#!/bin/bash
cd ~/website_ku/KOINKRIPTO
python buat_web_crypto.py
git add .
git commit -m "Update otomatis harga pagi"
git push origin main --force

