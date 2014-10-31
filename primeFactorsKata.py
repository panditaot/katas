def primeFactors(number):
    lista=[]
    while number != 1:
        for x in range(2, int(number+1)):
            if number%x==0:
                lista.append(x)
                number=number/x
                break
    return lista      

