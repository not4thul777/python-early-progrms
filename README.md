# Python Early Programs 🐍

A collection of small Python projects that I'm building while learning Python.

---

## 🎉 New Year Countdown

Counts down from 10 to 0 and wishes you a happy new year.

### Run

```bash
python happy_newyear_countdown.py
```

### Sample output

```text
10
9
8
7
6
5
4
3
2
1
0
🎉 Happy New Year!
```

---

## 🛒 Shopping Cart

A simple shopping cart application that stores food items in lists and calculates the total bill.

### Run

```bash
python shopping_cart.py
```

### Sample output

```text
Enter a food to buy (q to quit): Burger
Enter the price of Burger: $5

Enter a food to buy (q to quit): Pizza
Enter the price of Pizza: $10

Enter a food to buy (q to quit): q

------ YOUR CART ------

Burger - $5.00
Pizza - $10.00

Your total is: $15.00
```

---

---

## 🧠 Quiz Game

A multiple-choice quiz game that asks general knowledge questions and calculates the final score.

### Run

```bash
python quiz_game.py
```

### Sample output

```text
-------------------------
how many continents are there?

A. 7
B. 6
C. 8
D. 5
E. 9

Enter (A, B, C, D, or E): A

CORRECT!

-------------------------
RESULTS
-------------------------

Answers: A A A A A
Guesses: A A A B A

Your score is: 80%
```
---

## 🍕 Concession Stand

A simple concession stand program that displays a menu, allows users to select items, and calculates the total price.

### Run

```bash
python concession_stand.py
```

### Sample output

```text
-----------MENU-----------

pizza     : $10.00
burger    : $8.00
salad     : $6.00
soda      : $2.00
pasta     : $12.00

--------------------------

select an item (q to quit): pizza
select an item (q to quit): soda
select an item (q to quit): q

-----------CART-----------

pizza soda

total is: $12.00
```
---

## 🎮 Number Guessing Game

A game where the player tries to guess a randomly generated number between 1 and 100.

### Run

```bash
python number_guessing_game.py
```

### Sample output

```text
Python Number Guessing Game

Secret number between 1 and 100

Enter your guess: 50
Too low! Try again.

Enter your guess: 75
Too high! Try again.

Enter your guess: 63

Congratulations! You've guessed the number 63 in 3 attempts.

Game Over. Thank you for playing!
```

---

## ✊ Rock Paper Scissors

A classic Rock-Paper-Scissors game where the player competes against the computer.

### Run

```bash
python rock_paper_scissors.py
```

### Sample output

```text
enter a choice (rock, paper, scissors): rock

Player: rock
Computer: scissors

You win!

play again? (y/n): y
```

---

## 🎲 Dice Roller

A dice-rolling simulator that displays ASCII art for each die and calculates the total.

### Run

```bash
python dice_roller.py
```

### Sample output

```text
How many dice do you want to roll? 3

┌─────────┐  ┌─────────┐  ┌─────────┐
│  ●      │  │  ●   ●  │  │         │
│    ●    │  │    ●    │  │    ●    │
│      ●  │  │  ●   ●  │  │         │
└─────────┘  └─────────┘  └─────────┘

total: 9
```
---

## 🏦 Banking Program

A simple console-based banking program that allows users to check their balance, deposit money, withdraw money, and exit the program.

### How to run

```bash
python banking_program.py
```

### Sample output

```text
---------------------
    BANKING PROGRAM
---------------------
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
---------------------
Enter your choice (1-4): 2

Enter an amount to deposit: 100

---------------------
    BANKING PROGRAM
---------------------
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
---------------------
Enter your choice (1-4): 1

---------------------
Your balance is $100.00
---------------------
```
---

## 🎰 Slot Machine

A console-based slot machine game where players can bet their balance and win different payouts by matching symbols.

### How to run

```bash
python slot_machine.py
```

### Sample output

```text
-----------------------------
    WELCOME TO THE SLOT MACHINE
Symbols: 🍒 🍉 🍋 🔔 ⭐
-----------------------------
Current balance: $100
Place your bet amount: 10

Spinning......

****************
🍋 | 🍋 | 🍋
****************

YOU WON $50
Do you want to spin again? (Y/N): N

----------------------------------------------
GAME OVER!!! YOUR FINAL BALANCE IS $140
----------------------------------------------
```
---

## 🔐 Encryption & Decryption

A simple substitution cipher that randomly generates an encryption key and uses it to encrypt and decrypt messages.

### How to run

```bash
python encryption.py
```

### Sample output

```text
Enter a message to encrypt: hello

Original message: hello
Encrypted message: %2ii7

Enter a message to decrypt: %2ii7

Encrypted message: %2ii7
Original message: hello
```

> Note: The encrypted output will be different each time because the encryption key is randomly shuffled.

---

## 🎯 Hangman

A classic Hangman game where the player tries to guess a randomly selected word one letter at a time.

### How to run

Make sure both `hangman.py` and `wordlist.py` are in the same folder.

```bash
python hangman.py
```

### Sample output

```text
------------------------
 o
/|\
/ \
------------------------
_ _ _ _ _

Enter a letter: a

_ _ a _ _
```

### Features

- 🎲 Random word selection
- 🔤 Letter guessing
- ❤️ Limited wrong guesses
- 📝 Displays guessed letters
- 🎯 Win and lose conditions

## 🚀 How to run this repository

1. Clone the repository:

```bash
git clone https://github.com/not4thul777/python-early-programs.git
```

2. Open the folder:

```bash
cd python-early-programs
```

3. Run any project:

```bash
python shopping_cart.py
```

## 📚 Requirements

- Python 3.x

## 👨‍💻 Author

Athul Krishna A
