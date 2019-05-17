if __name__ =="__main__": 
    for i in range(1, 1+12):
        for j in range(1, 1+12):
            if(j%3==0):
                if(i%6==0):
                    print(j)
                    print(i)
                else:
                    print("Nel")
