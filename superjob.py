import requests
import math
import os
from salary_helpers import get_two_params
from dotenv import load_dotenv

load_dotenv()
super_job_key = os.environ['SUPER_JOB_SECRET_KEY']

def get_all_vacancies_sj(page, vacancy):
    url = "https://api.superjob.ru/2.0/vacancies"
    all_vacancies_info = []
    while True:
        headers = {
            "X-Api-App-Id": super_job_key
        }
        payload = {
            "keyword": vacancy,                  # название запроса, по которому ищется информация
            "town": 4,                           # id города (Москва)
            'period': 1,                         # время, в течение которого собирается информация с сайта
            "count": 10                          # номер страницы, на которой будет искаться информация
        }
        page_response = requests.get(url, headers=headers, params=payload)
        page_response.raise_for_status()
        pages_number = math.ceil(page_response.json()['total'] / payload['count'])
        page += 1
        all_vacancies_info.append(page_response.json())
        if page >= pages_number:
            break
    return all_vacancies_info, page_response.json()['total']


def predict_rub_salary_sj(language):
    vacancies_info, vacancies_found = get_all_vacancies_sj(page=0, vacancy=f'Программист {language}')
    all_middle_salary = 0
    vacancies_processed = 0
    for page in vacancies_info:
        for job in page["objects"]:
            middle_salary, vacancies = get_two_params(job,
                           salary_from="payment_from",
                           salary_to="payment_to",
                           currency='rub')
            all_middle_salary += middle_salary
            vacancies_processed += vacancies
    average_salary = all_middle_salary // vacancies_processed
    return average_salary, vacancies_processed, vacancies_found





