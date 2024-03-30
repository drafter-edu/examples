from drafter import *

@dataclass
class State:
    pass

@route
def index(state: State):
    return Page(state, [
        Header("Example Games"),
        BulletedList([
            Link("Cookie Clicker", "https://drafter-edu.github.io/examples/cookie/"),
            Link("Bank Account", "https://drafter-edu.github.io/examples/bank/"),
            Link("Adventure Game", "https://drafter-edu.github.io/examples/adventure/"),
        ])
    ])

start_server(State())