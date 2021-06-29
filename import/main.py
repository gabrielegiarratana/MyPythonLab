from module1 import fun1
import module2 as m2 #se importo così, nell'invocazione devo mettere il prefisso del modulo
#from module 2 import * #se import così, nell'invocazione non devo mettere il prefisso del modulo

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fun1() #non serve piu' usare il preefisso del modulo
    m2.fun2()
