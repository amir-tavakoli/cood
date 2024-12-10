# Prompt the user for a file name

try:
    # Open the file
    with open("C:\\Users\\amir\\Desktop\\mboxshort.txt", 'r') as file:
        total = 0 
        count = 0 

     
        for line in file:
           
            if line.startswith("X-DSPAM-Confidence:"):
            
                value = float(line.strip().split(":")[1])
                
                total += value
                count += 1
       
        if count > 0:
            average = total / count
            print("Average spam confidence:", average)
        else:
            print("No matching lines found.")

except FileNotFoundError:
    print("File not found. Please check the file name and try again.")