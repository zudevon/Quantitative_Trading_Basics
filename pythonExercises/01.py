"""
•	Write a script that loops through numbers 1 to 100 and checks odd or even parity.
Please print out the word ‘odd’ or ‘even’ next to the number.  The number should be
printed with a right alignment.  The script should however skip numbers in the 50 range
and only print out results for 1 to 49 and 60 to 100.

"""

for x in range(1, 101):

    # to clear out the 11 numbers that have 5 as ten digit
    if x in range(50, 60):
    # if x > 49 or x < 59:
        continue

    if x % 2 == 0:
        print(x, "is Even")
    else:
        print(x, "is Odd")


