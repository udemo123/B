import itertools

def calculate_support(itemsets, transactions):
    support_counts = []
    for itemset in itemsets:
        count = sum(1 for transaction in transactions if all(item in transaction for item in itemset))
        support_counts.append(float(count) / len(transactions))
    return support_counts

support_threshold = float(input("Enter the minimum support: "))
items = ['i1', 'i2', 'i3', 'i4', 'i5']
num_transactions = int(input("Enter number of transactions: "))

transactions = []
for i in range(num_transactions):
    transaction = input(f"Enter the items bought in transaction {i + 1}, separated by a comma: ").split(',')
    transactions.append([item.strip() for item in transaction])

print("\nTransactions are as follows:")
for transaction in transactions:
    print(transaction)

print("\nThe candidate set C1 is:", items)

support_c1 = calculate_support([(item,) for item in items], transactions)
for i, item in enumerate(items):
    print(f"Support for {item} is: {support_c1[i]}")

l1 = [items[i] for i in range(len(items)) if support_c1[i] >= support_threshold]
print("\nL1 is:", l1)


c2 = list(itertools.combinations(items, 2))
print("\nCandidate set C2 is:", c2)

support_c2 = calculate_support(c2, transactions)
for i, itemset in enumerate(c2):
    print(f"Support for {itemset} is: {support_c2[i]}")


l2 = [c2[i] for i in range(len(c2)) if support_c2[i] >= support_threshold]
print("\nL2 is:", l2)


c3 = list(itertools.combinations(items, 3))
support_c3 = calculate_support(c3, transactions)
for i, itemset in enumerate(c3):
    print(f"Support for {itemset} is: {support_c3[i]}")

l3 = [c3[i] for i in range(len(c3)) if support_c3[i] >= support_threshold]
print("\nL3 is:", l3)

confidence = []
for itemset in l3:
    base_item = itemset[0]  
    count_base = sum(1 for transaction in transactions if base_item in transaction)
    count_both = sum(1 for transaction in transactions if all(item in transaction for item in itemset))
    conf = count_both / count_base if count_base > 0 else 0
    confidence.append(conf)

for i, itemset in enumerate(l3):
    print(f"Confidence for {itemset} is: {confidence[i]}")
