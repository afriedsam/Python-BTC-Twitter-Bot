import requests
import pandas as pd
import tweepy
import schedule

print('RUNNING')

def upload():
    historicalCloseData = []
    historicalCloseData.clear
    historicalURL = "https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=25"
    historicalData = requests.get(historicalURL)
    ipdata = historicalData.json()
    dataFrame = pd.DataFrame(ipdata['Data']['Data'])
    for closeColumn in dataFrame['close']:
        historicalCloseData.append(closeColumn)
    EST_datetime_data = requests.get('http://worldtimeapi.org/api/timezone/Etc/GMT+6.json')
    EST_datetime = (EST_datetime_data.json()['datetime'])
    EST_time = (EST_datetime[11:16])
    broken_heart = ('\U0001F494' + ' -')
    green_heart = ('\U0001F49A' + ' +')
    current = (historicalCloseData[24])
    price1hr = (historicalCloseData[23])
    price5hr = (historicalCloseData[19])
    price24hr = (historicalCloseData[0])
    # LOCATE HISTORICAL PRICE DATA (24 HOURS)
    difference_1hr = float(current) - float(price1hr)  # Calculates difference
    # print(difference_1hr)
    percent_of_whole_1hr = float(current) / float(price1hr)  # Calculates pre decimal number
    # print(percent_of_whole_1hr)
    percent_in_decimal_1hr = float(percent_of_whole_1hr) - 1  # Converts two decimal
    # print(percent_in_decimal_1hr)
    percent_1hr = float(percent_in_decimal_1hr) * 100  # Converts from decimal to percent
    # print("Unrouned percent change: " + str(percent_1hr) + "%")
    rounded_dif_1hr = (round(difference_1hr, 2))  # Rounds difference
    # print("Rounded difference: " + str(rounded_dif_1hr))
    rounded_percent_1hr = (round(percent_1hr, 2))  # Rounds Percent
    # print("Rounded percent change: " + str(rounded_percent_1hr) + "%")
    difference_5hr = float(current) - float(price5hr)  # Calculates difference
    # print(difference_5hr)
    percent_of_whole_5hr = float(current) / float(price5hr)  # Calculates pre decimal number
    # print(percent_of_whole_5hr)
    percent_in_decimal_5hr = float(percent_of_whole_5hr) - 1  # Converts two decimal
    # print(percent_in_decimal_5hr)
    percent_5hr = float(percent_in_decimal_5hr) * 100  # Converts from decimal to percent
    # print("Unrouned percent change: " + str(percent_5hr) + "%")
    rounded_dif_5hr = (round(difference_5hr, 2))  # Rounds difference
    # print("Rounded difference: " + str(rounded_dif_5hr))
    rounded_percent_5hr = (round(percent_5hr, 2))  # Rounds Percent
    # print("Rounded percent change: " + str(rounded_percent_5hr) + "%")
    difference_24hr = float(current) - float(price24hr)  # Calculates difference
    # print(difference_24hr)
    percent_of_whole_24hr = float(current) / float(price24hr)  # Calculates pre decimal number
    # print(percent_of_whole_24hr)
    percent_in_decimal_24hr = float(percent_of_whole_24hr) - 1  # Converts two decimal
    # print(percent_in_decimal_24hr)
    percent_24hr = float(percent_in_decimal_24hr) * 100  # Converts from decimal to percent
    # print("Unrouned percent change: " + str(percent_24hr) + "%")
    rounded_dif_24hr = (round(difference_24hr, 2))  # Rounds difference
    # print("Rounded difference: " + str(rounded_dif_1hr))
    rounded_percent_24hr = (round(percent_24hr, 2))  # Rounds Percent
    # print("Rounded percent change: " + str(rounded_percent_24hr) + "%")
    if float(difference_1hr) > 0:
        tweet_1hr = ("Bitcoin: " + '$' + str(current) + '\n' + green_heart + str(
            rounded_dif_1hr) + " last 1 Hour " "(+" + str(rounded_percent_1hr) + "%)")
        # print(tweet_1hr)
    else:
        tweet_1hr = ("Bitcoin: " + '$' + str(current) + '\n' + broken_heart + str(abs(rounded_dif_1hr))
                     + " last 1 Hour " "(" + str(rounded_percent_1hr) + "%)")
        # print(tweet_1hr)
    if float(difference_5hr) > 0:
        tweet_5hr = (green_heart + str(rounded_dif_5hr) + " last 5 Hours " "(+" + str(rounded_percent_5hr) + "%)")
        # print(tweet_3hr)
    else:
        tweet_5hr = broken_heart + (
                    str(abs(rounded_dif_5hr)) + " last 5 Hours " + "(" + str(rounded_percent_5hr) + "%)")
        # print(tweet_3hr)
    if float(difference_24hr) > 0:
        tweet_24hr = (green_heart + str(rounded_dif_24hr) + " last 24 Hours " "(+" + str(rounded_percent_24hr) + "%)")
        # print(tweet_24hr)
    else:
        tweet_24hr = broken_heart + (
                    str(abs(rounded_dif_24hr)) + " last 24 Hours " "(" + str(rounded_percent_24hr) + "%)")
        # print(tweet_24hr)
    API_KEY = "******************************"
    API_SECRET = "******************************"
    ACCESS_TOKEN = "******************************-******************************"
    ACCESS_TOKEN_SECRET = "******************************"
    hashtags = "#BitcoinPriceUpdates #Bitcoin #HourlyCrypto #CryptoUpdates #Crypto"
    tweet_whole = tweet_1hr + '\n' + tweet_5hr + '\n' + tweet_24hr + '\n' + hashtags + '\n' + 'Powered By CryptoCompare API'
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(tweet_whole)
    print('\n' + 'NEW UPDATE:' + EST_time)

try:
	#schedule.every().day.at('22:51').do(upload)  # TEST TWEET
	schedule.every().hour.at(':00').do(upload)
	while True:
    	schedule.run_pending()
    	time.sleep(1)
except:
	print("SCRIPT EXCEPTION. SENDING MESSAGE. RESTART SCRIPT")
    api.send_direct_message("****************", "SCRIPT EXCEPTION. BOT RESTARTED. RESTART SCRIPT.")
    upload()
finally:
	schedule.every().hour.at(':00').do(upload)
	while True:
    	schedule.run_pending()
    	time.sleep(1)
