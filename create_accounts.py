'''
This script checks if the ATM machine is working properly
'''
import atm_machine as atmm

atm = atmm.ATMMachine()

#Create two differents accounts
atm.create_new_account('123', 'Paula', 2500.0)
atm.create_new_account('456', 'Aldana', 0.0)

#Make a withdraw from both accounts
atm.make_a_withdraw('123', 500)
atm.make_a_withdraw('456', 500)

#Make a transfer from Paula's account to Aldana's account
atm.make_a_transfer('123', '456', 1000)
