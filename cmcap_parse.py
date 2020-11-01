# after adapting source infos:
# things left to do: figure out how to get all the logos. figure out how to write whether the percent change is negative or positive. 

from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("cmc_parsed_files"):
	os.mkdir("cmc_parsed_files")

df = pd.DataFrame()

# # for trying to print things, uncomment this: 
# one_file_name = "html_files_trial/cmcap20201101164950.html"
# scrape_time = os.path.basename(one_file_name).replace("cmcap", "").replace("copy.html","")
# f = open(one_file_name, "r")
# soup = BeautifulSoup(f.read(), "html.parser")
# f.close()
# currencies_table = soup.find("tbody")
# currency_rows = currencies_table.find_all("tr")
# currency_columns = currency_rows[0].find_all("td")
# print()

for one_file_name in glob.glob("html_files_trial/*.html"):
	print(one_file_name)
	scrape_time = os.path.basename(one_file_name).replace("cmcap", "").replace(".html","")
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()

	currencies_table = soup.find("tbody")
	currency_rows = currencies_table.find_all("tr")

	for r in currency_rows:
		currency_columns = r.find_all("td")
		if len(currency_columns)>10:
			currency_name = currency_columns[2].find("p").text
			currency_rank = currency_columns[2].find("a")["href"]
			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
			currency_price = currency_columns[3].find("a").text.replace("$","").replace(",","")
			currency_marketcap = currency_columns[6].find("p").text.replace("$","").replace(",","")
			currency_trading_volume_inUSD = currency_columns[7].find("a").text.replace("$","").replace(",","")
			currency_pctchange_24h = currency_columns[4].find("span").text.replace("%","")
			currency_pctchange_7d = currency_columns[5].find("span").text.replace("%","")
			# to fix the percent changes, maybe try something with the replace function for the positive or negative. ie "if class =   , replace(,"-") or something
			currency_circulating_supply = currency_columns[8].find("p").text.replace("$","").replace(",","")
			currency_trading_volume_inCurrency = currency_columns[7].find("p", {"class": "Text-sc-1eb5slv-0 jicUsX"}).text.replace(",","")
			currency_link = currency_columns[2].find("a")["href"]
			currency_logo = currency_columns[2].find("a").find('img')
			df = df.append({
						'time': scrape_time,
						'name': currency_name,
						'symbol': currency_symbol,
						'rank': currency_rank,
						'price': currency_price,
						'market_cap': currency_marketcap,
						'trading_volume-USD': currency_trading_volume_inUSD,
						'trading_volume-currency': currency_trading_volume_inCurrency,
						'circulating_supply': currency_circulating_supply,
						'pct_change_24h': currency_pctchange_24h,
						'pct_change_7d': currency_pctchange_7d,
						'logo': currency_logo,
						'link': currency_link
					}, ignore_index=True)

df.to_csv("cmc_parsed_files/TRIALcmc_dataset.csv")


# ______
# 			currency_name = currency_columns[2].find("p").text
# 			currency_rank = currency_columns[2].find("a")["href"]
# 			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
# 			currency_price = currency_columns[3].find("a").text.replace("$","").replace(",","")
# 			currency_marketcap = currency_columns[6].find("p").text.replace("$","").replace("$","")
# 			currency_trading_volume_inUSD = currency_columns[7].find("a").text.replace("$","").replace(",","")
# 			currency_pctchange_24h = currency_columns[4].find("span").text.replace("%","")
# 			currency_pctchange_7d = currency_columns[5].find("p").text.replace("%","")
# 			currency_circulating_supply = currency_columns[8].find("p").text.replace("$","").replace(",","")
# 			currency_trading_volume_inCurrency = currency_columns[7].find("p", {"class": "Text-sc-1eb5slv-0 jicUsX"}).text.replace(",","").replace(" BTC","")
# 			currency_link = currency_columns[2].find("a")["href"]
# 			currency_logo = (currency_columns[2].find("a").find('img'))
# 			# print(currency_columns[2].find("a").find('img').get_attribute('src'))
# 			df = df.append({
# 						'time': scrape_time,
# 						'name': currency_name,
# 						'symbol': currency_symbol,
# 						'rank': currency_rank,
# 						'price': currency_price,
# 						'market_cap': currency_marketcap,
# 						'trading_volume-USD': currency_trading_volume_inUSD,
# 						'trading_volume-currency': currency_trading_volume_inCurrency,
# 						'circulating_supply': currency_circulating_supply,
# 						'pct_change_24h': currency_pctchange_24h,
# 						'pct_change_7d': currency_pctchange_7d,
# 						'logo': currency_logo,
# 						'link': currency_link
# 					}, ignore_index=True)



# # not indented at all:
# df.to_csv("cmc_parsed_files/TRIALcmc_dataset.csv")





# ___________________ trial, before adapting the source infos:


# things left to do: get logos!! indentations/undo comments. get tbodies.

# from bs4 import BeautifulSoup
# import os
# import glob
# import pandas as pd

# if not os.path.exists("cmc_parsed_files"):
# 	os.mkdir("cmc_parsed_files")

# df = pd.DataFrame()


# # one_file_name = "html_files/cmcap20201029203435.html"
# # scrape_time = os.path.basename(one_file_name).replace("cmcap", "").replace("copy.html","")
# # f = open(one_file_name, "r")
# # soup = BeautifulSoup(f.read(), "html.parser")
# # f.close()
# # currencies_table = soup.find("tbody")
# # currency_rows = currencies_table.find_all("tr")

