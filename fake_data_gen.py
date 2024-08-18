import csv
import random
import string
from faker import Faker
from faker.providers import DynamicProvider

#Initialize Faker instance
fake = Faker()

#Lists of possible values for various fields that weren't covered by the Faker library
debt_types = ['Credit Card', 'Student Loan', 'Mortgage', 'Auto Loan', 'Personal Loan', 'Medical Debt', "Business Debt"]
salary_frequencies = ["Weekly", "Biweekly", "Semimonthly", "Monthly"]
top_banks_in_america = ["JPMorgan Chase & Co.", "Bank of America", "Wells Fargo & Co.", "Citigroup Inc.", "Goldman Sachs Group Inc.", "Morgan Stanley", "U.S. Bancorp", "TD Bank, N.A.", "PNC Financial Services Group Inc.", "Capital One Financial Corporation", "HSBC Bank USA", "Citizens Financial Group Inc.", "Regions Financial Corporation", "Fifth Third Bancorp", "KeyBank", "BB&T Corporation", "SunTrust Banks, Inc.", "Ally Bank", "Discover Financial Services", "Synchrony Financial", "M&T Bank Corporation", "Northern Trust Corporation", "Charles Schwab Corporation", "BMO Harris Bank N.A.", "American Express National Bank"]
bank_acc_types = ["Checking", "Savings", "Certificate of Deposit", "Money Market"]
phone_types = ["Mobile", "Work", "Home"]
relationships = ['Spouse', 'Parent', 'Child', 'Sibling', 'Friend', 'Colleague']
yes_no = ["Yes", "No"]


#Manually create necessary address line generator
def generate_address_line_extension():
    """
    Generate a random address line for one of the fields.
    Possible formats include: 'Apt. ###', 'Suite ###', 'Unit ###', 'Building ###'.

    Returns:
        str: Randomly generated address line 2.
    """
    line_2 = fake.random_element(['Apt. ###', 'Suite ###', 'Unit ###', 'Building ###'])
    line_2 = line_2.replace('###', str(fake.random_number(digits=3)))  # Replace ### with a random number
    return line_2



#Define column names (features)
fields = ["DebtorId", "Account Number", "First Name", "Middle Name", "Last Name", "Address 1", "Address 2", "City", "State", "Zip", "Debtor Driver License", "Debtor SSN", "Debtor Date of Birth", "Debtor Email", "Debtor Credit Score", "Date of Origination", "Issuer", "State of Origin", "Date Charged Off", "Amount Financed", "Principal Outstanding", "Balance Due", "Debt Type", "Loan Term", "Loan Maturity", "Salary Frequency", "Employer Name", "Work Number", "Work Address", "Work Address Extension", "Work City", "Work State", "Work Zip", "Bank Name", "Bank Routing Number", "Bank Account Number", "Bank Account Type", "Debtor Phone 1 Number", "Debtor Phone 1 Type", "Debtor Phone 2 Number", "Debtor Phone 2 Type", "Ref 1 Name", "Ref 1 Relation", "Ref 1 Home Phone", "Ref 2 Name", "Ref 2 Relation", "Ref 2 Home Phone", "Home Text Permission", "Home Dialer Permission", "Cell Text Permission", "Cell Dialer Permission", "Charge Off Date", "Charge Off Balance", "Interest After Charge Off", "Fees After Charge Off", "Adjustments After Charge Off", "Payments After Charge Off"]



