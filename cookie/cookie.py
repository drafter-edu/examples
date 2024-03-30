from bakery import assert_equal
from drafter import *


@dataclass
class State:
    cookies: int


@route
def index(state: State) -> Page:
    return Page(
        state, ["You have " + str(state.cookies) + " cookies", Button("🍪", cookie)]
    )


@route
def cookie(state: State) -> Page:
    #state.cookies += 1
    return index(State(1))


assert_equal(
    index(State(cookies=0)),
    Page(
        state=State(cookies=0),
        content=["You have 0 cookies", Button(text="🍪", url="/cookie")],
    ),
)

assert_equal(
    cookie(State(cookies=0)),
    Page(
        state=State(cookies=1),
        content=["You have 1 cookies", Button(text="🍪", url="/cookie")],
    ),
)

assert_equal(
    cookie(State(cookies=100)),
    Page(
        state=State(cookies=101),
        content=["You have 101 cookies", Button(text="🍪", url="/cookie")],
    ),
)

start_server(State(0))
