# Problem:
# You have a list of students sorted as integers, and you need to sort them smallest to smallest using an insertion sort algorithm.


def insertion_sort(grades):
    for i in range(1, len(grades)):  
        key = grades[i]  
        j = i - 1  
        
        # Move values ​​larger than key to the front
        while j >= 0 and grades[j] > key:
            grades[j + 1] = grades[j]
            j -= 1
        
        grades[j + 1] = key  # Put the key in the right place

# random grades list
grades = [85, 72, 90, 65, 78, 88, 95, 70]
insertion_sort(grades)
print("After Sorting", grades)

# جمال عبدالناصر رضوان 
# setion 3