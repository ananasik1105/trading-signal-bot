
### Инструкция по настройке бота на Render

1. Зарегистрируйся на GitHub и создай новый публичный репозиторий, например: trading-signal-bot
2. Загрузить в него все файлы из этого архива
3. Перейди на https://render.com, зарегистрируйся и нажми "New Web Service"
4. Подключи GitHub, выбери созданный репозиторий
5. Render автоматически подхватит настройки из файла render.yaml
6. Укажи:
   - TELEGRAM_TOKEN — вставь свой токен бота от @BotFather
   - CHAT_ID — получи свой chat_id через getUpdates (если нужно — помогу)
7. После запуска Render даст ссылку: https://yourbot.onrender.com/webhook
8. Эту ссылку вставь в TradingView при создании сигнала (WebHook URL)

Пример сообщения в TradingView:
{
  "message": "Лонг по BTC: вход от {{close}}, EMA пересечена снизу вверх"
}
