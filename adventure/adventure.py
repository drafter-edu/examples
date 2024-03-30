from drafter import *

@dataclass
class State:
    has_key: bool
    name: str
    
@route
def index(state: State) -> Page:
    return Page(state, [
        "Welcome to the adventure! What is your name?",
        TextBox("name", "Adventurer"),
        Button("Begin", begin)
    ])
    
@route
def begin(state: State, name: str) -> Page:
    state.name = name
    return small_field(state)

@route
def small_field(state: State) -> Page:
    return Page(state, [
        "You are " + state.name + ".",
        "You are in a small field.",
        "You see paths to the woods and a cave.",
        Button("Cave", cave),
        Button("Woods", woods),
        Image("field.png")
    ])
    
@route
def cave(state: State) -> Page:
    if state.has_key:
        return Page(state, [
            "You enter the cave.",
            "You see a locked door.",
            Button("Unlock door", ending),
            Button("Leave", small_field),
            Image("cave.png")
        ])
    else:
        return Page(state, [
            "You enter the cave.",
            "You see a locked door.",
            Button("Leave", small_field),
            Image("cave.png")
        ])

    
@route
def woods(state: State) -> Page:
    if state.has_key:
        return Page(state, [
            "You are in the woods.",
            Button("Leave", small_field),
            Image("woods.png")
        ])
    else:
        return Page(state, [
            "You are in the woods.",
            "You see a key on the ground.",
            Button("Take key", take_key),
            Button("Leave", small_field),
            Image("woods.png")
        ])
    
@route
def take_key(state: State) -> Page:
    state.has_key = True
    return woods(state)

@route
def ending(state: State) -> Page:
    return Page(state, [
        "You unlock the door.",
        "You find a treasure chest.",
        "You win!",
        Image("victory.png")
    ])
    
start_server(State(False, ""))