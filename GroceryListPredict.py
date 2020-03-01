import pandas as pd
from random import randint
from random import uniform
# from mlxtend.preprocessing import TransactionEncoder
# from mlxtend.frequent_patterns import apriori
from apyori import apriori
GroceryProducts = pd.read_csv("product.csv")
# print(GroceryProducts.columns)
GroceryProducts = GroceryProducts.assign(price = [round(uniform(1, 100), 2) for i in range(0, len(GroceryProducts))])
a = GroceryProducts[['COMMODITY_DESC', 'price']]
Subset = a.values.tolist()

GroceryLists = [[[],0.0] for i in range(0,1000000)]
for i in range(0,1000):
    for j in range(0, randint(1,20)):
        a = randint(0, len(Subset)-1)
        GroceryLists[i][0].append(Subset[a])
for i in range(0,len(GroceryLists)):
    for j in range(0,len(GroceryLists[i][0])):
            GroceryLists[i][1] += GroceryLists[i][0][j][-1]
            GroceryLists[i][0][j][0] = str(GroceryLists[i][0][j][0])
FirstDf = [item[0] for item in GroceryLists]
AllLists = [[] for i in range(len(FirstDf))]
for i in range(0, len(FirstDf)):
    for j in range(0, len(FirstDf[i])):
        AllLists[i].append((FirstDf[i][j][0]))
# te = TransactionEncoder()
# te_ary = te.fit(AllLists).transform(AllLists)
# df = pd.DataFrame(te_ary, columns=te.columns_)a
association = apriori(AllLists, min_support = 0.0053, min_confidence = 0.20, min_lift = 3, min_length = 2 )
association = list(association)
# print(len(association))
# print(type(association[0]))
# Predictions = apriori(df, min_support=0.6, use_colnames=True)
# print(Predictions)
Suggestions = []
print(list(association[0][0]))                      #Predict things to buy