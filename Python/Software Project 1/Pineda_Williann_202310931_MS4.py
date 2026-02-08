N, B = map(int, input().split()) #reads the first line of input, splits it based on the space, converts it to int, and assigns N to number of contractors and B to number of projects

everything = [] #creates an empty list that will hold all contractor info (names, bids, wins, total winnings)
for a in range(N): #starts a loop that will iterate N times, once each contractor
    entry = input().split(',') #reads the second line of the input (contractor-bid pair) and splits it into a list of stringd at each comma
    name = entry[0] #assigns the contractor name the variable name
    bids = list(map(int, entry[1:])) #every subsequent parts from second part onwards will be converted to int, listed, and assigned to the variable bids
    everything.append({ #creates a dictionary that will store the contractor's info and adds it to the everything dict
        'name': name, #contractor name
        'bids': bids, #contractor bid (one per project)
        'wins': 0, #initializes wins to 0
        'total': 0 #initializes total winnings to 0
    }) #end command

for project in range(B): #starts a loop that repeats B times, once for each project
    minimum_wins = min(b['wins'] for b in everything) #creates a variable named minimum_wins that determines the minimum number of wins for all contractors in everything
    allowed_to_join = [b for b in everything if b['wins'] == minimum_wins] #creates a list named allowed_to_join whose members have wins == minimum_wins 
    winner = allowed_to_join[0] #initializes winner as the first on the list allowed_to_join
    lowest_bid = allowed_to_join[0]['bids'][project] #initializes lowest_bid by taking the bid of the previous winner for the current project as initial value
    for b in allowed_to_join: #starts a loop that will iterate in allowed_to_join
        bid = b['bids'][project] #takes the contractor's bid for the current project
        if bid < lowest_bid or (bid == lowest_bid and b['name'] < winner['name']): #if current bid is lower than lowest_bid, current contractor wins; if not, tie breaker: if current bid == lowest bid, name first alphabetically wins
            winner = b #if the if statement above is true, current contractor is new winner
            lowest_bid = bid #their bid is new lowest_bid
    winner['wins'] += 1 #adds one to the wins counter of the winning contractor
    winner['total'] += lowest_bid #adds the lowest_bid of winning contractor to total winnings 

for b in everything: #creates a loop that iterares through all contractor dictionaries in everything dict
    print(f"{b['name']},{b['total']}") #prints each contractor name, followed by their total cost they won