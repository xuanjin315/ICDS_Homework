# Task: Implement the Item class and the function print_summary(items)
# Do NOT change function/class names.

class Item:
    """Represent a shopping item."""
    def __init__(self, name, amount, unit_price):
        """
        Parameters
        ----------
        name : str
        amount : int or float (non-negative)
        unit_price : int or float (non-negative)
        """
        # TODO: store the three arguments as attributes on self

        self.name=name
        self.amount=amount
        self.unit_price=unit_price


def print_summary(items):
    """
    Print each item's name (one per line), then print the total cost.

    The last line must be:
    Total: <value>

    Parameters
    ----------
    items : list[Item]
        A list of Item objects.

    Returns
    -------
    None
    """
    # TODO:
    # 1) Loop over items and print each item's name.
    # 2) Calculate total cost
    # 3) Print: f"Total: {total}"
    total=0
    for item in items:
        print(item.name)
        total+=item.unit_price*item.amount
    
    print(f"Total: {total}")
        


if __name__ == "__main__":
    # Sample items (you can use these to test after you implement the code)
    items = [
        Item("coke", 1, 10),
        Item("Big Mac", 2, 20),
        Item("chips", 1, 5),
    ]

    # Expected output after your implementation:
    # coke
    # Big Mac
    # chips
    # Total: 55

    # Uncomment the line below after you finish print_summary
    print_summary(items)