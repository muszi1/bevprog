class developers:
    def __str__(self) -> str:
        return super().__str__()

    def __init__(self, name, rank, years_of_work, payment) -> None:
        self.name = name
        self.rank = rank
        self.years_of_work = years_of_work
        self.payment = payment

    def __str__(self) -> str:
            return f'Developer: (name: {self.name}, ' \
                   f'years_of_work: {self.years_of_work}, ' \
                   f'payment: {self.payment})'

    def up(self, up2 = 10000):
        self.payment += up2

    def plus(self, experience = 1):
        self.years_of_work += experience

    def rank2(self):
        if self.rank == 0:
            print("The developer is Intern.")
        if 1 < self.rank < 2:
            print("The developer is Junior")
        if 2 < self.rank < 5:
            print("The developer is Medior")
        if self.rank > 5:
            print("The developer is Senior")

    def kiiras(self):
        print("Fejlesztő: {0}, Rangja: {1}, Ledolgozott évei: {2}, Fizetése: {3}".format(self.name, self.rank,
                                                                                         self.years_of_work,
                                                                                         self.payment))

def main():
    c1 = developers("Adam", "Intern", 1, 5000)
    c1.up()
    c1.plus()
    c1.rank2()
    c1.kiiras()
    
    
    
    
if __name__ == "__main__":
    main()