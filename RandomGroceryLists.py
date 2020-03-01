import pandas as pd
from random import randint
from random import uniform
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

GroceryProducts = pd.read_csv("product.csv")
# GroceryProducts = GroceryProducts.drop(['PRODUCT_ID'], axis = 1)
GroceryProducts = GroceryProducts.assign(price = [round(uniform(1, 100), 2) for i in range(0, len(GroceryProducts))])
# print(GroceryProducts.columns)
Subset = GroceryProducts[['CURR_SIZE_OF_PRODUCT', 'price']]


# GroceryProducts = GroceryProducts.values.tolist()

Subset = Subset.values.tolist()

GroceryLists = [[[],0.0] for i in range(0,1000)]
for i in range(0,1000):
    for j in range(0, randint(1,20)):
        a = randint(0, len(Subset)-1)
        GroceryLists[i][0].append(Subset[a])



for i in range(0,len(GroceryLists)):
    for j in range(0,len(GroceryLists[i][0])):
            GroceryLists[i][1] += GroceryLists[i][0][j][-1]
            GroceryLists[i][0][j][0] = str(GroceryLists[i][0][j][0])
# associations = apriori([item[0] for item in GroceryLists],min_support = 0.2, min_confidence = 0.1)
FirstDf = [item[0] for item in GroceryLists]
AllLists = []
for i in range(0, len(FirstDf)):
    for j in range(0, len(FirstDf[i])):
        AllLists.append(FirstDf[i][j][0])
te = TransactionEncoder()
te_ary = te.fit(AllLists).transform(AllLists)
# print(te_ary)
# df = pd.DataFrame(AllLists, columns=te.columns_)
# apriori(te_ary, min_support = 0.6)

# print(df)
# results = apriori(DF, min_support=0.6)
# results1 = results.values.tolist
# print(results)

