#All Modules
from statistics import mean,median

import math
import statistics
import json


#All Variables



#All Functions
#List Functions
def create_list():
    List_init = []
    number_ele_List = int(input("Please enter number elements to be available in list:"))  
    for element in range(number_ele_List):
        element_n = int(input("please enter the element: "))
        List_init.append(element_n)
    return List_init


def append_list(List):
    element_to_be_inserted = int(input("Please enter the element to be inserted: "))
    List.append(element_to_be_inserted)
    return List

def pop_list(List):
    #Two different types of pop operations
    element_to_be_poped = int(input("Please enter the position of the element to be pop:"))
    List.pop(element_to_be_poped)
    return List
    
def len_list(List):
    return len(List)

def sum_list(List):
    return sum(List)

def max_list(List):
    return max(List)

def min_list(List):
    return min(List)

def sort_list(List):
    return sorted(List)

def mean_list(List):
    return mean(List)

def median_list(List):
    return median(List)

def count_list(List):
    freq_ele_num = int(input("Enter the element to find its frequency:"))
    return List.count(freq_ele_num)

def insert_list(List):
    insert_position = int(input("Enter the position where element is to be added:"))
    insert_element = int(input("Enter the element you want to add:"))
    List.insert(insert_position,insert_element)
    return List

def concate_list(List):
    List_new = []
    number_ele_NList = int(input("Please enter number elements to be available in new list:"))  
    for element in range(number_ele_NList):
        element_n = int(input("please enter the element: "))
        List_new.append(element_n)
        List.extend(List_new)
    return List

def reverse_list(List):
    List.reverse()
    return List

def slice_list(List):
    starting_point = int(input("Enter your starting point of list:"))
    ending_point = int(input("Enter end point:"))
    return List[starting_point:ending_point]
    #return List

def clear_list(List):
    List.clear()
    return List
def copy_list(List):
    New_List = List.copy()
    return New_List
