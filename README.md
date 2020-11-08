# ECON4980 Midterm Project

## Contents
* [Introduction](#Introduction)
* [Technologies](#Technologies)
* [Installation](#Installation)

## Introduction
This project downloads and parses salient data on the top 500 cryptocurrencies (ranked by market capitalization) from the websites [coinmarketcap](coinmarketcap.com) and [coingecko](coingecko.com) 192 times over a 48 hour time period. It uses these data to analyze differences in reporting between the two sites. As a bonus, the project also requests and attempts to parse historical data from these websites for the year between November 1, 2019 and November 1, 2020. 

## Technologies
This project was made on Python 3.7, so that or a newer version may be required to run it. 

The programs also use the modules numpy, matplotlib, bs4, pandas, sklearn, tzlocal, and requests. If you don't have these already, you may need to install them by writing:
`pip -m install numpy matplotlib bs4 pandas sklearn tzlocal requests`
in the terminal.

## Installation
To run this project, you will need to install it on your computer. To do this, write
`pip install git+git://github.com/cbouts/midterm_project.git`
in the terminal.

## Usage
Running this projects takes - steps. They are listed and elaborated here.

### Step 1:

Request data by running [cmcap_coingecko_request.py](https://github.com/cbouts/midterm_project/blob/main/cmcap_coingecko_request.py). This file requests the most important data from Coingecko using API and from Coinmarketcap using screen scraping. First, the file creates the folders which will hold html files from Coinmarketcap and the json files from Coingecko: 
```
if not os.path.exists("html_files_2"):
	os.mkdir("html_files_2")

if not os.path.exists("json_files_2"):
	os.mkdir("json_files_2")
```
On my computer, I need to include the next line because I get an "unverified" error if I do not. However, many people successfully omit this from their code: `context = ssl._create_unverified_context()`. We write this unverified context after each of our URLs to prevent the error: `context=context`. 

In its current form, the file requests data at 15 minute intervals for the 48 hour time period of interest, resulting in (4 downloads per hour) * (48 hours) = 192 download processes reflected in the beginning for the for loop: `for i in range(192):`. The file then requests the first page of 100 coins from coinmarketcap, the first 250 coins from coingecko, sleeps for 15 seconds, requests the second page of 100 coins from coinmarketcap and coins 250-500 from coingecko, sleeps for 15 seconds, then requests pages 3-5 (coins 300-500) from coinmarketcap (with sleep time of 15 seconds between these requests). After this, the program sleeps for 840 seconds. 

Of course, this can be adapted to fit your needs as is illustrated here:
- To get a different number of observations, you can change 192 to another number in this line of code:
`for i in range(192):`
- The 15 minute intervals are regulated by the 4 lines of code that say `time.sleep(15)` and the one line that says `time.sleep(840)`. Including 4 time.sleep periods of 15 seconds each throughout the program and 1 long 840 second time.sleep period yields 900 total seconds of sleep between the start of one round of downloads and the start of the next round. Note that you should always include some sleep time after your downloads in order to avoid breaking or getting banned from the sites.
- Manipulating these `time.sleep()` and `for i in range():` lines allows you to change the length of the time period of interest, as well as the frequency of your observations.For example, changing `time.sleep(840)` to `time.sleep(540)` while also changing `for i in range(192):` to `for i in range(6):` will yield 6 downloads of the site 10 minutes apart over a 1 hour time period.

Once you've configured the program to match your needs, you simply run it and monitor the terminal output for errors which will be printed without interrupting the program's progress due to the file's "try/except/else" format.
### Step 2: 
Parse the data for the two websites by running parse files.
#### Step 2A:
Run [coingecko_parse.py](https://github.com/cbouts/midterm_project/blob/main/coingecko_parse.py). This creates the folder 'coingecko_parsed_files' which will hold our new coingecko csv:
```
if not os.path.exists('coingecko_parsed_files'):
	os.mkdir('coingecko_parsed_files')
```
It then loops through the files in the json_files_2 folder (the folder which contains all json files from downloading Coingecko). It creates a dataframe for each coin in each file, appending key information to this dataframe with:
```
df = df.append({
        .........
			}, ignore_index=True)
```
After looping through all coins in all the Coingecko json files, it exports the dataframe to our new csv:
`df.to_csv('coingecko_parsed_files/coingecko_dataset.csv')`. 

#### Step 2B:
Run [cmcap_parse.py](https://github.com/cbouts/midterm_project/blob/main/cmcap_parse.py). This creates the folder 'cmc_parsed_files' which will hold our new coingecko csv:
```
if not os.path.exists("cmc_parsed_files"):
	os.mkdir("cmc_parsed_files")
```
It then loops through the files in the html_files_2 folder (the folder which contains all json files from downloading Coingecko). Within this for loop, there is a for loop that causes the program to loop through every row (representing every coin) in the current file. The for loop then picks up key information about the coins and appends this information to a dataframe with:
```
df = df.append({
        	.........
			}, ignore_index=True)
```
After looping through all coins in all the Coinmarketcap html files, it exports the composite dataframe to our new csv:
`df.to_csv('coingecko_parsed_files/cmc_dataset.csv')`. 

### Step 3: 
Run - with the coinmarketcap parsed data to request deep link information for each coin that features on the top 500 list over the time period of interest.
4. Step 4: Run the deep link parse file to parse the deep link information to a new csv called -
5. Step 5: Analyze the data on the 3 csvs. Run cleaning.py --- to determine how much data for each variable is missing. Using the CSVs, create Excel graphs to show differences in ----
