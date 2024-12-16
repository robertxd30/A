from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from eth_account import Account

Account.enable_unaudited_hdwallet_features()

sub_wallet_count = 1

options = Options()
options.add_argument("start-maximized")

def get_balance(public_key):
    driver.get("https://debank.com/profile/" + public_key)
    try:
        total_asset_div = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "HeaderInfo_totalAssetInner__HyrdC"))
        )
        total_asset_value = total_asset_div.text.strip()
        print("Total Asset Value:")
        print(total_asset_value)
    except Exception as e:
        print(f"Error locating the asset value: {e}")
 

with open('ethseed.txt', 'r') as file, open('ethseedoutput.txt', 'a') as outfile:
    global driver
    driver = webdriver.Chrome(options=options)
    for line in file:
        seed_phrase = line.strip()  # Remove any extra whitespace or newline characters
        if seed_phrase:  # Check if the line is not empty
            try:
                for i in range(sub_wallet_count):
                    acc = Account.from_mnemonic(seed_phrase, account_path=f"m/44'/60'/0'/0/{i}")
                    balance = get_balance(acc.address)
                    outfile.write(f"Seed Phrase: {seed_phrase}\nPublic Key: {acc.address}\nBalance: {balance}")
            except Exception as e:
                print(f"Error generating public key for seed phrase '{seed_phrase}': {e}")
    driver.quit()