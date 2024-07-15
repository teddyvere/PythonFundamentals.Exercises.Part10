from small_town_teller import Person, Account, Bank

zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
teddy = Person(2, "Teddy", "Archibald")
zc_bank.add_customer(bob)
zc_bank.add_customer(teddy)
zc_bank.print_customers()

bob_savings = Account(1001, "SAVINGS", bob.id, 100.00)
print(bob_savings)

# zc_bank.add_account(bob_savings)
# zc_bank.balance_inquiry(1001)
# # 0
# zc_bank.deposit(1001, 256.02)
# zc_bank.balance_inquiry(1001)
# # 256.02
# zc_bank.withdrawal(1001, 128)
# zc_bank.balance_inquiry(1001)
# # 128.02