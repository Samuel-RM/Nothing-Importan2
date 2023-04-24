try:
    print(0 / 0)
    assert 1 != 1, ' Uno no es igual que uno' 
    age = int(input(' Dame tu edad: '))
    if age < 18:    
        raise Exception(' Eres menor de edad')
except ZeroDivisionError as error:
    print ( error)       
except AssertionError as error:
    print (error)   
except Exception as error2:
    print(' SOS MENOR WEON LPTM')

print('holaa')
