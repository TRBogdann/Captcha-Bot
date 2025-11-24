
# How to run

## No complete exemple (Early Stage)
You won t be able to run main since you won t have the original env. But you can use ocr (captcha-reader + vocabulary)
or the action blocks to build your own bot.

## Initialize
```bash
python3 -m .venv venv
source .venv/bin/activate
pip install requirements.txt
```
## Create .env
### Exemple
```txt
EMAIL=dummy@gmail.com
PASSWORD=password123

DRIVER=Chrome

AUTH_STAGE_URL=https://page.com/log
HOME_PAGE_URL=https://page.com
TARGET_PAGE_URL=https://page.com/target

...
```

## Run the program
```bash
python3 bot.py
```