def generate_fake_data(num_entries):
    data = []
    num_entries = 10000
    for i in range(num_entries):
        entry = fake.user_name()
        account_num = fake.passport_number()
        first_name = fake.first_name()
        middle_name = random.choice(string.ascii_uppercase)
        last_name = fake.last_name()
        address1 = fake.street_address()
        address2 = fake.unique.street_address()
        city = fake.city()
        state = fake.state()
        zip = fake.postcode()
        driver_license = fake.pyint(min_value=100000, max_value=999999)
        ssn = fake.ssn()
        date_of_birth = fake.date_of_birth() #does object work
        email = fake.email()
        credit_score = fake.pyint(min_value=300, max_value=850)
        date_of_origination = fake.date() #ig origination is just when the account or debt was created/issued
        issuer = fake.company()
        state_of_orig = fake.state()
        date_charged_off = fake.date() #CHANGE
        amount_financed = fake.pyint(min_value=500, max_value=150000)
        orig_loan_amt = amount_financed
        principal_outstanding = fake.pyint(min_value=1, max_value=orig_loan_amt-1)
        current_principal_outstanding = principal_outstanding
        balance_due = fake.pyint(min_value=current_principal_outstanding, max_value=orig_loan_amt-1)
        current_bal_due = balance_due
        debt_type = random.choice(debt_types)
        loan_term = fake.pyint(min_value=4, max_value=64)
        loan_maturity_date = fake.date() #may needa change
        salary_frequency = random.choice(salary_frequencies)
        employer_name = fake.company()
        work_number = fake.phone_number()
        work_address = fake.street_address()
        work_address_extension = generate_address_line_extension()
        work_city = fake.city()
        work_state = fake.state()
        work_zip = fake.postcode()
        bank_name = random.choice(top_banks_in_america)
        bank_routing_number = fake.aba()
        bank_account_number = fake.bban()
        bank_account_type = random.choice(bank_acc_types)
        debtor_phone1_num = fake.phone_number()
        debtor_phone1_type = random.choice(phone_types)
        debtor_phone2_num = fake.phone_number()
        debtor_phone2_type = random.choice(phone_types)
        ref1_name = fake.first_name()
        ref1_relation = random.choice(relationships)
        ref1_home_phone = fake.phone_number()
        ref2_name = fake.first_name()
        ref2_relation = random.choice(relationships)
        ref2_home_phone = fake.phone_number()
        hometext_perm = random.choice(yes_no)
        homedialer_perm = random.choice(yes_no)
        celltext_perm = random.choice(yes_no)
        celldialer_perm = random.choice(yes_no)
        charge_off_date = fake.date()
        charge_off_balance = fake.pyint(min_value=50, max_value=current_bal_due-1)
        current_charge_off_bal = charge_off_balance
        interest_after_charge_off = fake.pyint(min_value=10, max_value=current_charge_off_bal-5)
        fees_after_charge_off = fake.pyint(min_value=10, max_value=current_charge_off_bal-20)
        adjustments_after_charge_off = fake.pyint(min_value=0, max_value=10)
        payments_after_charge_off = fake.pyint(min_value=0, max_value=10)
        data.append([entry, account_num, first_name, middle_name, last_name, address1, address2, city, state, zip, driver_license, ssn, date_of_birth, email, credit_score, date_of_origination, issuer, state_of_orig, date_charged_off, amount_financed, principal_outstanding, balance_due, debt_type, loan_term, loan_maturity_date, salary_frequency, employer_name, work_number, work_address, work_address_extension, work_city, work_state, work_zip, bank_name, bank_routing_number, bank_account_number, bank_account_type, debtor_phone1_num, debtor_phone1_type, debtor_phone2_num, debtor_phone2_type, ref1_name, ref1_relation, ref1_home_phone, ref2_name, ref2_relation, ref2_home_phone, hometext_perm, homedialer_perm, celltext_perm, celldialer_perm, charge_off_date, charge_off_balance, interest_after_charge_off, fees_after_charge_off, adjustments_after_charge_off, payments_after_charge_off])
    return data



def write_to_csv(filename, fields, data):
    """
    Write the generated data to a CSV file.

    Arguments:
        filename (str): The name of the file to write to.
        fields (list): List of column headers.
        data (list): List of data rows (containing generated values) to write.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        writer.writerows(data)



#Execution
if __name__ == "__main__":
    num_entries = 10000
    data = generate_fake_data(num_entries)
    filename = 'fake_data_remynt.csv'
    write_to_csv(filename, fields, data)