class NoDuplicates:
    def __init__(self,list):
        self.list_without_duplicate = list

    def __call__(self, new_items):
        [self.list_without_duplicate.append(x) for x in new_items if x not in self.list_without_duplicate]

my_no_dup_list = NoDuplicates([])

my_no_dup_list(['dupa', 'dom', 'grabie','dupa'])
print(my_no_dup_list.list_without_duplicate)

my_no_dup_list(['keyboard','mouse'])
print(my_no_dup_list.list_without_duplicate)

my_no_dup_list(['keyboard','mouse','pendrive'])
print(my_no_dup_list.list_without_duplicate)

my_no_dup_list(['charger','pendrive'])
print(my_no_dup_list.list_without_duplicate)


my_no_dup_list2 = NoDuplicates(['keyboard','mouse'])
print(my_no_dup_list2.list_without_duplicate)
