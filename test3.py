from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import requests
import keyboard

s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON 
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy
    '''
})

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


def send_request(cookies):
    url = "https://api-gw-tg.memefi.club/graphql"


    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjY2OWRhMWU5NjQxMjk5YzYzNjg1NzZjMSIsInVzZXJuYW1lIjoic3RlcF9idWJrYTQ0NDUifSwic2Vzc2lvbklkIjoiNjZhM2MxODcwNWFiZjRjMmY5NjQyMjU4Iiwic3ViIjoiNjY5ZGExZTk2NDEyOTljNjM2ODU3NmMxIiwiaWF0IjoxNzIyMDA3OTQzLCJleHAiOjE3Mjk3ODM5NDN9.2Jk5A-N6tJJcs-qGKkJam-6HTzPg0Eg2ekP3UOcbaOw',
        'content-type': 'application/json',
        'origin': 'https://tg-app.memefi.club',
        'priority': 'u=1, i',
        'referer': 'https://tg-app.memefi.club/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }
    cookies_str = "; ".join([f"{name}={value}" for name, value in cookies.items()])

    headers['cookie'] = cookies_str

    data = [
        {
            'operationName': 'MutationGameProcessTapsBatch',
            'variables': {
                'payload': {
                    'nonce': '04e1e9a01804bee6489f006953f0760b9dc5e980e304a09b1cda2ec150f5681c',
                    'tapsCount': 17,
                    'vector': '3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2',
                },
            },
            'query': 'mutation MutationGameProcessTapsBatch($payload: TelegramGameTapsBatchInput!) {\n  telegramGameProcessTapsBatch(payload: $payload) {\n    ...FragmentBossFightConfig\n    __typename\n  }\n}\n\nfragment FragmentBossFightConfig on TelegramGameConfigOutput {\n  _id\n  coinsAmount\n  currentEnergy\n  maxEnergy\n  weaponLevel\n  zonesCount\n  tapsReward\n  energyLimitLevel\n  energyRechargeLevel\n  tapBotLevel\n  currentBoss {\n    _id\n    level\n    currentHealth\n    maxHealth\n    __typename\n  }\n  freeBoosts {\n    _id\n    currentTurboAmount\n    maxTurboAmount\n    turboLastActivatedAt\n    turboAmountLastRechargeDate\n    currentRefillEnergyAmount\n    maxRefillEnergyAmount\n    refillEnergyLastActivatedAt\n    refillEnergyAmountLastRechargeDate\n    __typename\n  }\n  bonusLeaderDamageEndAt\n  bonusLeaderDamageStartAt\n  bonusLeaderDamageMultiplier\n  nonce\n  spinEnergyNextRechargeAt\n  spinEnergyNonRefillable\n  spinEnergyRefillable\n  spinEnergyTotal\n  spinEnergyStaticLimit\n  __typename\n}'
        }
    ]

    response = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print("Response Headers:")
    for header, value in response.headers.items():
        print(f"  {header}: {value}")
    print("Response Body:")
    print(response.text)


try:
    driver.get(
        'https://tg-app.memefi.club/#tgWebAppData=query_id%3DAAGdJhs9AwAAAJ0mGz3ngRON%26user%3D%257B%2522id%2522%253A7467640477%252C%2522first_name%2522%253A%2522Hddh%2522%252C%2522last_name%2522%253A%2522J3j4j4%2522%252C%2522language_code%2522%253A%2522ru%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1722013465%26hash%3D3faf9c4b52e399adbb79e25b427b192ccd9555d7e001a8eeb7deadc7aaa61fb5&tgWebAppVersion=7.6&tgWebAppPlatform=ios&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23212121%22%2C%22button_color%22%3A%22%238774e1%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22hint_color%22%3A%22%23aaaaaa%22%2C%22link_color%22%3A%22%238774e1%22%2C%22secondary_bg_color%22%3A%22%23181818%22%2C%22text_color%22%3A%22%23ffffff%22%2C%22header_bg_color%22%3A%22%23212121%22%2C%22accent_text_color%22%3A%22%238774e1%22%2C%22section_bg_color%22%3A%22%23212121%22%2C%22section_header_text_color%22%3A%22%238774e1%22%2C%22subtitle_text_color%22%3A%22%23aaaaaa%22%2C%22destructive_text_color%22%3A%22%23ff595a%22%7D')
    time.sleep(20)
    selenium_cookies = driver.get_cookies()
    cookies = {cookie['name']: cookie['value'] for cookie in selenium_cookies}
    print(cookies)

    time.sleep(1)

    send_request(cookies)

    time.sleep(1000)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
