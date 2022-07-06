import requests
import json
from salary_helpers import get_two_params


def get_all_vacancies_hh(page, vacancy):
    url = "https://api.hh.ru/vacancies"
    all_vacancies_info = []
    while True:
        payload = {
            "text": vacancy,       # название запроса, по которому ищется информация
            "area": 1,             # id города (Москва)
            "period": 1,           # время, в течение которого собирается информация с сайта
            'page': page           # номер страницы, на которой будет искаться информация
        }
        page_response = requests.get(url, params=payload)
        page_response.raise_for_status()
        pages_number = page_response.json()['pages']
        page += 1
        all_vacancies_info.append(json.loads(page_response.text))
        if page >= pages_number:
            break
    return all_vacancies_info, page_response.json()["found"]


def predict_salary_hh(language):
    vacancies_info, vacancies_found = get_all_vacancies_hh(page=0, vacancy=f'Программист {language}')
    all_middle_salary = 0
    vacancies_processed = 0
    for page in vacancies_info:
        for job in page['items']:
            if job['salary']:
                middle_salary, vacancies = get_two_params(job['salary'],
                               salary_from='from',
                               salary_to='to',
                               currency='RUR')
                all_middle_salary += middle_salary
                vacancies_processed += vacancies
    average_salary = all_middle_salary // vacancies_processed
    return average_salary, vacancies_processed, vacancies_found
