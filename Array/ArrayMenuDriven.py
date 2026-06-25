print("Welcome To Array Operations Hub")

while True:

    print("\nSelect an option : \n")
    print("1.Create an Array ")
    print("2.Find the Largest element ")
    print("3.Find the Smallest element ")
    print("4.Find the Odd and Even Elements ")
    print("5.Reverse the Array ")
    print("6.Check if the element Exist or not")
    print("7.Count frequency of any given element")
    print("8. Sum of all element")
    print("9.Exit")

    choice = int(input("\nEnter your choice : "))

    match choice:

        case 1:
            n=int(input("\nEnter How many Values you want to store in Array : "))
            arr = []

            for i in range(n):
                arr.append(int(input()))

            print("\nYour Array is ",arr)

        case 2:
            largest = max(arr)

            print("\nThe Largest Element is : ",largest)

        case 3:
            smallest = min(arr)

            print("\nThe Smallest Element is : ",smallest)
        
        case 4:
            for num in arr:
                if num % 2 == 0:
                    print(num, "is Even")

                else:
                    print(num, "is Odd")

        case 5:
            reversed_array = arr[::-1]

            print("\nReversed Array is : ",reversed_array)

        case 6:
            find=int(input("\nEnter the element to search : "))
            
            if find in arr:
                print("\nElement exists..!")

            else:
                print("\nElement Does not exist..!")
            
        case 7:
            num = int(input("\nEnter element to count: "))

            frequency = arr.count(num)

            print("\nFrequency of", num , "is", frequency)

        case 8:
            total = 0
            for x in arr:
                total += x

            print("Sum of all elements is : ",total)

        case 9:
            print("\nThank you for Visiting us , Goodbye !")
            break

        case _:
            print("\nInvalid Choice! Please enter a number between 1 and 6.")
    



