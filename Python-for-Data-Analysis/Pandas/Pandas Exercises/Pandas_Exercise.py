import pandas as pd

sal=pd.read_csv("Salaries.csv")

head=sal.head()
print(head)

#number of entries
print(sal.info())

#BasePay Average

average=sal['BasePay'].mean()
print("Average Basepay time pay:",format(average))
#High Overtime pay

highestOvertime=sal['OvertimePay'].max()

print("Highest Over time pay:",format(highestOvertime))

#Job Title of JOSEPH DRISCOLL

JobTitle=sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']
print(JobTitle)

#How much he makes include totalPayBenefits

TotalPay=sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']
print(TotalPay)

#Highest paid employ

hightpaid=sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]
print('Highest paid employee',format(hightpaid))

lowestpaid=sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]
print('Lowest paid employee',format(lowestpaid))

average_per_year=sal.groupby('Year')['BasePay']
print(average_per_year)

uniqueJob=sal['JobTitle'].nunique()
print(uniqueJob)

topJobs=sal['JobTitle'].value_counts().head(5)
print(topJobs)

sum_job=sum(sal[sal['Year']==2013['JobTitle'].value_count()==1])
print(format(sum_job))