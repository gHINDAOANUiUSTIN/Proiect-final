from valid_accounts import valid_accounts


def remove_account(account):
    valid_accounts.remove(account)


def update_valid_accounts_file(account):
    with open('valid_accounts.py', 'w') as f:
        f.write("valid_accounts = " + str(account))
