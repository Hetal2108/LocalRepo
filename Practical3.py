# Selection Sort
def selct_sort(sal):
    for i in range(len(sal)):
        min_idx = i
        for j in range(i + 1, len(sal)):
            if sal[j] < sal[min_idx]:
                min_idx = j
        sal[i], sal[min_idx] = sal[min_idx], sal[i]
    return sal

# Bubble Sort
def bubble_sort(sal):
    n = len(sal)
    for i in range(n):
        for j in range(n - i - 1):
            if sal[j] > sal[j + 1]:
                sal[j], sal[j + 1] = sal[j + 1], sal[j]
    return sal

# Manual list copy
def manual_copy(orign):
    new_list = []
    for item in orign:
        new_list.append(item)
    return new_list

# Main program
sal = []

n = int(input("Enter number of employees: "))
print("Enter the salaries:")

for i in range(n):
    salary = float(input(f"Salary {i + 1}: "))
    sal.append(salary)

# Manual copy of the list
sal_for_selection = manual_copy(sal)
sal_for_bubble = manual_copy(sal)

# Sort
selection_sorted = selct_sort(sal_for_selection)
bubble_sorted = bubble_sort(sal_for_bubble)

# Top 5 highest (last 5 elements reversed)
top5_selection = []
top5_bubble = []

# Selection sort top 5
i = len(selection_sorted) - 1
count = 0
while i >= 0 and count < 5:
    top5_selection.append(selection_sorted[i])
    i -= 1
    count += 1

# Bubble sort top 5
i = len(bubble_sorted) - 1
count = 0
while i >= 0 and count < 5:
    top5_bubble.append(bubble_sorted[i])
    i -= 1
    count += 1

# Output
print("\nTop 5 Highest Salaries using Selection Sort:")
for s in top5_selection:
    print(s)

print("\nTop 5 Highest Salaries using Bubble Sort:")
for s in top5_bubble:
    print(s)
