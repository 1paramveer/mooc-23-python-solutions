# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        return (self.__euros + self.__cents) == (another.__euros + another.__cents)
    
    def __gt__(self, another):
        return (self.__euros + self.__cents) > (another.__euros + another.__cents)
    
    def __ne__(self, another):
        return (self.__euros + self.__cents) != (another.__euros + another.__cents)

    def __add__(self,another):
        total_euros = self.__euros + another.__euros
        total_cents = self.__cents + another.__cents
        if total_cents >= 100:
            div_euros = int((str(total_cents))[:1])
            total_cents = int((str(total_cents))[1:])
            total_euros += div_euros
        return Money(total_euros, total_cents)
    
    def __sub__(self,another):
        total_euros = self.__euros - another.__euros
        total_cents = self.__cents - another.__cents

        if total_cents < 0:
            total_euros -= 1
            total_cents += 100

        if total_euros < 0:
            raise ValueError
        
        return Money(total_euros, total_cents)
            

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1
