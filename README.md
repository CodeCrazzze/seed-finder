Ethereum Balance Finder

This code is a Python program designed to search for Ethereum balances associated with specific seed phrases. It utilizes various libraries such as eth_account, colorama, and web3 for interacting with the Ethereum network, as well as aiohttp and asyncio for asynchronous request handling.

The program begins by importing the necessary modules and setting the console title to display the ETH balance. It then initializes the Finder class, which is responsible for the main logic of the program.

The Finder class includes the following methods and attributes:

__init__(self, word_сount: int, process: int, token: str): This is the constructor of the class, which initializes the object's attributes including the word count (word_сount) in the seed phrase, the number of processes (process), and the API token (token).
generate_mnemonic(self, words: str) -> List[str]: This method generates a seed phrase of the specified length (word_count) from a list of words (words).
cheaker(self, session: object, seed_phrase: str) -> None: This method checks the ETH balance for a given seed phrase (seed_phrase) by connecting to the Ethereum network using the web3 library. The result is written to the result.txt file and displayed in the console.
start(self) -> None: This method initiates the process of searching for ETH balances. It reads the word list from a file (WORDS_LIST_PATH), creates an aiohttp.ClientSession(), and generates seed phrases in a loop, passing them to the cheaker() method for verification.
Next, there is a function enter_lenght_words() that prompts the user to enter the length of the seed phrase in terms of the number of words. The function returns the selected value.

In the main part of the code, the API token, the number of processes, and the length of words for the seed phrase are obtained from the user. Then, an instance of the Finder class is created with the specified parameters. Multiple threads are created and started to execute the start() method of the Finder object. The threads wait for their completion using thread.join().

Overall, this code implements a multi-threaded mechanism for efficiently searching for Ethereum balances associated with seed phrases. It utilizes asynchronous request handling and parallel threads to speed up the process.
