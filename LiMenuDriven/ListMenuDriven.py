li = []
print("\n***************************Welcome***************************\n")

while True:
    print("Please choose your choice from list given below\n")
    print("=>Enter 1 to create an array")
    print("=>Enter 2 to read an array")
    print("=>Enter 3 to update an array")
    print("=>Enter 4 to delete an array")        
    print("=>Enter 0 to Exit an array")        

    choice=int(input("\nEnter your choice to perform an action : "))

    match choice:

        case 1:
            print("\nYou chose to create an array!\n")
            num = int(input("Enter The Number of values you want to add in array : "))

            for i in range(num):
                a = int(input(f"Enter the element no {i+1} : "))
                li.append(a)

            print("\nArray Created Successfully\n")

        case 2:
            print("\nYou chose to read an array!\n")
            for i in li:
                print(i,end=" ")
                print()


        case 3:
            idx = int(input("Enter the index to remove the element : "))
            if idx>=0 and idx<len(li):
                li.pop(idx)
                print("\nElement removed!\n")
            else:
                print("\nInvalid index\n")

      
        case 4:
            idx = int(input("Enter the index to removeqwa the element : "))
            val = int(input("Enter the new value : "))

            if idx>=0 and idx<len(li):
                li[idx] = val
                print("\nElememt Updated !")
            else:
                print("\nInvalid Index\n")
                      
        
        case 0:
            print("\nThank you so much !")
            break