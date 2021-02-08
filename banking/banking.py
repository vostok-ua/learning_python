import sqlite3
import generator


# initialising database
connection = sqlite3.connect('card.s3db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);")
connection.commit()

# defining global variables:
text_main_screen = "\n1. Create an account\n2. Log into account\n0. Exit\n"
text_authorized = "\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n"

state = "main"
user_id = -1


def create_account():
    pin = generator.pin()
    card = generator.card()
    cursor.execute("SELECT id FROM card;")
    id = cursor.fetchone()
    if id:
        id = max(id) + 1
    else:
        id = 1
    cursor.execute(f"INSERT INTO card (id, number, pin) VALUES ({id}, {card}, {pin});")
    connection.commit()
    print(f"\nYour card has been created\nYour card number:\n{card}\nYour card PIN:\n{pin}")


def log_in():
    global state
    global user_id
    card = input("\nEnter your card number:\n")
    entered_pin = input("Enter your PIN:\n")
    cursor.execute(f"SELECT pin, id FROM card WHERE number = {card}")
    user_info = cursor.fetchone()
    if user_info:
        real_pin = user_info[0]
        if real_pin == entered_pin:
            state = "logged_in"
            user_id = user_info[1]
            print("\nYou have successfully logged in!")
        else:
            print("\nWrong card number or PIN!")
    else:
            print("\nWrong card number or PIN!")


def balance():
    cursor.execute(f"SELECT balance FROM card WHERE id = {user_id}")
    balance = cursor.fetchone()
    balance = balance[0]
    print(f"\nBalance: {balance}")


def add_income():
    income = int(input("\nEnter income:\n"))
    cursor.execute(f"UPDATE card SET balance = balance + {income} WHERE id = {user_id}")
    connection.commit()
    print("Income was added!")


def do_transfer():
    reciever_card = input("\nTransfer\nEnter card number:\n")
    if not generator.luhn("check", reciever_card):
        print("Probably you made a mistake in the card number. Please try again!")
    else:
        cursor.execute(f"SELECT number, balance FROM card WHERE id = {user_id}")
        sender_info = cursor.fetchone()
        sender_card = sender_info[0]
        sender_balance = sender_info[1]
        if sender_card == reciever_card:
            print("You can't transfer money to the same account!")
        else:
            cursor.execute(f"SELECT number FROM card WHERE number = {reciever_card}")
            reciever_info = cursor.fetchone()
            if not reciever_info:
                print("Such a card does not exist.")
            else:
                amount = int(input("Enter how much money you want to transfer:\n"))
                if amount > sender_balance:
                    print("Not enough money!")
                else:
                    cursor.execute(f"UPDATE card SET balance = balance - {amount} WHERE id = {user_id}")
                    connection.commit()
                    cursor.execute(f"UPDATE card SET balance = balance + {amount} WHERE number = {reciever_card}")
                    connection.commit()
                    print("Success!")


def close_account():
    global state
    global user_id
    cursor.execute(f"DELETE FROM card WHERE id = {user_id}")
    connection.commit()
    user_id = -1
    state = "main"


def log_out():
    global state
    global user_id
    user_id = -1
    state = "main"
    print("\nYou have successfully logged out!")


def main():
    global state
    if state == "main":
        action = input(text_main_screen)
        if action == "1":
            create_account()
        elif action == "2":
            log_in()
        elif action == "0":
            state = "exit"
    elif state == "logged_in":
        action = input(text_authorized)
        if action == "1":
            balance()
        elif action == "2":
            add_income()
        elif action == "3":
            do_transfer()
        elif action == "4":
            close_account()
        elif action == "5":
            log_out()
        elif action == "0":
            state = "exit"


while state != "exit":
    main()
print("Bye!")
