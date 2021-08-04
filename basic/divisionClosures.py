def make_division_by(n):
    def divide(x):
        return x/n
    return divide

division_ny_3 = make_division_by(3)
print(division_ny_3(18))

division_ny_5 = make_division_by(5)
print(division_ny_5(100))

division_ny_18 = make_division_by(18)
print(division_ny_18(54))