import json


def count_workers(dict_org, chief_pos, found_chief, counter, position):
    if found_chief == 0 and chief_pos in dict_org['name']:

        counter = count_workers(dict_org, chief_pos, 1, counter, position)
    else:
        for x in dict_org['subordinates']:
            if found_chief == 0:
                if chief_pos in x['name']:
                    counter = count_workers(x, chief_pos, 1, counter, position)
            else:
                if 'subordinates' in x:
                    counter = count_workers(x, chief_pos, found_chief, counter, position)
                else:
                    if position != '':
                        if position in x['name']:
                            counter += 1
                    else:
                        counter += 1
    return counter


def department_counter(dict_org, counter):
    for x in dict_org['subordinates']:
        if 'subordinates' in x:
            counter = department_counter(x, counter)
        else:
            counter += 1
            print(f"{x['name'].split()[0]} Department ")
            return counter
    return counter


j = open('companies.json')
j = j.read()
dict_ = json.loads(j)
i = 1
for d in dict_:
    print(f'Company {i}\nThe number of the workers is {count_workers(dict_[d], "CEO", 0, 0, "")}')
    print(f'The number of the workers under CTO is {count_workers(dict_[d], "CTO", 0, 0, "")}')
    print(
        f'The number of the people with “developer” in their title is {count_workers(dict_[d], "CEO", 0, 0, "Developer")}')
    print('The names of the departments:')
    print(f'The number of the departments is {department_counter(dict_[d], 0)}\n')
    i += 1
