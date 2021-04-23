class Company:
    def __init__(self, name, address, city, state, cnpj):
        self._name = name
        self._address = address
        self._city = city
        self._state = state
        self._cnpj = cnpj


def calculate_salary(salary, days_to_work, worked_days, justified_absences):
    payment = salary / days_to_work * (worked_days + justified_absences)

    if payment <= 1100:
        return payment * 0.925

    if 1100 < payment <= 2203.48:
        return payment * 0.91

    if 2203.48 < payment <= 3305.22:
        return payment * 0.88

    return payment * 0.86
