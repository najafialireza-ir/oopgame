def diamond(rows):
    if rows % 2 == 0:
        rows 
    
    for i in range(1, rows + 1, 2):
        print(" " * ((rows - i) // 2) + "*" * i)
        
    for i in range(rows - 2, 0, -2):
        print(" " * ((rows - i) // 2) + "*" * i)


rows = int(input("Enter number of rows: "))
diamond(rows) 

