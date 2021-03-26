import re


class Citizen:
    def __init__(self, id, name, email, age):
        self.id = id
        self.name = self._is_valid_name(name)
        self.email = self._is_valid_email(email)
        self.age = self._is_valid_age(age)

    # validate name, It should not be greater than 20 char
    def _is_valid_name(self, name):
        if len(name) > 20:
            raise ValueError("Name cannot exceed 20 characters.")
        return name

    # validate email address
    def _is_valid_email(self, email):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, email):
            raise ValueError("It's not an valid email address.")
        return email

    # validate age It should not be negative and not greater than 120
    def _is_valid_age(self, age):
        if age < 0 or age > 120:
            raise ValueError("Not valid age")
        return age


viresh = Citizen('id1', 'viresh patel', 'vpatel@williamhill.us', 30)
# viresh1 = Citizen('id1', 'viresh1 patel1', 'vpatel@williamhill.u', 30)
# viresh2 = Citizen('id1', 'viresh1fggdadgdfgdsfgsd patel1',
#                 'vpatel@williamhill.us', 30)
# viresh3 = Citizen('id1', 'viresh patel',
#                   'vpatel@williamhill.us', -30)

viresh.age = -40
# It can assign negative value. which is wrong.
