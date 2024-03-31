from drafter import *


@dataclass
class State:
    has_key: bool
    name: str


@route
def index(state: State) -> Page:
    return Page(
        state,
        [
            "Welcome to the adventure! What is your name?",
            TextBox("name", "Adventurer"),
            Button("Begin", begin),
        ],
    )


@route
def begin(state: State, name: str) -> Page:
    state.name = name
    return small_field(state)


@route
def small_field(state: State) -> Page:
    return Page(
        state,
        [
            "You are " + state.name + ".",
            "You are in a small field.",
            "You see paths to the woods and a cave.",
            Button("Cave", cave),
            Button("Woods", woods),
            Image("field.png"),
        ],
    )


@route
def cave(state: State) -> Page:
    if state.has_key:
        return Page(
            state,
            [
                "You enter the cave.",
                "You see a locked door.",
                Button("Unlock door", ending),
                Button("Leave", small_field),
                Image("cave.png"),
            ],
        )
    else:
        return Page(
            state,
            [
                "You enter the cave.",
                "You see a locked door.",
                Button("Leave", small_field),
                Image("cave.png"),
            ],
        )


@route
def woods(state: State) -> Page:
    if state.has_key:
        return Page(
            state,
            ["You are in the woods.", Button("Leave", small_field), Image("woods.png")],
        )
    else:
        return Page(
            state,
            [
                "You are in the woods.",
                "You see a key on the ground.",
                Button("Take key", take_key),
                Button("Leave", small_field),
                Image("woods.png"),
            ],
        )


@route
def take_key(state: State) -> Page:
    state.has_key = True
    return woods(state)


@route
def ending(state: State) -> Page:
    return Page(
        state,
        [
            "You unlock the door.",
            "You find a treasure chest.",
            "You win!",
            Image("victory.png"),
        ],
    )


assert_equal(
    ending(State(has_key=True, name="Ada")),
    Page(
        state=State(has_key=True, name="Ada"),
        content=[
            "You unlock the door.",
            "You find a treasure chest.",
            "You win!",
            Image(url="victory.png", width=None, height=None),
        ],
    ),
)

assert_equal(
    cave(State(has_key=True, name="Ada")),
    Page(
        state=State(has_key=True, name="Ada"),
        content=[
            "You enter the cave.",
            "You see a locked door.",
            Button(text="Unlock door", url="/ending"),
            Button(text="Leave", url="/small_field"),
            Image(url="cave.png", width=None, height=None),
        ],
    ),
)

assert_equal(
    small_field(State(has_key=True, name="Ada")),
    Page(
        state=State(has_key=True, name="Ada"),
        content=[
            "You are Ada.",
            "You are in a small field.",
            "You see paths to the woods and a cave.",
            Button(text="Cave", url="/cave"),
            Button(text="Woods", url="/woods"),
            Image(url="field.png", width=None, height=None),
        ],
    ),
)

assert_equal(
    take_key(State(has_key=False, name="Ada")),
    Page(
        state=State(has_key=True, name="Ada"),
        content=[
            "You are in the woods.",
            Button(text="Leave", url="/small_field"),
            Image(url="woods.png", width=None, height=None),
        ],
    ),
)

assert_equal(
    woods(State(has_key=False, name="Ada")),
    Page(
        state=State(has_key=False, name="Ada"),
        content=[
            "You are in the woods.",
            "You see a key on the ground.",
            Button(text="Take key", url="/take_key"),
            Button(text="Leave", url="/small_field"),
            Image(url="woods.png", width=None, height=None),
        ],
    ),
)

assert_equal(
    small_field(State(has_key=False, name="Ada")),
    Page(
        state=State(has_key=False, name="Ada"),
        content=[
            "You are Ada.",
            "You are in a small field.",
            "You see paths to the woods and a cave.",
            Button(text="Cave", url="/cave"),
            Button(text="Woods", url="/woods"),
            Image(url="field.png", width=None, height=None),
        ],
    ),
)

assert_equal(
    cave(State(has_key=False, name="Ada")),
    Page(
        state=State(has_key=False, name="Ada"),
        content=[
            "You enter the cave.",
            "You see a locked door.",
            Button(text="Leave", url="/small_field"),
            Image(url="cave.png", width=None, height=None),
        ],
    ),
)

assert_equal(
    begin(State(has_key=False, name=""), "Ada"),
    Page(
        state=State(has_key=False, name="Ada"),
        content=[
            "You are Ada.",
            "You are in a small field.",
            "You see paths to the woods and a cave.",
            Button(text="Cave", url="/cave"),
            Button(text="Woods", url="/woods"),
            Image(url="field.png", width=None, height=None),
        ],
    ),
)

assert_equal(
    index(State(has_key=False, name="")),
    Page(
        state=State(has_key=False, name=""),
        content=[
            "Welcome to the adventure! What is your name?",
            TextBox(name="name", kind="text", default_value="Adventurer"),
            Button(text="Begin", url="/begin"),
        ],
    ),
)

start_server(State(False, ""))
