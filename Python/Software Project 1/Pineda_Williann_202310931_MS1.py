N = int(input()) #count the number of contractors

bids = {} # a dictionary to store all contractors bidding

for blank in range(N): #read each contractor entry, will loop for N times
    entry = input() #reads the next line of entry and stores it in entry
    contractor_name, bid = entry.split(',') #splits the entry: before the comma - stored in contractor_name, after comma - stored in bid
    bids[contractor_name] = int(bid) #adds a new entry to the dictionary, converts bid to int

minimum_bid = min(bids.values()) #find minimum of bids

cheapest_bids = [contractor_name for contractor_name, i in bids.items() if i == minimum_bid] #find all contractors who bids minimum_bid by checking if is equal to minimum_bid

granted_contractor = min(cheapest_bids) #pick the smallest-valued starting letter of contractor name, for ties

print(granted_contractor) #print the lowest bid AND the smallest-valued contractor first name