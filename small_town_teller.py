import pickle


class Person:
    def __init__(self, id: int, first_name: str, last_name: str):
       self.id = id
       self.first_name = first_name
       self.last_name = last_name
       
    def __str__(self):
        return f'{id}{self.first_name}{self.last_name}'

class Account:
    def __init__(self, number: int, type: str, owner: Person, balance: float):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance    
        
class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, person):
            if person.id in self.customers:
                raise ValueError("Person already in system")
            self.customers[id] = person
            
    def print_customers(self):
        for key,value in self.customers.items():
            print(key, value)

    def add_account(self, number, id, balance):
        if number in self.accounts:
            raise ValueError ("Account already exists")
        if id not in self.customers:
            raise ValueError("customer does not exist")
        self.accounts[id] = Account(number, id, balance)

    def remove_account(self, number):
        if number not in self.accounts:
            ValueError("Account does not exist")
        del self.accounts[number]
        
    def deposit(self, number, balance):
        if number not in self.accounts:
            ValueError("Account does not exist")
        return self.accounts[number].deposit(balance)

    def withdraw(self, number, balance):
        if number not in self.accounts:
            ValueError("Account does not exist")
        return self.accounts[number].withdraw(balance)

    def balance_inquiry(self, number, balance):
        if number not in self.accounts:
            ValueError("Account does not exist")
        return self.accounts[id].balance

    def save_data(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Data saved to {'customer_accounts.pickle'}")
        
    def load_data(filename):
        with open('customer_accounts.pickle.py', 'rb') as file:
            Bank = pickle.load(file)
        print(f'Data loaded from {filename}')
        return Bank
            

class PersistenceUtils:
    
    def write_pickle(obj, pickle_file):
        try:
            with open(pickle_file, 'wb') as file:
                pickle.dump(obj, file)
            print(f"Data has been written to {pickle_file}")
        except Exception as e:
            print(f"An error occurred while writing to pickle file: {e}")
       

    def load_pickle(file_path):
        try:
            with open(file_path, 'rb') as file:
                data = pickle.load(file)
                return data
        except FileNotFoundError:
            print(f"The file {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred while reading the pickle file: {e}")
            return None

#999