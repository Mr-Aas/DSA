# # Let us say your expense for every month are listed below,
# # January - 2200
# # February - 2350
# # March - 2600
# # April - 2130
# # May - 2190

# # Create a list to store these monthly expenses and using that find out,
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


expense = [["january",2200],["febuary",2350],["march",2600],["april",2130],["may",2000]]

def compareExpense(monthA , monthB):
    if (monthA in expense) & (monthB in expense):
        if monthA[1] >= monthB[1]:
            return f"{monthA[0]} have {monthA[1]-monthB[1]} more spend than {monthB[0]}."
        else:
            return f"{monthA[0]} have {monthB[1]-monthA[1]} less spend than {monthB[0]}."
    else:
        return "no such month exist in expense data"
def quaterExpense():
    return f"{expense[0][1]+expense[1][1]+expense[2][1]}"

def spentMonth(value):
    for data in expense:
        # print(data)
        if data[1]==value:
            return f"In {data[0]} you have spent {value}"
    else:
        return f"no such month pass when you spent {value}"

def insertExpense(month,amount):
    expense.append([month,amount])
    return f"On {month} inserted amount {amount} "

def returnItem(month, itemAmount):
    for item in expense:
        if item[0] == month:
            oldexpense  = item[1]
            item[1]-= itemAmount
            return f"{month} expense get reduced from {oldexpense} to {item[1]}"
    else:
        return f"no such month exist in record"

print("Ans1.",compareExpense(expense[0],expense[1]))
print("Ans2.",quaterExpense())
print("Ans3.",spentMonth(2000))
print("Ans4.",insertExpense("june",1980))
print("Ans5.",returnItem("april",200))
# print("Ans1.",compareExpense(expense[0],expense[1]))