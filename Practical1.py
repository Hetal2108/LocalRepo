def get_lib_data():
    lib_data = {}
    print("Enter number of Books: ")
    num_books = int(input())
    print("Enter number of members:")
    num_memb = int(input())

    for i in range(num_books):
        print(f"\nEnter title of book {i+1}:")
        title = input()
        lib_data[title] = []

        print(f"Enter borrow count for each of the {num_memb} members for '{title}':")
        for j in range(num_memb):
            print(f"Member {j+1}: ", end="")
            count = int(input())
            lib_data[title].append(count)
    return lib_data


#1. Compute the Average number of book borrowed by all library members.
def comp_avg(lib_data):
    total_borrowed = 0
    total_entries = 0
    for book in lib_data:
        for count in lib_data[book]:
            total_borrowed += count
            total_entries += 1
    avg = total_borrowed / total_entries
    return avg


#2. Calculate the Book with Highest and Lowest Borrowing.
def find_high_low_borw_bks(lib_data):
    highest = None
    lowest = None
    highest_book = ''
    lowest_book = ''

    for book in lib_data:
        total = 0
        for count in lib_data[book]:
            total += count

        if highest is None or total > highest:
            highest = total
            highest_book = book

        if lowest is None or total < lowest:
            lowest = total
            lowest_book = book

    return highest_book, lowest_book


#3. Count members with 0 borrowing
def cnt_memb_bor(lib_data):
    num_members = len(next(iter(lib_data.values())))
    member_cnt = 0

    for i in range(num_members):
        total_borrowed = 0
        for book in lib_data:
            total_borrowed += lib_data[book][i]

        if total_borrowed == 0:
            member_cnt += 1

    return member_cnt


#4. Display most Frequently borrowed count (mode)
def mfbc(lib_data):
    freq_map = {}

    for book in lib_data:
        for count in lib_data[book]:
            if count in freq_map:
                freq_map[count] += 1
            else:
                freq_map[count] = 1

    max_freq = 0
    max_count = None

    for count in freq_map:
        if freq_map[count] > max_freq:
            max_freq = freq_map[count]
            max_count = count

    return max_count


# Main Program
print("Library Borrowing Records System")
lib_data = get_lib_data()

print("\nLibrary Statistics:")

avg = comp_avg(lib_data)
print("1. Average number of books borrowed by all members:", avg)

highest_book, lowest_book = find_high_low_borw_bks(lib_data)
print("2. Book with Highest Borrowings:", highest_book)
print("   Book with Lowest Borrowing:", lowest_book)

zero_borrowers = cnt_memb_bor(lib_data)
print("3. Number of members who borrowed 0 books:", zero_borrowers)

most_freq = mfbc(lib_data)
print("4. Most Frequently occurring borrow count:", most_freq)
