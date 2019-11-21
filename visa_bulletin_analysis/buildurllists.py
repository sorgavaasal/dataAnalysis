from datetime import date

curr_date = date.today()
url_lists = []
html_file = 'visa-bulletin-for-MMMMMM-YYYY.html'
month_list = ['october', 'november', 'december', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september']
prev_year_list = ['october', 'november', 'december']

def build_url_lists(settings):
    req_year = settings['visa-bulletin-req-year']
    curr_year = curr_date.year
    validate(req_year)
    next_year = req_year 
    root_url = settings['url-setting']['root-url']
    while curr_year <= next_year :
       req_urls = buildUrl(root_url, next_year) 
        

    #built_url = buildUrl(root_url, req_year)


def buildUrl(root_url, next_year):
    prev_year = next_year - 1
    for month_str in month_list :
        if  month_str in  prev_year_list:
            monthly_html_file = html_file.replace('YYYY', )
        root_url = root_url + '/' + next_year + '/' + 


def validate_req(req_year):
    curr_year = curr_date.year
    if req_year > curr_date.year:
        raise ValueError(
            'Incorrect request year, should be less than or equal to current year '
        )
