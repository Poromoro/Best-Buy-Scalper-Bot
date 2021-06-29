# BestBuy-Selenium-Scalper-Bot

Refreshes page until add to cart button is ready and automates the checkout process

Created for US-English Best Buy Site

Created in Python

## Need to have existing Best Buy Account with a linked Shipping address and only ONE Credit Card on account.



## Dependencies
- Selenium
	- `pip install selenium`
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://chromedriver.chromium.org/downloads)
	- Extract the compressed chromedriver executable to a driectory of your choice (be sure to update the path in login.py)

## To run
-Edit the login.py file with required information such as email, password, ccv, and driver path

-Edit the Best Buy Links in the main.py file to any item of your choosing on Bestbuy.com

-Head over to your project directory and run the bot script from your prefered enviorment





## Notes
Currently only operational for shipping orders, not pickup.

## Possible Fixes
Orders that direct you to a queue 


Low cost orders may not need a ccv to be inputted



