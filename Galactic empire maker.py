import random


class alien_delegation:
    def __init__(self, name, materials, num_sugg):
        self.name = name
        self.needed_materials = materials
        self.num_sugg = num_sugg


def negotiation(alien_list, materials):
    num_convinced_aliens=0
    for alien in alien_list:
        num_my_sugg = 1
        print(f"The current alien delegation is : {alien.name}")
        suggestion = random.choice(materials)
        print(f'My suggestion material number {num_my_sugg} is : {suggestion} ')
        while num_my_sugg <= alien.num_sugg and suggestion not in alien.needed_materials:
            print(f'It did not work,I will try another suggestion')
            suggestion = random.choice(materials)
            num_my_sugg += 1
            print(f'My suggestion number {num_my_sugg} is : {suggestion} ')
        if num_my_sugg>alien.num_sugg:
            print(f'I failed to convince {alien.name},I will try with next alien delegation ')
        else:
            num_convinced_aliens+=1
            print(f'I convinced {alien.name}!,I will continue with next alien delegation')
        print(f'Until now I convinced {(num_convinced_aliens/len(alien_list))*100}% of  alien groups\n')
    if (num_convinced_aliens/len(alien_list))*100 >=70:
        print(f'I succeeded to convince {(num_convinced_aliens/len(alien_list))*100}% of total alien groups')
    else:
        print(f'I failed to convince 70% of total alien groups')


### why use ___name__?
if __name__ == '__main__':
    ### this is ok for placeholder, when submitting final project try to make it realistic
    materials = ['A', 'B', 'C', 'D', 'S', 'Y', 'Z', 'E', 'P', 'O', 'M', 'X', 'T', 'R', 'V', 'H', 'W', 'Q', 'U', 'K']
    ### GREAT! dynamicly created. 10 points!
    alien_delegation_list = []
    for i in range(4):
        mat_list = []
        for _ in range(3):
            tmp = random.choice(materials)
            while tmp in mat_list:
                tmp = random.choice(materials)
            mat_list.append(tmp)
        alien_delegation_list.append(alien_delegation('Delegation' + str(i + 1), mat_list, random.randint(3, 7)))

    negotiation(alien_delegation_list,materials)
