# name = "Aryan"
# age = 22
# experience = 0.5
# is_employed = False

# print(name)
# print(age)
# print(experience)
# print(is_employed)

# # getting data types
# print(type(name))
# print(type(age))
# print(type(experience))
# print(type(is_employed))

# numbers = [10, 20, "swift, kotlin", "false", False, "0.3", 0.3]
# numbers.append(False)
# print(numbers)
# print(type(numbers))
# print(len(numbers))
# print(numbers[-1])
# numbers.remove(numbers[-1])
# numbers.pop(-1)
# del numbers[-1]
# print(numbers)


# # dictionary
# person = {
#     "name": "Aryan",
#     "age": 0.3
# }

# print(person)
# print(type(person))
# print(person["age"])

# person["age"] = True
# print(person)


# opportunity = {
#     "id": 1,
#     "company": "Google",
#     "role": "iOS developer Intern",
#     "status": "Applied",
#     "date": "2026-11-14"
# }
# print("\n", opportunity, "\n")

# opportunities = [
#     {
#         "id": 1,
#         "company": "Google",
#         "role": "iOS developer Intern",
#         "status": "Applied",
#         "date": "2026-11-14"
#     }, 
#     {
#         "id": 2,
#         "company": "Apple",
#         "role": "iOS developer Senior",
#         "status": "Applied",
#         "date": "2026-11-13"
#     },
#     {
#         "id": 1,
#         "company": "Google",
#         "role": "iOS developer Intern",
#         "status": "Applied",
#         "date": "2026-11-14"
#     },
#     {
#         "id": 2,
#         "company": "Apple",
#         "role": "iOS developer Senior",
#         "status": "Applied",
#         "date": "2026-11-13"
#     },
#     {
#         "id": 1,
#         "company": "Google",
#         "role": "iOS developer Intern",
#         "status": "Applied",
#         "date": "2026-11-14"
#     }
# ]

# import pprint
# use pprint.pprint to print each item in next line, 
# use print(*variableName, sep = "\n") to print each item in collection in next line, where sep stands for separator and * unpacks each element of collection and passes them as separate arguments.

# print(*opportunities, sep = "\n")


# Conditions
# status = "Applied"
# if status == "Applied":
#     print("Application Submitted")
# elif status == "Interview":
#     print("You have an Interview")
# else:
#     print("no matching status")

# opportunities = ["Google", "Microsoft", "Amazon", "Telegram"]
# for company in opportunities: 
#     print(company)

# iterating through dict by 'for key, value in dictName.items(): print(key, ":", value)'

# while loop 'while condition: task...'

# taking input in python 'value = input("Enter the value")'

# function in python can be written by using 'def funcName(paramenters optional): task...' calling 'functionName(arguments if any)'
# python can auto detect return type so you can directly us return without mentioning any return type 'def funcName(paras): return value'
# default parameters in python 'def funcName(para = defValue): task...'


opportunities: dict[int, dict[str, str]] = { 
    13: {
        "company": "Google",
        "role": "iOS Developer",
        "status": "Applied"
    },
    54: {
        "company": "Microsoft",
        "role": "Backend Intern",
        "status": "Interview"
    }, 
    23: {
        "company": "Amazon",
        "role": "Python Intern",
        "status": "Rejected"
    }
}



oppIds: set[int] = {13, 54, 23}
min, max = 1, 100

import random 
def add_opportunity(company: str, role: str, status: str):
    availableIDs: set[int] = set(range(min, max + 1)) - set(oppIds)
    newOppId: int = random.choice(list(availableIDs))
    oppIds.add(newOppId)
    newOpp = {
        "company": company.title(),
        "role": role.title(),
        "status": status.title()
    }
    opportunities[newOppId] = newOpp
    print("Updated opportunities...\n")
    show_opportunities()



def del_opportunity(id: int):
    try:
        opportunities.pop(id)
        oppIds.remove(id)
        print("Updated opportunities...\n")
        show_opportunities()
    except KeyError as error:
        print("Id/Opportunity not found in the database, Error: ", error)
    return



def show_opportunities():
    print("< All opportunities available...>")
    if not opportunities:
        print("No opportunity available")
        return
    for key, value in opportunities.items():
        print(f"id: {key}: {value}")
    return



def filter_by_status(status: str):
    filterResultCount = 0
    for opportunity in opportunities.values():
        if opportunity["status"].lower() == status.lower():
            print(f"Company: {opportunity['company']}\nRole: {opportunity['role']}\nStatus: {opportunity['status']}")
            filterResultCount += 1

    if filterResultCount == 0:
        print("No such opportunity available")
    return



from collections import Counter

def count_by_status():
    oppCount: dict[str, int] = {}
    # for opportunity in opportunities:
    #     status = opportunity["status"]
    #     oppCount[status] = oppCount.get(status, 0) + 1
    if not opportunities:
        print("No opportunity available")
        return
    oppCount = Counter(opp["status"] for opp in opportunities.values())
    print(oppCount)
    return


    
def search_by_company(company: str):
    compMatch: list[dict[str, str]] = []

    for opportunity in opportunities.values():
        if opportunity["company"].lower() == company.lower():
            compMatch.append(opportunity)

    if not compMatch:
        print("No such opportunity available")
        return

    print(compMatch)
    return




def menu(option: str) -> bool: 
    match option.strip().lower(): 
        case "1" | "show":
            print("\n")
            show_opportunities()

        case "2" | "add": 
            print("\n")
            company = input("Enter company name: ")
            role = input("Enter the role: ")
            status = input("Enter the status: ")
            print("\n")
            add_opportunity(company, role, status)

        case "3" | "delete":
            try:
                print("\n")
                show_opportunities()
                print("\n")
                id: int = int(input("Enter id to delete an opportunity: "))
                print("\n")
                del_opportunity(id)
            except ValueError as error:
                print("\n")
                print("Wrong Input!, Error: ", error)

        case "4" | "filter":
            print("\n")
            status = input("Enter status to filter by: ")
            print("\n")
            filter_by_status(status)

        case "5" | "count": 
            print("\n")
            count_by_status()
        case "6" | "search":
            print("\n")
            company = input("Enter company to filter by: ")
            print("\n")
            search_by_company(company)
        case "7" | "exit":
            print("\n")
            print("Exitted the menu!")
            return False
        case _: 
            print("\n")
            print("Invalid input!")
            print("Returning to main menu...")
    return True


def main():
    while True:
        print("\nMENU:")
        print("1 - Show all opportunities")
        print("2 - Add a new opportunity")
        print("3 - Delete an opportunity")
        print("4 - Filter by status")
        print("5 - Count by status")
        print("6 - Search by company")
        print("7 - Exit")
        print("\n")

        # try:
        #     age = int(input("Enter your age: "))
        #     print(age)
        # except ValueError as error:
        #     print(error)

        choice = input("Enter your choice(No or Name): ")
        print("\n")
        print("\n")
        print("___Output___")
        state: bool = menu(choice)
        print("\n")
        print("____________")
        print("\n")
        print("\n")
        if not state:
            break
            

main()

# from collections import Counter(oppCount = Counter(opp["status"] for opp in opportunities)

        





