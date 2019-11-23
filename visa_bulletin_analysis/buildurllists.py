from datetime import date

curr_date = date.today()
url_lists = []
html_file = 'visa-bulletin-for-MMMMMM-YYYY.html'
month_list = ['october', 'november', 'december', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september']
prev_year_list = ['october', 'november', 'december']

def build_url_lists(settings):
    req_year = settings['visa-bulletin-req-year']
    print (req_year)
    curr_year = curr_date.year
    print (curr_year)
    req_urls = []
    final_lists = []
    validate_req(req_year)
    next_year = req_year 

    root_url = settings['url-setting']['root-url']
    while curr_year >= next_year :
       req_urls = buildUrl(root_url, next_year) 
       final_lists = final_lists + req_urls 
       next_year += 1
    return final_lists

    #built_url = buildUrl(root_url, req_year)


def buildUrl(root_url, next_year):
    prev_year = next_year - 1
    monthly_html_file = ' '
    final_url = ' '
    req_urls = []
    for month_str in month_list :
        if  month_str in  prev_year_list:
            monthly_html_file = html_file.replace('YYYY', str(prev_year))
            monthly_html_file = monthly_html_file.replace('MMMMMM', month_str)
            final_url = root_url + '/' + str(next_year) + '/' + str(monthly_html_file)
        else :
            monthly_html_file = html_file.replace('YYYY', str(next_year))
            monthly_html_file = monthly_html_file.replace('MMMMMM', month_str)
            final_url = root_url + '/' + str(next_year) + '/' + str(monthly_html_file)
        req_urls.append(final_url)
    return req_urls


def validate_req(req_year):
    curr_year = curr_date.year
    if req_year > curr_date.year:
        raise ValueError(
            'Incorrect request year, should be less than or equal to current year '
        )
