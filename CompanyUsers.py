companies = {}

command = input().split(" -> ")

while command[0] != "End":
    company,id = command
    if company in companies.keys():
        companies[company] = []
    if id not in companies[company]:
        companies[company].append(id)
    command = input().split(" -> ")

for company,emps in companies.items():
    print(company)
    for emp in emps:
        print(f"-- {emp}")
