# Debt Data Generation Script

## Overview
This script generates synthetic debtor data for testing and research purposes. The generated data includes personal, financial, and debt-related information.

## Features
**Personal Information**: Names, addresses, contact details, and identification numbers.
**Financial Information**: Bank details, credit scores, and employment information.
**Debt Details**: Types of debt, amounts financed, balances due, and charge-off information.

## Usage
1. Install the required dependencies using `pip install faker`.
2. Run the script using `python fake_data_gen.py`.
3. The script will output a CSV file (`fake_data_remynt.csv`) with 10,000 entries.

## Dependencies
- Python 3.x
- Faker Library ([Link]([url](https://faker.readthedocs.io/en/master/)))

## Notes
**Data Integrity**: This script generates random data, and the results should not be used for real-world applications without further validation.
**Data Volume**: The default number of entries is set to 10,000, but this can be adjusted by changing the num_entries parameter in the script.
