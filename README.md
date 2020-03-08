# Telegram private groups creator

## overview workflow

- creating a private telegram group with a user from .txt file
- giving this user an admin rights
- creating group invite link
- recording info in file txt

---

## requirements

- [telethon](https://github.com/LonamiWebs/Telethon)

---

## running
### first step 
> https://docs.telethon.dev/en/latest/basic/signing-in.html#signing-in
1. [Login to your Telegram](https://my.telegram.org/) account with the phone number of the developer account to use.
2. Click under API Development tools.
3. A *Create new application* window will appear. Fill in your application details. There is no need to enter any *URL*, and only the first two fields (*App title* and *Short name*) can currently be changed later.
4. Click on *Create application* at the end. Remember that your **API hash is secret** and Telegram won’t let you revoke it. Don’t post it anywhere!

### second step

1. add in `config.ini` yours ***api_id*** and ***api_hash***
2. add in `users.txt` yours ***telegram_users*** without "***@***"
   ```
   // users.txt
   telegram_username_1
   telegram_username_2
   telegram_username_3
   telegram_username_4
   telegram_username_5
   ```
> you can also change ***group title prefix*** or ***input*** and ***output*** .txt file names in `config.ini`

### third step
1. install `requirements.txt` and run `.py` file
```
pip install -r requirements.txt
python main.py
```

## output `.txt` example
```
// users-and-group_links.txt
user: telegram_username_1 	 group_name: <3 telegram_username_1 	 invite_link: https://t.me/joinchat/Lsd4sdasdasdIT4ANsg
user: telegram_username_2 	 group_name: <3 telegram_username_2 	 invite_link: https://t.me/joinchat/Fa30wxasdasfgplIT4A
user: telegram_username_3 	 group_name: <3 telegram_username_3 	 invite_link: https://t.me/joinchat/HSdgGGSDGdhfghplIT4
user: telegram_username_4 	 group_name: <3 telegram_username_4 	 invite_link: https://t.me/joinchat/A254aSFG3gvplIT4ANs
user: telegram_username_5	 group_name: <3 telegram_username_5 	 invite_link: https://t.me/joinchat/AFAssdgfvplIT4ANsgg
```

---

***Maksim Smirnov*** - <smirn08m@gmail.com>