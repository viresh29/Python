import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(message)s')
# file_handler = logging.FileHandler('./log/employee.log')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

"""logging.basicConfig(filename='./log/employee.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')
"""


class Employee:
    """A sample employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(
            'Create Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Viresh', 'Patel')
emp_2 = Employee('Mitali', 'Patel')
