from eth_account import Account
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from eth_account import Account

Account.enable_unaudited_hdwallet_features()
options = Options()
options.add_argument("start-maximized")

def get_balance(public_key):
    driver.get("https://debank.com/profile/" + public_key)
    try:
        total_asset_div = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "HeaderInfo_totalAssetInner__HyrdC"))
        )
        total_asset_value = total_asset_div.text.strip()
        print("Total Asset Value:")
        print(total_asset_value)
    except Exception as e:
        print(f"Error locating the asset value: {e}")

file_path = './ethpvkey.txt'
output_file_path = './ethpvoutput.txt'

with open(file_path, 'r') as infile, open(output_file_path, 'a') as outfile:
    global driver
    driver = webdriver.Chrome(options=options)
    for line in infile:
        private_key = line.strip()
        if private_key:
            try:
                account = Account.from_key(private_key)
                public_key = account.address
                balance = get_balance(public_key)
                outfile.write(f'{private_key} {public_key} {balance}\n')
            except Exception as e:
                print(f'Error processing private key {private_key}: {e}')
    driver.quit()
