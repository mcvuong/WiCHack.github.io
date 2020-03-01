import pandas as pd
from random import randint
from random import uniform
GroceryProducts = pd.read_csv("product.csv")
GroceryProducts = GroceryProducts.drop(['PRODUCT_ID'], axis = 1)
GroceryProducts = GroceryProducts.assign(price = [round(uniform(1, 100), 2) for i in range(0, len(GroceryProducts))])
GroceryProducts = GroceryProducts.values.tolist()
# print(GroceryProducts)
GroceryLists = [[randint(121, 4000),[],0.0] for i in range(0,1000)]
for i in range(0,1000):
    for j in range(0, randint(1,20)):
        a = randint(0, len(GroceryProducts)-1)
        for k in range(0, randint(0,5)):
            GroceryLists[i][1].append(GroceryProducts[a])

# for i in range(0, len(GroceryLists)):
#     for j in range(0, len(GroceryLists[i])):
#         for k in range(0, len(GroceryLists[i][j])):
#             GroceryLists[i][1] += GroceryLists[i][j][k][6]


for i in range(0,len(GroceryLists)):
    for j in range(0,len(GroceryLists[i][1])):
            GroceryLists[i][2] += GroceryLists[i][1][j][6]
            
print(GroceryLists[0][0][2])

