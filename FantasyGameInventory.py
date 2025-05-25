 print("Name   : Sahil Gurav")
 print("USN    : 1AY24AI093")
 print("Section: O\n")
def displayInventory(inventory):
    print("Inventory:")
    total_items = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        total_items += count
    print(f"Total number of items: {total_items}")
stuff = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1
}
displayInventory(stuff)
