def permutations(n):
    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def get_permutations(n):
        list_of_permutations = []
        i = 1
        while i <= n:
            list_of_permutations.append(i)
            i += 1

        list_of_directions = [-1] * n  
        final_list = [list_of_permutations.copy()]  

        while True:
            mobile = -1
            mobile_index = -1

            for i in range(n):
                #if pointing left and is mobile
                if list_of_directions[i] == -1 and i > 0 and list_of_permutations[i] > list_of_permutations[i - 1] and list_of_permutations[i] > mobile:
                    mobile = list_of_permutations[i]
                    mobile_index = i

                #if pointing right and is mobile      
                elif list_of_directions[i] == 1 and i < n - 1 and list_of_permutations[i] > list_of_permutations[i + 1] and list_of_permutations[i] > mobile:
                    mobile = list_of_permutations[i]
                    mobile_index = i

            #if no mobile number exists
            if mobile == -1:
                break  

            swap_index = mobile_index + list_of_directions[mobile_index]
            swap(list_of_permutations, mobile_index, swap_index)
            swap(list_of_directions, mobile_index, swap_index)

            #a number greater than the current mobile number gets its direction pointing switched
            for i in range(n):
                if list_of_permutations[i] > mobile:
                    list_of_directions[i] = -list_of_directions[i]

            final_list.append(list_of_permutations.copy())

        return final_list
    return get_permutations(n)
