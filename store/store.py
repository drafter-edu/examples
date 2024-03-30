from drafter import *

@dataclass
class Item:
    name: str
    price: int
    stock: int

@dataclass
class State:
    items: list[Item]
    

@route
def index(state: State) -> Page:
    return Page(state, [
        "Welcome to the store!",
        "Select an item to purchase:",
    ])
    
@route
def purchase(state: State, item: Item) -> Page:
    if item.stock > 0:
        item.stock -= 1
        return Page(state, [
            "You have purchased a " + item.name + " for " + str(item.price) + " coins",
            Button("Return to store", index)
        ])
    else:
        return Page(state, [
            "Sorry, we are out of stock of " + item.name,
            Button("Return to store", index)
        ])
