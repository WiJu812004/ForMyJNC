contractor_bids = input().split() #reads the first line of input, and then separates them into N and B
N = int(contractor_bids[0]) #number of contractors
B = int(contractor_bids[1]) #number of bids

biddings = {} #place everything in dict

for a in range(N): #reads each contractor and their bids
    entry = input() #reads the next line of input and adds it in entry
    company_and_bids = entry.split(',') #split the entry into a list: i.e. "Contractor0", "876", "727", "788", "880", "968", "817", "730", "632", "912"
    name = company_and_bids[0] #takes the first item in entry and designates it as name
    bid_list = [] #creates an empty list for the bids
    for b in range(1, len(company_and_bids)): #creates a loop that starts with the first bid (1) and loops through all bids
        bid_list.append(int(company_and_bids[b])) #converts each bid to int from str, adds it to bid_list
    biddings[name] = bid_list #stores bid_list in the biddings dict created earlier

total = {} #create another list for total bids

for name in biddings: #creates a loop that goes through each contractor
    total[name] = 0 #every contractor starts with 0
for project in range(B): #goes through over each project: 0 - first bid column, 1 - second bid column, ...
    minimum_bid = 100000 #initialize min_bid with a big number so that any bid be smaller
    for name in biddings: #loop through all contractor
        if biddings[name][project] < minimum_bid: #compares each bid of each contractor with min_bid
            minimum_bid = biddings[name][project] #if a bid is smaller, it will replace min_bid value; after loop, min_bid = smallest bid
    lowest_bidders = [] #creates another list
    for name in biddings: #loops AGAIN to all contractors
        if biddings[name][project] == minimum_bid: #determines if a contractor has a bid that is equal to min_bid
            lowest_bidders.append(name) #adds that contractor to the list lowest_bidders
    lowest_bidders.sort() #sorts the list alphabetically in case of a tie
    winning_contractor = lowest_bidders[0] #selects the first on the list which is the smallest-valued name
    total[winning_contractor] = total[winning_contractor] + minimum_bid #adds the bid aount to the contractor's total

for name in biddings: #loops through all contractors as to how it's written in the input
    print(name + "," + str(total[name])) #prints each contractor's name and their total separated by a comma