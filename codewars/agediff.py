#Find the Difference in Age between Oldest and Youngest Family Members

def difference_in_ages(ages):
    smallest = min(ages)
    biggest = max(ages)
    return (smallest,biggest,biggest-smallest)