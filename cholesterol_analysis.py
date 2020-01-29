
def LDL_analysis(LDL_level):
    if LDL_level >=190:
        return "Very high"
    elif 160 <= LDL_level < 190:
        return "High"
    elif 130 <= LDL_level < 159:
        return "Borderline High"
    else:
        return "Normal"



def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return "Normal"
    elif 40 <= HDL_level < 60:
        return "Borderline low"
    else:
        return "Low"




def Cholesterol_analysis():
    print("Cholesterol_analysis")
    HDLinput = input("Enter HDL test result: ")
    test_info = HDLinput.split(" = ")
    LDLinput = input("Enter LDL test result: ")
    test_info_ = LDLinput.split(" = ")
    if test_info[0] == "HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("The HDL level is {}.".format(answer))
        answer_ = LDL_analysis(int(test_info_[1]))
        print("The LDL level is {}.".format(answer_))
        
def name_function():
    return



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
