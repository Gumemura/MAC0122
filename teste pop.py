def main():
    a = [0,1,2,3,4,5,6,0,0,0,0,0]
    
    for i in range (1,len(a) + 1):
        if a[-1] == 0:
            a.pop(-1)
        else:
            break

    print(a)

main()