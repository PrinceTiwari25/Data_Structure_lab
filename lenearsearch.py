def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = []
print("Enter 10 Numbers:")
for _ in range(10):
    arr.append(int(input()))

x = int(input("Enter a Number to Search: "))
index = linear_search(arr, x)

if index != -1:
    print("Found at Index No.", index)
else:
    print("Number not found")

print("\n----- LETTER 1 -----")
print("Dear Sir,\n")
print("Greetings of the day!!\n")
print('On behalf of Computer Society of India (CSI) at KRMU, we wish to propose an event "AI based Cinematography contest" on 019/09/2023 from 10:30 am onwards in C Block Lab 13.\n')
print("Objective of the Event:")
print("• The main aim for conducting this event is to help students to explore AI that will be used to generate unique storylines, characters, and visual effects.")
print("Outcomes of Event:")
print("• It provides a platform for collaboration between filmmakers and AI experts.\n")
print("NAAC Metric: 2.3.1 and 3.3.1\n")
print("CSI club collects the membership fees from the students where some percentage of the amount is kept as a treasure in KRMU accounts so that this amount can be used for conducting CSI events for students.")
print("We request approval of Rs 3000 for event execution:")
print("First Prize -- Rs 1500")
print("Second Prize -- Rs 800")
print("Third Prize -- Rs 700\n")
print("Thanks & Regards,\nDr Swati & Dr Meenu\nCSI Coordinators")

print("\n----- LETTER 2 -----")
print("Dear Sir,\n")
print("Greetings!!!\n")
print("I wish to inform that proposed event Code Cracker Contest is under the club Computer Society of India.")
print("CSI club collects the membership fees from the students where some percentage of the amount is kept as a treasure in KRMU accounts.")
print("The event and its budget of Rs 5000 is approved in the SOET event calendar for the academic year 2022-2023.\n")
print("We require approval of Rs 5000 for event execution:")
print("First Prize -- Rs 3000")
print("Second Prize -- Rs 2000")
print("Third Prize -- Rs 1000\n")
print("Please provide us the approval of Rs 5000 for the conduction of the Event from CSI funds.")
