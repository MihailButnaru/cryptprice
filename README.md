<div align="center">
<h1> CryptPrice Chat-Bot on Slack</h1>

![CryptPrce Chat Bot](https://github.com/MihailButnaru/cryptprice/blob/develop/images/cryptprice_bot.png)

<p1>The CryptPrice Bot is designed to allow you to see the current price
of different crypto currencies on your slack channel.</p1>
</div>
<hr/>


## Intro
Slack is a team collaboration hub that brings every member of a team
together and more collaborative. Is a tool that is used by millions of
users around the world on daily basis.

CryptPrice allows you to see the current price of the crypto-currencies [BTC, ETH, XRP].

## Tutorial
Full tutorial of how to run the CryptPrice Bot. Say Hi when he is running!
Visit: https://medium.com/@butnarum/build-a-cryptocurrency-price-bot-on-slack-with-python-using-django-code-included-aa04a0d41c28


## Instalation
Clone the project and start by building a dvelopment environment
1. Install the dependencies of project
```
$ pip install -r requirements.txt
```
2. Create the environment variable file (.env) to include
the Slack credentials:
You can get all the credentials when you create your slack app: https://api.slack.com/apps/new
```
SLACK_BOT_USER_OAUTH_ACCESS_TOKEN = 'your bot user oauth token here'
SLACK_CLIENT_ID = 'your client id here'
SLACK_CLIENT_SECRET = 'your client secret here'
SLACK_VERIFICATION_TOKEN = 'your verification token here'
```
3. Run the CryptPrice bot
```
$ python manage.py runserver
```

## License & Author
License 2020 © MIHAIL BUTNARU

Made by Mihail Butnaru
