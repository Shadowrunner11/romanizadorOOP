class Romanizer:
    def start(self):
        continuar = True
        while continuar:
            
            number = input("Ingrese un numero \n")
            while not self.isValidNumber(number):
                number = input("Intente de nuevo \n")
        
            number =int(number)

            print(self.rominze(number))

            continuar = input("Deseas repetir el programa?[y/n] \n").lower()
            while continuar not in ["y", "n"]:
                continuar = input("No e suna opcion, deseas continuar? [y/n] \n").lower()

            continuar= True if  continuar=="y" else False

    def rominze(self,num:int)->str:
        valores= [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanos= ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ans=""

        for i in range (0,len(valores)):
            while(num>=valores[i]):
                ans +=romanos[i]
                num -=valores[i]

        return "El numero en romanos es "+ ans
        
  
    def isValidNumber(self,number)->bool:
        try:
            number = int(number)
            if number<0 or number >4000:
                raise Exception
            return True
        except Exception:
            return False
         
   

if __name__=="__main__":
    Romanizer().start()