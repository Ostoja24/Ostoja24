import backoff
import pytest
from assertpy import assert_that, soft_assertions
import requests
import time


@pytest.mark.crypto
class Test_Cryptocurrency:
    @backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_time=60)
    def test_01_check_market_info(self, config, read):
        dataset = "global"
        r = read(f"{config.URL}/{dataset}",
                 headers=None,
                 auth=None,
                 params=None,
                 timeout=3)
        print(r.content)
        assert_that(r.status_code).is_equal_to(200)

    @backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_time=60)
    def test_02_check_id_bitcoin(self, config, read):
        dataset = "ticker/?id=90"
        r = read(f"{config.URL}/{dataset}",
                 headers=None,
                 auth=None,
                 params=None,
                 timeout=3)
        print(r.content)
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
            assert_that(r.json()[0]["name"]).is_equal_to("Bitcoin")
            assert_that(r.json()[0]["nameid"]).is_equal_to("bitcoin")

    @backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_time=60)
    def test_03_check_crypto_info_markets(self, config, read):
        dataset = "tickers"
        r = read(f"{config.URL}/{dataset}/?id=90",
                 headers=None,
                 auth=None,
                 params=None,
                 timeout=3)
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
            assert_that(r.json()["percent_change_24h"].is_type_of(float))
            assert_that(r.json()["percent_change_1h"].is_type_of(float))
            assert_that(r.json()["percent_change_7d"].is_type_of(float))
            assert_that(r.json()["market_cap_usd"].is_type_of(float))
            assert_that(r.json()["volume24"].is_type_of(float))
            assert_that(r.json()["volume24_native"].is_type_of(float))
            assert_that(r.json()["csupply"].is_type_of(float))
            assert_that(r.json()["price_btc"].is_type_of(float))
            assert_that(r.json()["percent_change_24h"].is_type_of(float))

    @backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_time=60)
    def test_04_check_50_markets_values_crypto(self, config, read):
        dataset = "coin/markets"
        r = read(f"{config.URL}/{dataset}/?id=90",
                 headers=None,
                 auth=None,
                 params=None,
                 timeout=3)
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
            assert_that(len(r.json()["name"])).is_equal_to(50)

    @backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_time=60)
    def test_05_check_all_exchanges(self, config, read):
        dataset = "exchanges"
        r = read(f"{config.URL}/{dataset}",
                 headers=None,
                 auth=None,
                 params=None,
                 timeout=3)
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
            assert_that(r.json()["date_added"]).is_not_equal_to("0000-00-00 00:00:00")

    @backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_time=60)
    def test_06_check_exchange_data_fetching(self, config, read):
        dataset = "exchanges"
        r = read(f"{config.URL}/{dataset}/?id=5",
                 headers=None,
                 auth=None,
                 params=None,
                 timeout=3)
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
            assert_that(len(r.json()["base"])).is_equal_to(100)
            assert_that(r.json()["quote"]).is_not_none()
            assert_that(r.json()["time"]).is_greater_than_or_equal_to(time.time())

    @backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_time=60)
    def test_07_check_social_stats(self, config, read):
        dataset = "coin/social_stats"
        r = read(f"{config.URL}/{dataset}/?id=90",
                 headers=None,
                 auth=None,
                 params=None,
                 timeout=3)
        assert_that(r.status_code).is_equal_to(200)

        # assert_that(r.json["name"]).is_equal_to("bitcoin")