# # currency_columns = currency_rows[0].find_all("td")

# # print(currency_columns[2].find("a").find('img').text)

# for one_file_name in glob.glob("html_files_trial/*.html"):
# # indent everything after this
# 	# one_file_name = "html_files/cmcap20201029203435.html"
# 	print(one_file_name)
# 	scrape_time = os.path.basename(one_file_name).replace("cmcap", "").replace(".html","")
# 	f = open(one_file_name, "r")
# 	soup = BeautifulSoup(f.read(), "html.parser")
# 	f.close()

# 	currencies_table = soup.find("tbody")
# 	currency_rows = currencies_table.find_all("tr")
# 	# need to figure out how to get the other tbodys.
# 	for r in currency_rows:
# 		currency_columns = r.find_all("td")
# 		if len(currency_columns)>10:
# 			currency_name = currency_columns[2].find("p").text?
# 			currency_rank = currency_columns[2].find("a")["href"]
# 			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
# 			currency_price = currency_columns[3].find("a").text.replace("$","").replace(",","")
# 			currency_marketcap = currency_columns[6].find("p").text.replace("$","").replace("$","")
# 			currency_trading_volume_inUSD = currency_columns[7].find("a").text.replace("$","").replace(",","")
# 			currency_pctchange_24h = currency_columns[4].find("p").text.replace("%","")
# 			currency_pctchange_7d = currency_columns[5].find("p").text.replace("%","")
# 			currency_circulating_supply = currency_columns[8].find("p").text.replace("$","").replace(",","")
# 			currency_trading_volume_inCurrency = currency_columns[7].find("p", {"class": "Text-sc-1eb5slv-0 jicUsX"}).text.replace(",","").replace(" BTC","")
# 			currency_link = currency_columns[2].find("a")["href"]
# 			currency_logo = (currency_columns[2].find("a").find('img'))
# 			# print(currency_columns[2].find("a").find('img').get_attribute('src'))
# 			df = df.append({
# 						'time': scrape_time,
# 						'name': currency_name,
# 						'symbol': currency_symbol,
# 						'rank': currency_rank,
# 						'price': currency_price,
# 						'market_cap': currency_marketcap,
# 						'trading_volume-USD': currency_trading_volume_inUSD,
# 						'trading_volume-currency': currency_trading_volume_inCurrency,
# 						'circulating_supply': currency_circulating_supply,
# 						'pct_change_24h': currency_pctchange_24h,
# 						'pct_change_7d': currency_pctchange_7d,
# 						'logo': currency_logo,
# 						'link': currency_link
# 					}, ignore_index=True)



# # not indented at all:
# df.to_csv("cmc_parsed_files/TRIALcmc_dataset.csv")











# ___________________________ original/not trial:



# # things left to do: get logos!! indentations/undo comments.
# from bs4 import BeautifulSoup
# import os
# import glob
# import pandas as pd

# if not os.path.exists("cmc_parsed_files"):
# 	os.mkdir("cmc_parsed_files")

# df = pd.DataFrame()

# one_file_name = "html_files/cmcap20201029203435.html"
# for one_file_name in glob.glob("html_files/*.html"):
# # indent everything after this
# 	# one_file_name = "html_files/cmcap20201029203435.html"
# 	print(one_file_name)
# 	scrape_time = os.path.basename(one_file_name).replace("cmcap", "").replace(".html","")
# 	f = open(one_file_name, "r")
# 	soup = BeautifulSoup(f.read(), "html.parser")
# 	f.close()

# 	currencies_table = soup.find("tbody")
# 	currency_rows = currencies_table.find_all("tr")
	
# 	for r in currency_rows:
# 		currency_columns = r.find_all("td")
# 		if len(currency_columns)>10:
# 			currency_name = currency_columns[2].find("p").text
# 			currency_rank = currency_columns[2].find("a")["href"]
# 			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
# 			currency_price = currency_columns[3].find("a").text.replace("$","").replace(",","")
# 			currency_marketcap = currency_columns[6].find("p").text.replace("$","").replace("$","")
# 			currency_trading_volume_inUSD = currency_columns[7].find("a").text.replace("$","").replace(",","")
# 			currency_pctchange_24h = currency_columns[4].find("p").text.replace("%","")
# 			currency_pctchange_7d = currency_columns[5].find("p").text.replace("%","")
# 			currency_circulating_supply = currency_columns[8].find("p").text.replace("$","").replace(",","")
# 			currency_trading_volume_inCurrency = currency_columns[7].find("p", {"class": "Text-sc-1eb5slv-0 jicUsX"}).text.replace(",","").replace(" BTC","")
# 			currency_link = currency_columns[2].find("a")["href"]
# 			# currency_logo = 
# 			# print(currency_columns[2].find("a").find('img').get_attribute('src'))
# 			df = df.append({
# 						'time': scrape_time,
# 						'name': currency_name,
# 						'symbol': currency_symbol,
# 						'rank': currency_rank,
# 						'price': currency_price,
# 						'market_cap': currency_marketcap,
# 						'trading_volume-USD': currency_trading_volume_inUSD,
# 						'trading_volume-currency': currency_trading_volume_inCurrency,
# 						'circulating_supply': currency_circulating_supply,
# 						'pct_change_24h': currency_pctchange_24h,
# 						'pct_change_7d': currency_pctchange_7d,
# 						# 'logo': currency_logo,
# 						'link': currency_link
# 					}, ignore_index=True)



# # not indented at all:
# df.to_csv(cmc_parsed_files/cmc_dataset.csv)












