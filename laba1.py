def selection_sort(arr): 
    n = len(arr)     
    comparisons = 0     
    assignments = 0 
 
    
    for i in range(n - 1): 
               
        min_index = i 
        assignments += 1  
 
            
        for j in range(i + 1, n): 
            comparisons += 1               
            if arr[j] < arr[min_index]: 
                min_index = j 
                assignments += 1   
 
                
        if min_index != i:              
            arr[i], arr[min_index] = arr[min_index], arr[i]             
            assignments += 3     

    return arr, comparisons, assignments 


my_list = [50, 80, 19, 86, 35, 7, 60, 48, 51 ]
sorted_list, comps, assigs = selection_sort(my_list.copy())    

print("Оригінальний список:", my_list) 
print("Відсортований список:", sorted_list) 
print(f"Кількість порівнянь: {comps}") 
print(f"Кількість присвоєнь: {assigs}") 
