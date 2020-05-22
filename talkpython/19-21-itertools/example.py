from itertools import cycle, permutations, combinations
from random import sample



if __name__ == "__main__":
    traffic_lights = ['RED', 'GREEN', 'AMBER']
    #for light in cycle(traffic_lights):
    #    print(light)


    def friends_teams( names, team_size = 2, order_does_matter = False):

        when_order_does_not_matter = sample(list(permutations(names, team_size)), 10)
        when_order_does_matter =  sample(list(combinations(names, team_size)), 10)

        if order_does_matter:
            for team in when_order_does_matter:
                print(team)

        else:
            
            for team in when_order_does_not_matter:
                print(team)
                
    NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


    friends_teams(NAMES, True)


    

    
    
