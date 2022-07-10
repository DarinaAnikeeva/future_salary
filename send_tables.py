import os

from terminaltables import AsciiTable
from salary_helpers import get_vacancies
from headhunter import predict_salary_hh
from superjob import predict_salary_sj
from dotenv import load_dotenv


def table_vacancies(vacancies, languages, title):
    TABLE_DATA = [('Язык программирования', 'Вакансий найдено', 'Вакансий обработано', "Средняя зарплата ")]
    for language in languages:
        TABLE_DATA.append((language, vacancies[language]["vacancies_found"], vacancies[language]['vacancies_processed'],
                           vacancies[language]['average_salary']))

    table_instance = AsciiTable(TABLE_DATA, title)
    table_instance.justify_columns[2] = 'right'
    print(table_instance.table)
    print()


if __name__ == "__main__":
    load_dotenv()
    super_job_key = os.environ['SUPER_JOB_SECRET_KEY']

    sj_vacancies, sj_languages = get_vacancies(predict_salary_sj)
    hh_vacancies, hh_languages = get_vacancies(predict_salary_hh)

    table_vacancies(sj_vacancies, sj_languages, 'SuperJob, Москва')
    table_vacancies(hh_vacancies, hh_languages, 'HeadHunter, Москва')
