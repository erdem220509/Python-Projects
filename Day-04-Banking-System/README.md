# Day #4 — Object-Oriented Banking System 🏦

A command-line banking system built with Python to practice Object-Oriented Programming (OOP), inheritance, method overriding, and polymorphism.

## Features

- Create Savings and Checking accounts
- Automatically generate account numbers
- Deposit money
- Withdraw money
- View all accounts
- Apply interest to Savings accounts
- Overdraft support for Checking accounts
- Input validation
- Manage multiple account objects

## Account Types

### BankAccount

The base class containing common account functionality:

- Owner
- Account number
- Balance
- Deposit
- Withdraw
- Display account information

### SavingsAccount

Inherits from `BankAccount` and adds:

- Interest rate
- `apply_interest()` method

Example:

```text
Balance: $1000
Interest Rate: 5%

After interest:
Balance: $1050