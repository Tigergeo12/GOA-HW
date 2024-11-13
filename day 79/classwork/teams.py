import random
def create_teams(students, num_teams):
   
    random.shuffle(students)
    
    teams = [[] for _ in range(num_teams)]
    
   
    for i, student in enumerate(students):
        teams[i % num_teams].append(student)
    
    return teams #daxmareba gamoviyene randomistvis

