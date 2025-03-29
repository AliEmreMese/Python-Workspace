def seqSearchordered( alist, item ):
    i = 0
    while i < len(alist):
        if alist[i] == item:
            return True # direct return technique
        if alist[i] > item:
            return False
        i += 1
    return False

sorted_list = [1, 3, 5, 7, 9, 11]
target = 5

result = seqSearchordered(sorted_list, target)

if result:
    print(f"Hedef değer {target} listede bulundu.")
else:
    print(f"Hedef değer {target} listede bulunamadı.")