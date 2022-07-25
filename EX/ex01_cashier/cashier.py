"""Cashier power."""
sum = int(input("Enter a sum: "))
coin = 0
"""
while sum >= 50:
    coin += 1
    sum -= 50
while sum >= 20:
    coin += 1
    sum -= 20
while sum >= 10:
    coin += 1
    sum -= 10
while sum >= 5:
    coin += 1
    sum -= 5
while sum >= 1:
    coin += 1
    sum -= 1 """
temporary = sum - (sum % 50)
coin += (temporary / 50)
sum = (sum - temporary)
temporary = sum - (sum % 20)
coin += (temporary / 20)
sum = (sum - temporary)
temporary = sum - (sum % 10)
coin += (temporary / 10)
sum = (sum - temporary)
temporary = sum - (sum % 5)
coin += (temporary / 5)
sum = (sum - temporary)
coin += sum
results = int(coin)
print("Amount of coins needed: " + str(results))
