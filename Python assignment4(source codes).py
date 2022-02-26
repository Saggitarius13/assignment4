# Name -- Prem Shankar  SID -- 21104084

# Q1..

def tower_of_hanoi(n, sourceTower, destinationTower, intermediateTower):
    if n == 0:
        return
    tower_of_hanoi(n - 1, sourceTower, intermediateTower, destinationTower)   # disk1<disk2<disk3(size-wise)
    print(f"Move disk{n} from {sourceTower} to {destinationTower}")
    tower_of_hanoi(n - 1, intermediateTower, destinationTower, sourceTower)

print("Steps to solve the problem of tower of hanoi:\n")
tower_of_hanoi(3, 'A', 'C', 'B')


# Q2..

row = int(input("Enter number of rows: "))

space = 36

# empty list containg all 0s
a = [0] * 20

print("\n\t\t\t\t*** PASCAL TRIANGLE ***\n")
for i in range(row):

    for spi in range(1, space + 1):
        print(" ", end="")  

    a[i] = 1

    for j in range(i + 1):
        print('%6d' % (a[j]), end="")

    for j in range(i, 0, -1):
        a[j] = a[j] + a[j - 1]

    space = space - 3

    print()

# Q3.


dividend = int(input("Enter the dividend number\n"))
divisor = int(input("Enter the divisor number\n"))

k = divmod(dividend,divisor)

print(f"The quotient and the remainder are {k}")

#a.
print("[True = callable, False == not callable]", end = "")
print(f"\tThe status whether function callable or not:{callable(k)}") # for checking whether the function is callable or not.
print()
#b.
if dividend!=0 and divisor!=0:
    print("All the entered values as dividend and divisor are non-zero")
elif divisor==0:
    print("Please enter a valid divisor")
else:
    print("All the entered values as dividend and divisor are not non-zero")
#c.
tuple2 = (4,4)
tuple3 = (5,5)
tuple4 = (6,6)


combine_tuple1 = zip(k,tuple2)
mapping1 = map(sum,combine_tuple1)
sum1 = list(mapping1)
combine_tuple2 = zip(k,tuple3)
mapping2 = map(sum,combine_tuple2)
sum2 = list(mapping2)
combine_tuple3 = zip(k,tuple4)
mapping3 = map(sum,combine_tuple3)
sum3 = list(mapping3)
new = sum1+sum2+sum3  # created a combine list of all the elements after performing addition of each element of k with the tuple (4,5,6)

def filterout(number):
    if number>4:
        return True
    
    return False


filtering_numbers = filter(filterout,new)
#print(filtering_numbers)

new_tuple = list(filtering_numbers)
print(f"The number(s) greater than 4 is/are {tuple(new_tuple)}")

#d.
setdatatype = set(new_tuple)
print("After converting it into set datatype it become")
print(setdatatype)

#f.
maximumvalue = max(setdatatype)
print(f"The maximum value in this  set is\n{maximumvalue}")
N = hash(13)
print(f"The hash value of N is {N}")

#e.
immutable_set = frozenset(setdatatype)

print(f"Now the immutable_set has become immutable after the use of 'frozenset' function")


# Q4.

class Student:
    def __init__(self,name,rollnumber):
        self.name = name
        self.rollnumber = rollnumber

    def details(self):
        print(f"The name of the student is {self.name} and the roll number of the student is {self.rollnumber}")

    def __del__(self):
        print("Destructor called, Student deleted")



detail1 = Student("Prem",145876)
detail1.details()
del detail1


# Q5.

#a.
class employees:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def details1(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")



employee_details1=employees("Mehak",40000)
employee_details1.details1()

employee_details2=employees("Ashok",50000)
employee_details2.details1()

employee_details3=employees("Viren",60000)
employee_details3.details1()

#b.

print("\nAfter updating the salary of Mehak")
employee_details1.salary = 70000
employee_details1.details1()

employee_details2=employees("Ashok",50000)
employee_details2.details1()

employee_details3=employees("Viren",60000)
employee_details3.details1()

#c.
print("\n")


employee_details1=employees("Mehak",40000)
employee_details1.details1()

employee_details2=employees("Ashok",50000)
employee_details2.details1()

employee_details3=employees("Viren",60000)
print("After deleting the details of the viren")
del(employee_details3)
employee_details3.details1()



# Q6.
word_by_george = input("Enter your word\n")
list1 = list(word_by_george)
def anagrams(s):
    if s == "":
        return [s]

    else:
        ans = []

        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans

b = anagrams(word_by_george)
possible_words = list(b)   # created all the anagrams of the word entered by george and verified if the meaningful word entered by barbie is in the anagram or not.

word_by_barbie = input(f"Enter a word using the letters {list1}\n")
if word_by_barbie in possible_words:
    print("Your friendship is not fake")
else:
    print("Your friendship is fake")




