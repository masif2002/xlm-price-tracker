# XLM Price Tracker
This project scrapes the price of [_Stellar Lumens_](https://www.stellar.org/lumens?locale=en) or  _XLM_ and forwards the price to the user via Telegram every hour. This project is hosted on _Heroku_.

## Working
* Initially, the price is scraped from [coinmarketcap.com](https://coinmarketcap.com/currencies/stellar/) and is sent to a group chat by the TelegramBot which is controlled using the [TelegramBotAPI](https://core.telegram.org/bots/api)
* If the price scraped is found to be greater than a specific amount, then the price is sent to a different group chat which is meant only for price alerts
* The entire project is hosted on **Heroku** for free
* A **CI/CD pipeline** also has been set up with **GitHub Actions**, that automatically deploys to Heroku if any new changes are pushed to the repository
