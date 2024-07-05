def get_balance(account_number: str) -> float:
    with open('accounts.txt', 'r') as file:
        for line in file:
            acc_no, balance = line.split(",")
            if acc_no == account_number:
                return float(balance)


def update_account(account_number: str, amount: float):
    with open('accounts.txt', 'r') as file:
        data = file.readlines()

        line_to_update = None

        for i, line in enumerate(data):
            acc_no, _ = line.split(",")
            if acc_no == account_number:
                line_to_update = i
                break

    if line_to_update is not None:
        data[line_to_update] = f"{account_number},{amount:.2f}\n"

        with open('accounts.txt', 'w') as file:
            file.writelines(data)

        return "Updated. Account - {}, Balance - {:.2f}".format(account_number,
                                                                amount)

    else:
        return "Account not found"


def deposit(account_number: str, amount: float):
    balance = get_balance(account_number)
    if balance is None:
        return "Account {} not found".format(account_number)
    else:
        balance += amount
        return update_account(account_number, balance)


def withdraw(account_number: str, amount: float):
    balance = get_balance(account_number)
    if balance is None:
        return "Account {} not found".format(account_number)
    else:
        if balance >= amount:
            balance -= amount
            return update_account(account_number, balance)
        else:
            return "Account {} low on funds".format(account_number)


print(get_balance("3"))
print(get_balance("4"))
print(get_balance("7"))
print(update_account("7", 2))
print(deposit("1", 400))
print(withdraw("5", 150))
