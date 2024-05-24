import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():  #to get the key and the value
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [[], [], []]
    for _ in range(cols):
        column = []
        current_sybmols = all_symbols[:] #to copy a list
        for _ in range(rows):
            value = random.choice(current_sybmols)
            current_sybmols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def deposit():
    while True:
        amount = input("What is your deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")

    return amount


def get_number_of_line():
    while True:
        lines = input("How many lines to bet on? (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please provide valid number of lines")
        else:
            print("Please enter a number")

    return lines


def get_bet():
    while True:
        amount = input("What is your bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Your balance doesnt have enough money, you current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")


main()
