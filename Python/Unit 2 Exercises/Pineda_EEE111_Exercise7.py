import csv

input_file = "input_data.csv"
output_file = "result.csv"

number_rows = []
with open(input_file, newline = "") as f:
    for row in csv.reader(f):
        nums = [int(x) for x in row if x]
        if nums: 
            nums.append(sum(nums))
            number_rows.append(nums)
column_averages = [sum(r[a] for r in number_rows) // len(number_rows) for a in range(len(number_rows[0]))]
number_rows.append(column_averages)
with open(output_file, "w", newline="") as f:
    csv.writer(f).writerows(number_rows)

print("Result file saved as result.csv")