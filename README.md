# Table of Contents

## General Info
The project "Cryptotests" focuses on testing Coinlore API (https://api.coinlore.net/api/)
Test Cases involve specific endpoint which provides data about Cryptocurrencies (like Bitcoin)

## Technologies
In Test Cases were used: 
- Python 3.9,
- Pytest,
- Python modules: Requests, time, assertpy, backoff,
- Pytest fixtures.

## Setup
At the beginning, you can install IDE with Python (like Pycharm) and create a virtual environment (venv). Tester should import mentioned Python modules, Pytest. 

## Test Cases Description

###### test_01_check_market_info
Test aim: Checking 200 HTTP Response Code for loading market information endpoint
###### test_02_check_id_bitcoin
Test aim: Checking if loaded data from endpoint are appropriate for Bitcoin (Name and ID)
###### test_03_check_crypto_info_markets
Test aim: Verification of data types in crypto information endpoint
###### test_04_check_50_markets_values_crypto
Test aim: Verification of receiving 50 crypto exchanges in endpoint JSON
######  test_05_check_all_exchanges
Test aim: Verification if "date_added" is not zero data in endpoint JSON
###### test_06_check_exchange_data_fetching
Test aim: Verification if data from exchange are not null or zero value
###### test_07_check_social_stats
Test aim: Checking 200 HTTP Response Code for loading social stats endpoint

