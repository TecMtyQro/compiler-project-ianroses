if __name__ =="__main__": 
    print("What's your name?")
    name = input()    
    print("Your Name is:")
    print(name)
    year = 1997
    if(year>=2001):
        print('21st century')
    elif(year>=1901):
        print('20th century')
    for month in range(1, 1+12):
        print(month)
        if(month<5):
            print("hola")
        else:
            print("no se puede")
    while(year<2016):
        year += 1