#Set Functions
def create_set():
    Set_init = set()
    number_ele_Set = int(input("Please enter number elements to be available in Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_init.add(element_n)
    return Set_init

def add_set(Set):
    element_to_be_inserted = int(input("Please enter the element to be inserted: "))
    Set.add(element_to_be_inserted)
    return Set
def update_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
        Set.update(Set_new)
    return Set
def union_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
    return Set.union(Set_new)
    #return Set

def intersection_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
    return Set.intersection(Set_new)
    #return Set

def difference_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
    return Set.difference(Set_new)
    #return Set

def Symmetric_difference_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
    return Set.symmetric_difference(Set_new)
    #return Set

def pop_set(Set):
    #Two different types of pop operations
    #element_to_be_poped = int(input("Please enter the position of the element to be pop:"))
    Set.pop()
    return Set
def sum_set(Set):
    return sum(Set)
def max_set(Set):
    return max(Set)
def min_set(Set):
    return min(Set)
def len_set(Set):
    #return len(Set)
    length = len(Set)
    return length
def intersection_update_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
        Set.intersection_update(Set_new)
    return Set

def difference_update_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
        Set.difference_update(Set_new)
    return Set
def symmetric_difference_update_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
        Set.symmetric_difference_update(Set_new)
    return Set
def clear_set(Set):
    Set.clear()
    return Set

def discard_set(Set):
    discard_element = int(input("Enter the element to be removed:"))
    Set.discard(discard_element)
    return Set

def disjoint_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
        output = Set.isdisjoint(Set_new)
    return output
def subset_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
        output = Set.issubset(Set_new)
    return output
#Dictionary functions
def create_dict():
    Dict_init = dict()
    number_ele_Dict = int(input("Please enter number elements to be available in Dictionary:"))  
    for element in range(number_ele_Dict):
        key_n = input("please enter the Key: ")
        val_n = input("Please enter values to the Keys:")
        Dict_init[key_n] = val_n
        #Set_init.add(element_n)
    return Dict_init

def update_dict(Dict):
    key_val = input("Please enter key value:")
    val = input("Please enter value to key:")
    Dict.update({key_val:val})
    return Dict

def access_dict(Dict):
    key_val = input("Please enter key to access value:")
    display_value = Dict.get(key_val)
    return display_value
    #return Dict

def items_dict(Dict):
    display_items = Dict.items()
    return display_items
    #return Dict
def keys_dict(Dict):
    display_keys = Dict.keys()
    return display_keys
    #return Dict
def copy_dict(Dict):
    copy_Dict = Dict.copy()
    return copy_Dict
def pop_dict(Dict):
    key_val = input("Please enter key value to Pop:")
    pop_val = Dict.pop(key_val)
    return Dict
def popItem_dict(Dict):
    popItem = Dict.popitem()
    return Dict
def clear_dict(Dict):
    Dict.clear()
    return Dict
def len_dict(Dict):
    return len(Dict)
#Tuple Functions
def create_tuple():
    tuple_init = ()
    Li_Tup = list(tuple_init)
    number_ele_Tuple = int(input("Please enter number elements to be available in Tuple:"))  
    for element in range(number_ele_Tuple):
        key_n = input("please enter the elements to your Tuple: ")
        Li_Tup.append(key_n)
        tuple_init = tuple(Li_Tup)
    return tuple_init

def count_tuple(Tuple):
    count_element = input("Enter the Element to find out its frequency:")
    Count = Tuple.count(count_element)
    return Count

def index_tuple(Tuple):
    count_element = input("Enter the Element to find out its Index of First Occurance:")
    Index = Tuple.index(count_element)
    return Index

def concate_tuple(Tuple):
    Tuple_new = ()
    List_new = list(Tuple_new)
    number_ele_NTuple = int(input("Please enter number elements to be available in new Tuple:"))  
    for element in range(number_ele_NTuple):
        element_n = input("please enter the element: ")
        List_new.append(element_n)
        Tuple_new = tuple(List_new)
        T = Tuple + Tuple_new
    return T

def len_tuple(Tuple):
    return len(Tuple)
def del_tuple(Tuple):
    del Tuple
    #return Tuple
'''
def update_tuple(Tuple):
    tuple_new = ()
    Li_tuple_new = list(tuple_new)
    number_ele_Tuple = int(input("Please enter number elements to be available in Tuple:"))  
    for element in range(number_ele_Tuple):
        key_n = input("please enter the elements to your Tuple: ")
        Li_tuple_new.append(key_n)
        tuple_new = tuple(Li_tuple_new)
    return Tuple
'''
print("Welcome to Data structure calculator")

print("Please select any operation to proceed \n1.List \n2.Set \n3.Dictionary \n4.Tuple ")

data_input = int(input("please enter a number between 1 and 4: "))

if data_input == 1:
                 print("Welcome to List operations ")
                 print("Create a List for proceeding List Operations")
                 List_main = create_list()
                 print("The created list is ", List_main)
                 print("Please select any one List operation to proceed (Any number between 1-16)")
                 print(" 1. Append \n 2. Pop \n 3. Len \n 4. Sum \n 5. Max \n 6. Min \n 7. Sort \n 8. Mean \n 9. Median \n 10. Frequency \n 11. Insert \n 12. Concatenation \n 13. Reverse \n 14. Slicing \n 15. Clear \n 16. Copy" )

                 List_operation_input = int(input("Please enter any one number:"))

                 if List_operation_input == 1:
                                        output_append = append_list(List_main)
                                        print("The output after append operations is ", output_append)
                 elif List_operation_input == 2:
                                         output_len = pop_list(List_main)
                                         print("The output after pop operations is ", output_len)

                 elif List_operation_input == 3:
                                        output_len = len_list(List_main)
                                        print("The output after len operations is ", output_len)

                 elif List_operation_input == 4:
                                         output_len = sum_list(List_main)
                                         print("The output after Sum operations is ", output_len)
                 elif List_operation_input == 5:
                                         output_len = max_list(List_main)
                                         print("The output after Max operations is ", output_len)
                 elif List_operation_input == 6:
                                         output_len = min_list(List_main)
                                         print("The output after Min operations is ", output_len)
                 elif List_operation_input == 7:
                                         output_len = sort_list(List_main)
                                         print("The output after Sort operations is ", output_len)
                 elif List_operation_input == 8:
                                         output_len = mean_list(List_main)
                                         print("The output after Mean operations is ", output_len)
                 elif List_operation_input == 9:
                                         output_len = median_list(List_main)
                                         print("The output after Median operations is ", output_len)
                 elif List_operation_input == 10:
                                         output_len = count_list(List_main)
                                         print("The output after Count operations is ", output_len)
                 elif List_operation_input == 11:
                                         output_len = insert_list(List_main)
                                         print("The output after Insert operations is ", output_len)
                 elif List_operation_input == 12:
                                         output_len = concate_list(List_main)
                                         print("The output after Concate operations is ", output_len)
                 elif List_operation_input == 13:
                                         output_len = reverse_list(List_main)
                                         print("The output after Reverse operations is ", output_len)
                 elif List_operation_input == 14:
                                         output_len = slice_list(List_main)
                                         print("The output after Slice operations is ", output_len)
                 elif List_operation_input == 15:
                                         output_len = clear_list(List_main)
                                         print("The output after Clear operations is ", output_len)
                 elif List_operation_input == 16:
                                         output_copy = copy_list(List_main)
                                         print("The output after Copy operations is ", output_copy)

elif data_input == 2:
                print("Welcome to Set Operations")
                print("Create a Set for proceeding Set Operations")
                Set_main = create_set()
                print("The created Set is ", Set_main)
                print("Please select any one Set operation to proceed (Any number between 1-19)")
                print("1. Add \n 2. Update \n 3. Union \n 4. Intersection \n 5. Difference \n 6. Symmetric Difference \n 7. Pop \n 8. Sum \n 9. Max \n 10. Min \n 11. Len \n 12. Intersection Update \n 13. Difference Update \n 14. Symmetric Difference Update \n 15. Clear \n 16. Discard \n 17. Disjoint \n 18. SubSet" )
             
                Set_operation_input = int(input("Please enter any one number:"))

                if Set_operation_input == 1:
                                        output_add = add_set(Set_main)
                                        print("The output after add operations is ", output_add) 
                if Set_operation_input == 2:
                                        output_update = update_set(Set_main)
                                        print("The output after update operations is ", output_update) 
    
                if Set_operation_input == 3:
                                        output_union = union_set(Set_main)
                                        print("The output after Union operations is ", output_union)
                if Set_operation_input == 4:
                                        output_intersection = intersection_set(Set_main)
                                        print("The output after Intersection operations is ", output_intersection)
                if Set_operation_input == 5:
                                        output_difference = difference_set(Set_main)
                                        print("The output after Difference operations is ", output_difference)
                if Set_operation_input == 6:
                                        output_Symdifference = Symmetric_difference_set(Set_main)
                                        print("The output after Symmetric Difference operations is ", output_Symdifference)

                if Set_operation_input == 7:
                                        output_pop = pop_set(Set_main)
                                        print("The output after Pop operations is ", output_pop)
                if Set_operation_input == 8:
                                        output_sum = sum_set(Set_main)
                                        print("The output after Sum operations is ", output_sum)
                if Set_operation_input == 9:
                                        output_max = max_set(Set_main)
                                        print("The output after Max operations is ", output_max)
                if Set_operation_input == 10:
                                        output_min = min_set(Set_main)
                                        print("The output after Min operations is ", output_min)
                if Set_operation_input == 11:
                                        output_len = len_set(Set_main)
                                        print("The output after Len operations is ", output_len)
                if Set_operation_input == 12:
                                        output_intersection_update = intersection_update_set(Set_main)
                                        print("The output after Intersection Update operations is ", output_intersection_update)
                if Set_operation_input == 13:
                                        output_difference_update = difference_update_set(Set_main)
                                        print("The output after Difference Update operations is ", output_difference_update)
                if Set_operation_input == 14:
                                        output_symmetric_difference_update = symmetric_difference_update_set(Set_main)
                                        print("The output after Symmetric Difference Update operations is ", output_symmetric_difference_update)
                if Set_operation_input == 15:
                                        output_clear = clear_set(Set_main)
                                        print("The output after Clear operations is ", output_clear)
                if Set_operation_input == 16:
                                        output_discard = discard_set(Set_main)
                                        print("The output after Discard operations is ", output_discard)
                if Set_operation_input == 17:
                                        output_disjoint = disjoint_set(Set_main)
                                        print("The output after Disjoint operations is ", output_disjoint)
                if Set_operation_input == 18:
                                        output_subset = subset_set(Set_main)
                                        print("The output after Subset operations is ", output_subset)

elif data_input == 3:
                print("Welcome to Dictionary Operations")
                print("Create a Dictionary for proceeding Dictionary Operations")
                Dict_main = create_dict()
                print("The created Dictionary is ", Dict_main)
                print("Please select any one Dictionary operation to proceed (Any number between 1-8)")
                print(" 1. Insert or Update \n 2. Access \n 3. Get Items \n 4. Get Keys \n 5. Copy Dictionary \n 6. Pop \n 7. Pop Item \n 8. Clear \n 9. Len" )
             
                Dict_operation_input = int(input("Please enter any one number:"))

                if Dict_operation_input == 1:
                                        output_update = update_dict(Dict_main)
                                        print("The output after Update operations is ", output_update)
                if Dict_operation_input == 2:
                                        output_access = access_dict(Dict_main)
                                        print("The output after Access operations is ", output_access)
                if Dict_operation_input == 3:
                                        output_items = items_dict(Dict_main)
                                        print("The output after Get Items operations is ", output_items)
                if Dict_operation_input == 4:
                                        output_keys = keys_dict(Dict_main)
                                        print("The output after Get Keys operations is ", output_keys)
                if Dict_operation_input == 5:
                                        output_copy = copy_dict(Dict_main)
                                        print("The output after Copy operations is ", output_copy)
                if Dict_operation_input == 6:
                                        output_pop = pop_dict(Dict_main)
                                        print("The output after Pop operations is ", output_pop)
                if Dict_operation_input == 7:
                                        output_popItem = popItem_dict(Dict_main)
                                        print("The output after Pop Item operations is ", output_popItem)
                if Dict_operation_input == 8:
                                        output_clear = clear_dict(Dict_main)
                                        print("The output after Clear operations is ", output_clear)
                if Dict_operation_input == 9:
                                        output_len = len_dict(Dict_main)
                                        print("The output after Len operations is ", output_len)

elif data_input == 4:
                print("Welcome to Tuple Operations")
                print("Create a Tuple for proceeding Tuple Operations")
                Tuple_main = create_tuple()
                print("The created Tuple is ", Tuple_main)
                print("Please select any one Tuple operation to proceed (Any number between 1-5)")
                print(" 1. Count \n 2. Get Index \n 3. Concatenation \n 4. Len \n 5. Del  " )
                Tuple_operation_input = int(input("Please enter any one number:"))

                
                if Tuple_operation_input == 1:
                                        output_count = count_tuple(Tuple_main)
                                        print("The output after Count operations is ", output_count)
                if Tuple_operation_input == 2:
                                        output_index = index_tuple(Tuple_main)
                                        print("The output after Index operations is ", output_index)
                if Tuple_operation_input == 3:
                                        output_concate = concate_tuple(Tuple_main)
                                        print("The output after Concatenation operations is ", output_concate)
                if Tuple_operation_input == 4:
                                        output_len = len_tuple(Tuple_main)
                                        print("The output after Len operations is ", output_len)
                if Tuple_operation_input == 5:
                                        output_del = del_tuple(Tuple_main)
                                        print("The output after Del operations is ", output_del)
