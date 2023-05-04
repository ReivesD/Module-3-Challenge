import csv

csvpath = "budget_data.csv"

total_months = 0
total_profit_loss = 0
profit_losses = []
previous_profit_loss = None
greatest_increase = {"date": None, "amount": 0}
greatest_decrease = {"date": None, "amount": 0}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) 
    for row in csvreader:
       
        date = row[0]
        profit_loss = int(row[1])
        
        total_months += 1
        total_profit_loss += profit_loss
        
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            profit_losses.append(change)
                        
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            elif change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change
        
        
        previous_profit_loss = profit_loss


average_change = sum(profit_losses) / len(profit_losses)


total_months_str = str(total_months)
total_profit_loss_str = "${:,.0f}".format(total_profit_loss)
average_change_str = "${:,.2f}".format(average_change)
greatest_increase_str = "${:,.0f} ({})".format(greatest_increase["amount"], greatest_increase["date"])
greatest_decrease_str = "${:,.0f} ({})".format(greatest_decrease["amount"], greatest_decrease["date"])


print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months_str}")
print(f"Total: {total_profit_loss_str}")
print(f"Average Change: {average_change_str}")
print(f"Greatest Increase in Profits: {greatest_increase_str}")
print(f"Greatest Decrease in Profits: {greatest_decrease_str}")


with open("financial_analysis.txt", "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("-----------------------------\n")
    outfile.write(f"Total Months: {total_months_str}\n")
    outfile.write(f"Total: {total_profit_loss_str}\n")
    outfile.write(f"Average Change: {average_change_str}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase_str}\n")
    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease_str}\n")
