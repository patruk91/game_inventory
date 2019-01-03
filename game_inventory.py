inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    """Display the inventory."""
    total_quantity = 0
    for item, quantity in inventory.items():
        print("{} {}".format(quantity, item))
        total_quantity += quantity
    return "Total number of items: {}" .format(total_quantity)


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""

    new_loot = dict((item, added_items.count(item)) for item in set(added_items))
    for item in new_loot:
        if item in inventory:
            inventory[item] += new_loot[item]
        else:
            inventory[item] = new_loot[item]
    return display_inventory(inventory)



def print_table(inventory, order=None):
    """
    Take your inventory and display it in a well-organized table with
    each column right-justified.

    The 'order' parameter (string) works as follows:
    - None (by default) means the table is unordered
    - "count,desc" means the table is ordered by count (of items in the
      inventory) in descending order
    - "count,asc" means the table is ordered by count in ascending order
    """
    longest_str_keys = ([len(str(x)) for x in inventory.keys()])
    longest_str_values = ([len(str(x)) for x in inventory.keys()])
    longest_string = max(longest_str_keys + longest_str_values)


    print("Inventory:")
    print("{:>{ls}}  {:>{ls}}".format("count", "item name", ls=longest_string))
    print("-" * (longest_string * 2 + 2))  # + 2 due to space between lower list
    total_quantity = 0

    if order == "empty":
        for item, quantity in inventory.items():
            print("{:>{ls}}  {:>{ls}}" .format(quantity, item, ls=longest_string))
            total_quantity += int(quantity)
        print("-" * (longest_string * 2 + 2))
        return "Total number of items: {}" .format(total_quantity)

    elif order == "count,desc":
        inventory = dict(sorted(inventory.items(), key=lambda x: x[1], reverse=True))
        for item, quantity in inventory.items():
            print("{:>{ls}}  {:>{ls}}" .format(quantity, item, ls=longest_string))
            total_quantity += int(quantity)
        print("-" * (longest_string * 2 + 2))
        return "Total number of items: {}" .format(total_quantity)

    elif order == "count,asc":
        inventory = dict(sorted(inventory.items(), key=lambda x: x[1], reverse=False))
        for item, quantity in inventory.items():
            print("{:>{ls}}  {:>{ls}}" .format(quantity, item, ls=longest_string))
            total_quantity += int(quantity)
        print("-" * (longest_string * 2 + 2))
        return "Total number of items: {}" .format(total_quantity)


def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    '''

    pass


def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''

    pass

print(add_to_inventory(inventory, dragon_loot))
print(print_table(inventory, order="count,asc"))