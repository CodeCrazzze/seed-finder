from eth_account import Account
from colorama import init
from colorama import Fore
from web3 import Web3

from typing import List
import config

import aiohttp
import asyncio
import ctypes

import random
import threading


# Init
ctypes.windll.kernel32.SetConsoleTitleA(b"Balance: 0.00 ETH")
Account.enable_unaudited_hdwallet_features()
init()


class Finder:
    def __init__(
            self,
            word_сount: int,
            process: int,
            token: str
        ) -> None:

        self.token: str = token
        self.word_count: int = word_сount
        self.process: int = process

        self.balance: int = 0


    def generate_mnemonic(self, words: str) -> List[str]:
        mnemonic = []
        word_list = words.split('\n')

        for _ in range(self.word_count):
            word = random.choice(word_list)
            mnemonic.append(word)

        return mnemonic


    async def cheaker(
            self,
            session: object,
            seed_phrase: str
        ) -> None:

        try:
            private_key = Account.from_mnemonic(seed_phrase).key
        except:
            return
        address = Account.from_key(private_key).address

        # Connect to the Ethereum network using web3
        w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{self.token}'))

        # Get the balance using web3
        balance_wei = w3.eth.get_balance(address)
        balance_eth = w3.from_wei(balance_wei, 'ether')

        color = Fore.RED
        if balance_eth > 0:
            with open("result.txt", "a") as file:
                file.write(seed_phrase + "\n")
                self.balance += balance_eth
            ctypes.windll.kernel32.SetConsoleTitleA(b"Balance: " + str(self.balance).encode() + b' ETH')
            color = Fore.GREEN
        print(color + f"{address}:{balance_eth} ETH - " + seed_phrase)


    async def start(self) -> None:
        with open(config.WORDS_LIST_PATH, "r") as file:
            data = file.read()

        async with aiohttp.ClientSession() as session:
            while True:
                seed_phrase = " ".join(self.generate_mnemonic(data))
                await self.cheaker(session, seed_phrase)




def enter_lenght_words() -> int:
    print("""Выберете количество слов в секретной фразе:\n1. 12 слов\n2. 15 слов\n3. 18 слов\n4. 21 слов\n5. 24 слов""")
    result = int(input(":"))

    match result:
        case 1:
            return 12
        case 2:
            return 15
        case 3:
            return 18
        case 4:
            return 21
        case 5:
            return 24
        case _:
            print("[ERROR] Данные не верны, повторите попытку")
            return enter_lenght_words()


if __name__ == "__main__":
    api_token = input("Введите ваш api token от сайта https://www.infura.io/:")
    process = int(input("Введите колличество процессов: "))

    word_count = enter_lenght_words()


    finder = Finder(
        word_сount=word_count,
        process=process,
        token=api_token
    )

    threads = []
    for _ in range(process):
        thread = threading.Thread(target=lambda: asyncio.run(finder.start()))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()