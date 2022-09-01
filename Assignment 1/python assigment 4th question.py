it_companies = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon' }
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#length of it_companies
print("Length of it_companies is :",len(it_companies))

#adding Twitter to it_companies
it_companies.add("Twitter")
print(it_companies)

#inserting multiple it companies
new_it_companies={"TCS","INFOSYS","Wipro"}
it_companies.update(new_it_companies)
print("after adding new companies\n",it_companies)

#removing one of the companies
it_companies.remove("Facebook")
print("after removing a company  \n",it_companies)

## remove() method will raise an error if the specified item does not exist, and the discard() method will not raise an error if the specified item does not match

#join of A and B
A_B = A.union(B)
print("\nJoining A and B ",A_B)

#intersection of A and B
A_intersection_B = A.intersection(B)
print("\nIntersection of A and B ",A_intersection_B)

#is A subset of B
print("\nA is subset of B :", A.issubset(B))

#is A disjoint set of B
print("\n A is disjoin set of B:",A.isdisjoint(B))

#join A with B
print("\n Joining A with B :",A.union(B))

#join B with A
print("\n Joining B with A :",B.union(A))

#symetric difference between two sets
print("\nSymetric difference between A and B :",A.symmetric_difference(B))

#clearing elements from A and B
A.clear()
B.clear()
print(A)
print(B)

#converting age to set
set_age = set(age)
print("\n ages = ",set_age)
print("Length of  list age = ",len(age))
print("Length of set_age = ",len(set_age))