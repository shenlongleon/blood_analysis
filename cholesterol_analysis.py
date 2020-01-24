def Cholesterol_analysis():
    print("Cholesterol_analysis")
    HDLinput = input("Enter test result: ")
    test_info = HDLinput.split("-")
    if test_info[0] == "HDL":
        HDL_analysis()



def interface():
    choice = 0
    while choice != "9":
        print("Cholesterol Analysis")
        print("Options: ")
        print("  1 - Cholesterol Analysis")
        print("  9 - Quit")
        choice = input("Enter your options: ")
        if choice == "9":
            return
        elif choice == "1":
            Cholesterol_analysis()

if __name__ == "__main__":
    interface()
