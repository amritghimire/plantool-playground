"""Small deterministic fixture for PlanTool's agent workflow."""


def greet(name: str) -> str:
    """Return a greeting after removing surrounding whitespace."""
    if not isinstance(name, str):
        raise TypeError("name must be text")
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
