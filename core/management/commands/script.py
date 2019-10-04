from django.core.management.base import BaseCommand

from core.models import Problem

import bs4
import requests
import datetime

class Command(BaseCommand):
    help = 'Scrapes spoj.com to obtain the details of all the classical problems.'
    
    def handle(self, *args, **options):
        self.stdout.write(f'\nScraping started at {datetime.datetime.now()}\n')
        
        count = 0
        while count != 3650:
            self.stdout.write('\nScraping problem details for problem %d to %d' %(count + 1, count + 50))
            
            url = f'http://www.spoj.com/problems/classical/sort=6,start={count}'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36', 'cookie':'inweb_city=Kolkata;'}
            
            response = requests.get(url, headers = headers)
            response.raise_for_status()
            
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            problems = soup.select('td["align"] > a')
            scores = soup.select('td.text-center > a["title"]')

            for problem, score  in zip(problems, scores):
                problem_name = problem.getText()
                problem_code = problem['href'].split('/')[-1]
                problem_score = float(score['title'].split(' ')[1])
                problem_users = int(score.getText())
                obj, created = Problem.objects.update_or_create(code = problem_code, defaults = {'name': problem_name, 'code': problem_code, 'users': problem_users, 'score': problem_score})
            
            count += 50
        
        self.stdout.write(f'\nScraping ended at {datetime.datetime.now()}\n')
