"""Pancakes."""


def make_n_pancakes(n: int, ingredients: list) -> int:
    """
    Make n pancakes.

    If you can not make n pancakes, make as many as you can.
    If you can make more than n pancakes, do not make more. In that case make exactly n pancakes.

    Use the following functions here.
    Tip: the first step would be making dough.

    :param n: how many pancakes you have to make
    :param ingredients: given ingredients
    :return: amount of pancakes made
    """
    dough_amount = make_dough(ingredients)
    pancakes = 0

    while can_make_pancake(dough_amount) and pancakes < n:
        dough_amount = make_a_pancake(dough_amount)
        pancakes += 1
    return pancakes


def make_dough(ingredients: list) -> int:
    """
    You must always make as much dough as possible regardless of how many pancakes you are going to make.

    To make 7dl dough, it takes:
    One part egg, 5 parts milk, 4 parts flour, 1 part butter, 2 parts sugar.
    PS! It's a random recipe I made up, do not try to pancake according to this.

    :param ingredients: given ingredients as a list
    :return: dough made in dl
    """
    egg_count = ingredients.count("egg")
    milk_count = ingredients.count("milk")
    flour_count = ingredients.count("flour")
    butter_count = ingredients.count("butter")
    sugar_count = ingredients.count("sugar")
    dough_amount = 0
    while egg_count >= 1 and milk_count >= 5 and flour_count >= 4 \
            and butter_count >= 1 and sugar_count >= 2:
        dough_amount += 7
        egg_count -= 1
        milk_count -= 5
        flour_count -= 4
        butter_count -= 1
        sugar_count -= 2
    return dough_amount


def can_make_pancake(dough_amount: float) -> bool:
    """
    Making one pancake takes 0.8 dl pancake dough.

    Return True if you have enough dough to make a pancake, False otherwise.

    :param dough_amount:
    :param dough: pancake dough given in dl
    :return: boolean whether you have enough dough to make a pancake or not
    """
    if dough_amount >= 0.8:
        return True
    else:
        return False


def make_a_pancake(dough_amount: float) -> float:
    """
    Make a pancake. Making one pancake takes 0.8 dl dough.

    Round the remaining dough up to two decimal places.

    You do not have to implement the actual pancake making,
    you just have to return the amount of dough left after (hypothetically) making a pancake.

    :param dough_amount:
    :param dough: pancake dough given in dl
    :return: dough in dl after making a pancake
    """
    dough_amount -= 0.8
    a = round(dough_amount, 2)
    return a


if __name__ == '__main__':
    ingredients = ["egg"] + ["milk"] * 5 + ["flour"] * 4 + ["butter"] + ["sugar"]
    print(make_dough(ingredients))  # 0 -> not enough sugar.
    ingredients2 = ["egg"] * 4 + ["milk"] * 9 + ["flour"] * 14 + ["butter"] * 3 + ["sugar"] * 7
    print(make_dough(ingredients2))  # 7 -> can make 7dl dough not 7.x dl.
    ingredients3 = ["egg" for _ in range(3)] + ["milk"] + ["flour" for _ in range(7)] + ["butter" for _ in range(3)] + ["sugar" for _ in range(2)]
    print(make_n_pancakes(8, ingredients3))  # 8
    ingredients4 = ["egg" for _ in range(21)] + ["milk" for _ in range(45)] + ["flour" for _ in range(4)] + ["butter" for _ in range(14)] + ["sugar" for _ in range(12)]
    print(make_n_pancakes(4, ingredients4))  # 4 -> 7dl dough, 0.8dl per pancake -> could make 8 pancakes, we want 4
