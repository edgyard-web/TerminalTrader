import ccxt
import time

# Инициализируем биржу Binance (она самая популярная)
exchange = ccxt.binance()

print("--- Начинаем мониторинг цены BTC ---")

try:
    while True:
        # Получаем данные о тикере (цене)
        ticker = exchange.fetch_ticker('BTC/USDT')
        last_price = ticker['last']
        
        # Выводим цену в терминал
        print(f"Текущая цена BTC: ${last_price}", end="\r")
        
        # Ждем 2 секунды перед следующим обновлением
        time.sleep(2)
except KeyboardInterrupt:
    print("\nПрограмма остановлена.")
