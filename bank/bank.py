"""
The ``State`` for the webpage should have only one integer field: ``balance``
"""

from drafter import *
from dataclasses import dataclass


@dataclass
class State:
    balance: int


@route
def index(state: State) -> Page:
    return Page(
        state,
        [
            "Your current balance is:",
            str(state.balance),
            Button("Withdraw", start_withdraw),
            Button("Deposit", start_deposit),
        ],
    )


@route
def start_withdraw(state: State) -> Page:
    return Page(
        state,
        [
            "How much would you like to withdraw?",
            TextBox("amount", 10),
            Button("Withdraw", finish_withdraw),
            Button("Cancel", index),
        ],
    )


@route
def finish_withdraw(state: State, amount: int) -> Page:
    state.balance -= amount
    return index(state)


@route
def start_deposit(state: State) -> Page:
    return Page(
        state,
        [
            "How much would you like to deposit?",
            TextBox("amount", 10),
            Button("Deposit", finish_deposit),
            Button("Cancel", index),
        ],
    )


@route
def finish_deposit(state: State, amount: int) -> Page:
    state.balance += amount
    return index(state)


# Check that the index page renders correctly
assert_equal(
    index(State(balance=100)),
    Page(
        state=State(balance=100),
        content=[
            "Your current balance is:",
            "100",
            Button(text="Withdraw", url="/start_withdraw"),
            Button(text="Deposit", url="/start_deposit"),
        ],
    ),
)

# Check that the start_withdraw page renders correctly
assert_equal(
    start_withdraw(State(balance=100)),
    Page(
        state=State(balance=100),
        content=[
            "How much would you like to withdraw?",
            TextBox(name="amount", kind="text", default_value=10),
            Button(text="Withdraw", url="/finish_withdraw"),
            Button(text="Cancel", url="/"),
        ],
    ),
)

# Check that the finish_withdraw updates the state correctly
assert_equal(
    finish_withdraw(State(balance=100), 10),
    Page(
        state=State(balance=90),
        content=[
            "Your current balance is:",
            "90",
            Button(text="Withdraw", url="/start_withdraw"),
            Button(text="Deposit", url="/start_deposit"),
        ],
    ),
)

# Check that the start_deposit page renders correctly
assert_equal(
    start_deposit(State(balance=90)),
    Page(
        state=State(balance=90),
        content=[
            "How much would you like to deposit?",
            TextBox(name="amount", kind="text", default_value=10),
            Button(text="Deposit", url="/finish_deposit"),
            Button(text="Cancel", url="/"),
        ],
    ),
)

# Check that the finish_deposit updates the state correctly
assert_equal(
    finish_deposit(State(balance=90), 20),
    Page(
        state=State(balance=110),
        content=[
            "Your current balance is:",
            "110",
            Button(text="Withdraw", url="/start_withdraw"),
            Button(text="Deposit", url="/start_deposit"),
        ],
    ),
)

# Another check for finishing the deposit
assert_equal(
    finish_deposit(State(balance=100), 20),
    Page(
        state=State(balance=120),
        content=[
            "Your current balance is:",
            "120",
            Button(text="Withdraw", url="/start_withdraw"),
            Button(text="Deposit", url="/start_deposit"),
        ],
    ),
)


start_server(State(100))
