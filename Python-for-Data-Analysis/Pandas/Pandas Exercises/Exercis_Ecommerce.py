import pandas as pd

df=pd.read_csv('EcommercePurchases.csv')

head=df.head()
#print(head)

#df.info()

average_purchase=df['Purchase Price'].mean()
print(average_purchase)

lowest=df['Purchase Price'].min()
highest=df['Purchase Price'].max()

print(highest)
print(lowest)


en_sum=df[df['Language']=='en']
print(en_sum)