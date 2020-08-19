from application import people, salary
import datetime
a = datetime.date.today()
if __name__ == '__main__':
    print(a)
    print(people.get_employees())
    print(salary.calculate_salary())

