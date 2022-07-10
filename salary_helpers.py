
def predict_salary(salary_from, salary_to):
    if not salary_from and not salary_to:
        middle_salary = 0
    elif not salary_to or salary_to == 0:
        middle_salary = salary_from * 1.2
    elif not salary_from or salary_from == 0:
        middle_salary = salary_to * 0.8
    else:
        middle_salary = (salary_from + salary_to) // 2
    return middle_salary


def get_vacancies(function):
    languages = ["JavaScript", "Python"]
        # , "Java", "C", "C++", "PHP", "CSS", "C#"]
    vacancies = {}
    for language in languages:
        average_salary, vacancies_processed, vacancies_found = function(language)
        vacancies[language] = {
            "vacancies_found": vacancies_found,
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }
    return vacancies, languages


def get_two_params(job, salary_from, salary_to, currency):
    middle_salary = 0
    vacancies = 0
    if job['currency'] == currency:
        middle_salary = predict_salary(job[salary_from], job[salary_to])
        if middle_salary != 0:
            vacancies = 1
    return middle_salary, vacancies