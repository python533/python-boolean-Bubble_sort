list=[5,4,2,1,3,2,4,1,3,5]



def kabarcık_sıralama(arr):
    for i in list:
        if i[0] == list[1]:
            orta=len(arr)//2
            top=arr[:orta]
            down=arr[orta:]
            kabarcık_sıralama(top)
            kabarcık_sıralama(down)
            a=b=c=0

            while a <len(top) and len(down):
                if top[a] <= down[b]:
                    arr[c]: down[a]
                    a += 1
                else:
                    arr[down] = top[b]
                    a+=1
                    b+=1

            while a < len(down) and b < len(top):
                arr[a] = arr[b]
                a += 1
                b += 1


def printlist(arr):
    for i in range(len(arr)):
        print(arr[i],end="")
        print()


if __name__ == '__main__':
    arr_list = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    printlist(arr_list)
    kabarcık_sıralama(arr_list)
    print("\nSorted array is ")
    printlist(arr_list)

