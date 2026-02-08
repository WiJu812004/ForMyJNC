N, B = map(int, input().split()) #reads the first line of input, splits it based on the space, converts it to int, and assigns N to number of contractors and B to number of projects

everything = []  #creates a dict that will store everything (all dictionaries), hence the name

for blank in range(N): #creates a loop that will iterate N times, once for each contractor
    entry = input() #reads the second line of input (contractor names and bids), assigns it as entry
    parts = entry.split(',') #splits entry into a list of str at the comma; first part is contractor name, next parts are bids
    company_name = parts[0] #assigns first part to company_name
    bids = [int(x) for x in parts[1:]] #all elements from the second part onwards (all of these are bids) converted to int, stored to bids as list for all B projects
    everything.append({'name': company_name, 'bids': bids, 'total': 0}) #creates a new dictionary for the contractor analyzed — their names, list of bids, and total winnings (initialized to 0) — and added to everything

previous_winner = None #initializes the disqualification tracker to none

for project in range(B): #starts another loop that will repeat B times, project is an integer index that represents the current bid list evaluated
    current_winner = None #creates a new variable current_winner and initializes it to null
    minimum_bid = 100000 #makes a new variable that will store the min bid, initializes it to a very high amount so that every bid will be minimum
    for a in everything: #stars another loop that will go through every contractor in the everything dict
        if a['name'] == previous_winner: #checks if the current contractor being anaylzed is the same as the previous winner
            continue #if yes, skips them and goes to the next contractor (disqualified)
        b = a['bids'][project] #gets the bid for the contractor being analyzed 
        if b < minimum_bid or (b == minimum_bid and a['name'] < current_winner['name']): #checks if current bid is lower than min_bid, OR in case of a tie, if the name has a smaller value than the current_winner
            current_winner = a #if the above condition is true, the contractor analyzed will be the new current_winner
            minimum_bid = b #the new min bid is stored
    if current_winner: #checks if a winner was selected for the project
        current_winner['total'] += minimum_bid #min_bid addrd to total winnings 
        previous_winner = current_winner['name'] #current_winner name added to previous_winner, and this name will be one that will be disqualified in the next project

for a in everything: #last loop of this code, iterates through the whole everything dict
    print(f"{a['name']},{a['total']}") #prints the name, their total winnings