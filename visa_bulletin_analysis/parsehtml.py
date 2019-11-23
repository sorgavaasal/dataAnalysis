import pandas
import bs4 as bs
import urllib.request as urreq

# https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin/2020/visa-bulletin-for-december-2019.html

#dfs = pandas.read_html('https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin/2020/visa-bulletin-for-december-2019.html')

#for df in dfs:
    #print (type(df))
    #print (df)
    #print (df.columns)
    #print (type(df.values))
    #print (df.values)
    #print (df.keys)

source = urreq.urlopen('https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin/2020/visa-bulletin-for-december-2019.html').read()
soup = bs.BeautifulSoup(source, "lxml")
body = soup.body

table_list = body.find_all('tbody')
#print (table_list)
for table_var in table_list:
    table_var_next = table_var
    while table_var_next is not None:
        if table_var_next.contents > 0:
            print (table_var_next.text)
        table_var_next = table_var.next
        #print (table_var)
        #table_data = table_var.find_all('td')
        #print (table_data)
        #for table_data_indv in table_data:
        #    if (len(table_data_indv.contents)) > 0:
        #       if ('Employment' in table_data_indv.text) :
        #           print (table_data_indv.contents)
        #           print (table_data_indv.text)
        #       else:
        #           break
        #   else:
        #       break

def break_down_vb(vb_url) :
    source = urreq.urlopen(vb_url).read()
    soup = bs.BeautifulSoup(source, "lxml")
    body = soup.body
    ## list of tables from the body to be extracted 
    table_list = body.find_all('tbody')
    for table_var in table_list:
        print (table_var.values)
