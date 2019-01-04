import csv


def display_inventory(inventory):
    """Display the inventory."""
    total_quantity = 0
    for item, quantity in inventory.items():
        print("{} {}".format(quantity, item))
        total_quantity += quantity
    print("Total number of items: {}" .format(total_quantity))


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    new_loot = dict((item, added_items.count(item))
                    for item in set(added_items))
    for item in new_loot:
        if item in inventory:
            inventory[item] += new_loot[item]
        else:
            inventory[item] = new_loot[item]
    return inventory


def print_table(inventory, order=None):
    """
    Take your inventory and display it in a well-organized table with
    each column right-justified.
    """
    longest_str_keys = ([len(str(x)) for x in inventory.keys()])
    longest_str_values = ([len(str(x)) for x in inventory.keys()])
    longest_string = max(longest_str_keys + longest_str_values)

    print("Inventory:")
    print("{:>{ls}}  {:>{ls}}".format("count", "item name", ls=longest_string))
    # + 2 due to space between lower list
    print("-" * (longest_string * 2 + 2))
    total_quantity = 0

    if order == "empty":
        order_is_unordered(inventory, longest_string, total_quantity)

    elif order == "count,desc":
        order_is_descending(inventory, longest_string, total_quantity)

    elif order == "count,asc":
        order_is_ascending(inventory, longest_string, total_quantity)


def order_is_unordered(inventory, longest_string, total_quantity):
    """
    The 'order' parameter (string) works as follows:
    None (by default) means the table is unordered
    """
    for item, quantity in inventory.items():
        print(
            "{:>{ls}}  {:>{ls}}".format(
                quantity,
                item,
                ls=longest_string))
        total_quantity += int(quantity)
    print("-" * (longest_string * 2 + 2))
    print("Total number of items: {}".format(total_quantity))


def order_is_descending(inventory, longest_string, total_quantity):
    """
    The 'order' parameter (string) works as follows:
    "count,desc" means the table is ordered by count (of items in the
    inventory) in descending order
    """
    inventory = dict(
        sorted(
            inventory.items(),
            key=lambda x: x[1],
            reverse=True))
    for item, quantity in inventory.items():
        print(
            "{:>{ls}}  {:>{ls}}".format(
                quantity,
                item,
                ls=longest_string))
        total_quantity += int(quantity)
    print("-" * (longest_string * 2 + 2))
    print("Total number of items: {}".format(total_quantity))


def order_is_ascending(inventory, longest_string, total_quantity):
    """
    The 'order' parameter (string) works as follows:
    "count,asc" means the table is ordered by count in ascending order
    """
    inventory = dict(
        sorted(
            inventory.items(),
            key=lambda x: x[1],
            reverse=False))
    for item, quantity in inventory.items():
        print(
            "{:>{ls}}  {:>{ls}}".format(
                quantity,
                item,
                ls=longest_string))
        total_quantity += int(quantity)
    print("-" * (longest_string * 2 + 2))
    print("Total number of items: {}".format(total_quantity))


def import_inventory(inventory, filename="import_inventory.csv"):
    """
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    """
    with open(filename) as file_object:
        loot_list = []
        for item in file_object:
            loot_list = item.rstrip().split(",")
        print(loot_list)
        add_to_inventory(inventory, loot_list)
        print_table(inventory, order="count,desc")
    return inventory


def export_inventory(inventory, filename="export_inventory.csv"):
    """
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    """
    with open(filename, 'w') as file_object:
        results = []
        for k, v in inventory.items():
            unpack_list = [k] * v
            results.extend(unpack_list)
        print(results)

        write_to_column = csv.writer(file_object)
        write_to_column.writerow(results)
