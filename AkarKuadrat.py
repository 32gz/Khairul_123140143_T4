import math

class InputError(Exception):
    
    pass

class NegativeNumberError(Exception):
    
    pass

class ZeroInputError(Exception):
    
    pass

class SquareRootCalculator:
    def __init__(self):
        self.number = None

    def get_input(self):
        try:
            user_input = input("Masukkan angka: ")
            try:
                self.number = float(user_input)
            except ValueError:
                raise InputError("Input tidak valid. Harap masukkan angka yang valid.")

            if self.number < 0:
                raise NegativeNumberError("Input tidak valid. Harap masukkan angka positif.")
            elif self.number == 0:
                raise ZeroInputError("Error: Akar kuadrat dari nol tidak diperbolehkan.")

        except (InputError, NegativeNumberError, ZeroInputError) as e:
            print(e)
            return False

        return True

    def calculate_square_root(self):
        result = math.sqrt(self.number)
        print(f"Akar kuadrat dari {self.number} adalah {result}")

    def run(self):
        while True:
            if self.get_input():
                self.calculate_square_root()
                break

# Menjalankan program
if __name__ == "__main__":
    calc = SquareRootCalculator()
    calc.run()
