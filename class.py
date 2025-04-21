class favoriteIceCream:
    def __init__(self, flavor: str):
        self.flavor = flavor

    def __str__(self):
        return f"My favorite ice cream flavor is {self.flavor}."
    

class favoriteIceCream2:
    def __init__(self, flavor: str):
        self.flavor = flavor

    def __str__(self):
        return f"My favorite ice cream flavor is {self.flavor}."
    

print(favoriteIceCream("chocolate"))
print(favoriteIceCream2("vanilla"))
# Output:
# My favorite ice cream flavor is chocolate.
# My favorite ice cream flavor is vanilla.