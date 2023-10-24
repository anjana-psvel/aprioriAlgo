# 
file_path = "categories.txt.txt"  
with open(file_path, 'r') as file:
    with open(file_path, 'r') as file:
     dataset = file.read()
    # print(dataset)

Data = dataset.split("\n")

s1=[]
for i in range(len(Data)):
   s1.append(Data[i].split(";"))
for j in range(3):
   print(s1[j])

items = dataset.split("\n")
s1=[]
for i in range(len(items)):
   s1.append(items[i].split(";"))
n=len(s1)
s2=[]
for i in range(n):
   s2=s2+s1[i]
s3=s2
unique= list(set(s2))

C1={}
for item in unique:
    frequency = s3.count(item)
    C1.update({item:frequency})
print(C1)

def write_to_file(file_name, data):
    try:
        with open(file_name, "w") as file:
            for item in data:
                file.write(str(item) + ":" + str(s3.count(item)) + "\n")
        print(f"Data has been written to {file_name}")
    except IOError:
        print(f"An error occurred while writing to {file_name}")

data_to_write = C1
write_to_file("patterns_1.txt", data_to_write)


def generate_candidates(Lk_minus_1, K):
    """
    Generate candidate itemsets Ck from frequent itemsets L(k-1).
    Lk_minus_1: List of frequent (k-1)-itemsets
    k: Size of the candidate itemsets to generate (k)
    Returns: List of candidate itemsets Ck
    """
    Ck = []

    # Combine each pair of (k-1)-itemsets from L(k-1)
    for i in range(len(Lk_minus_1)):
        for j in range(i + 1, len(Lk_minus_1)):
            itemset1, itemset2 = list(Lk_minus_1[i]), list(Lk_minus_1[j])
            itemset1.sort()
            itemset2.sort()

            # Merge the two itemsets if their first (k-2) elements are the same
            if itemset1[:K - 2] == itemset2[:K - 2]:
                new_itemset = tuple(set(itemset1 + [itemset2[-1]]))
                Ck.append(new_itemset)
    
    unique_list = []
    [unique_list.append(x) for x in Ck if x not in unique_list and (len(x)== K+1)]
    # print(unique_list)

    return unique_list

def prune_candidate_itemsets(Ck, min_support, transactions):
    """
    Prune candidate itemsets Ck by removing those that do not meet the minimum support threshold.
    Ck: List of candidate itemsets.
    min_support: Minimum support threshold.
    transactions: List of transactions in the database.
    Returns: List of frequent itemsets Lk.
    """
    
    Lk = []
    itemset_counts = {}

    # Count the occurrences of candidate itemsets in the transactions
    for transaction in transactions:
        for candidate in Ck:
            if set(candidate).issubset(transaction):
                itemset_counts[candidate] = itemset_counts.get(candidate, 0) + 1

    # Check if candidate itemsets meet the minimum support threshold
    for candidate, count in itemset_counts.items():
        support = count / len(transactions)
        if support >= min_support:
            Lk.append(candidate)

    return Lk

L1=[]
for i in C1:
    if (C1[i]) >= 771:
        L1.append({i: C1[i]})
print(L1)
print(f"Patterns_1: {len(L1)}")

data_to_write = L1
write_to_file("patterns_1.txt", data_to_write)

C=[C1];
L=[L1];

i=0
while  L[i] != [] and C[i] != []:
    C.append(generate_candidates(L[i],i+1))
    L.append(prune_candidate_itemsets(C[i+1], 0.01, s1))
    i+=1
print(C[-1])
print(L[-1])

data_to_writez = C[-1]
write_to_file("patterns_all.txt", data_to_writez)
