print("Analysing stock price for $AMC in January 2023 using day parametre.")

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(i):
  return stock_prices[i-1] #Subtract 1 because indexing start at 0, this will allow the code to give an inclusive price

def max_price(a,b):
  mx = price_at(a) #Initialise using first price variable in the range
  for i in range(a, b + 1): # Loop through given range days, inclusive of price
    mx = max(mx, price_at(i)) #Compares the price found against the intial stock price
  return mx

def min_price(a,b):
  mn = price_at(a)
  for i in range(a, b + 1):
    mn = min(mn, price_at(i)) #Compares the price found against the intial stock price
  return mn

print(price_at(4))
print(max_price(4,5))
print(min_price(6,10))