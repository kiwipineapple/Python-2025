class MathOperations:
    @staticmethod
    def is_even(x):
        if x % 2 == 0:
            print(f'{x} ist gerade Zahl.')
        else:
            print(f'{x} ist NICHT gerade Zahl.')


MathOperations.is_even(6)
