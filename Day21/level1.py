import math

class Statistics:
    def __init__(self,  liste = []):
        self.numbers_list = liste

    def length_of_array(self):
        n = len(self.numbers_list)
        print(f"Nombre : {n}")

    def sum_of_numbers(self):
        print(f"Somme : {sum(self.numbers_list)}")

    def minimum(self):
        print('Min : ', {min(self.numbers_list)})

    def maximum(self):
        print('Max : ', {max(self.numbers_list)})

    def etendue(self):
        n = max(self.numbers_list) - min(self.numbers_list)
        print('Étendue : ', n)

    def moyenne(self):
        n = sum(self.numbers_list) / len(self.numbers_list)
        print('Moyenne : ', n)

    def mediane(self):
        sorted_list = sorted(self.numbers_list)
        n = len(sorted_list)

        if n % 2 == 0:
            mediane = (sorted_list[n // 2 - 1] +
                       sorted_list[n // 2]) / 2
        else:
            mediane = sorted_list[n // 2]

        print(f"Médiane : {mediane}")


    def mode(self):
        frequences = {}

        for number in self.numbers_list:
            frequences[number] = frequences.get(number, 0) + 1

        max_frequency = max(frequences.values())

        modes = [
            number for number, frequency in frequences.items()
            if frequency == max_frequency
        ]

        print(f"Mode : {modes}")

    def ecart_type(self):
        moyenne = sum(self.numbers_list) / len(self.numbers_list)

        somme_ecarts = 0
        for number in self.numbers_list:
            somme_ecarts += (number - moyenne) ** 2

        variance = somme_ecarts / len(self.numbers_list)
        ecart_type = variance ** 0.5

        print(f"Écart type : {ecart_type}")

    def variance(self):
        moyenne = sum(self.numbers_list) / len(self.numbers_list)

        somme_ecarts = 0
        for number in self.numbers_list:
            somme_ecarts += (number - moyenne) ** 2

        variance = somme_ecarts / len(self.numbers_list)

        print(f"Variance : {variance}")

    def frequence(self):
        frequences = {}

        for number in self.numbers_list:
            frequences[number] = frequences.get(number, 0) + 1

        print("Distribution de fréquence :")
        for number, frequency in sorted(frequences.items()):
            print(f"{number} : {frequency}")
    def describe(self):
        self.length_of_array()
        self.sum_of_numbers()
        self.minimum()
        self.maximum()
        self.etendue()
        self.moyenne()
        self.mediane()
        self.mode()
        self.ecart_type()
        self.variance()
        self.frequence()


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

s = Statistics(ages)
s.describe()