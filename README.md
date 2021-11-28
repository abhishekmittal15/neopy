# Documentation
Neostox doesnt have an API Support, so this is a little selenium code to automate strategies 

## How to use
- Clone this repository and then make a .env file where you will store your email_id and password. 
- Edit your strategy class
- Run the strategy.py file and a new neostox window will open up
- Just finish the recaptcha and press enter on the terminal from where you ran your file 
- It will fetch the list of instruments in your side bar and store them   

## Broker.py
Handles `signing in` , `fetching list of options` , `fetching data every minute` and `placing orders`

## Strategy.py
The strategy function in the Strategy class is called every minute and it finally takes one of 3 steps :
1. Place a buy order 
2. Place a sell order 
3. Do nothing

Since this is my first time using selenium, I had run into few issues which I havent yet been able to resolve. I have put them up in the `Issues` tab Anyone more familiar with selenium can kindly fix those issues by creating a new branch and then upon verification, they will be merged with the `main` branch

