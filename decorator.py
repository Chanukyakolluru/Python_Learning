#decorator is used to extend the behavior of another function without modifying the base function
# pass the base function as an argument for decorator.

def add_sprinkles(func):
    def wrapper(*args):
        print("* Add sprinkles to your ice cream **")
        func(*args)
    return wrapper

def add_fudge(func):
    def wrapper(*args):
        print("*you can add fudge*")
        func(*args)
    return wrapper
@add_sprinkles
@add_fudge
def get_icecream(flavour):
    print(f"your fav {flavour} ice cream +🍦")

get_icecream("Vanilla")
print()  # just to creates a line gap btw the lines
get_icecream("Chocolate")
