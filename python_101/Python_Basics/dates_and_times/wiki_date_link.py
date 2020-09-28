import datetime

#TODO: Create get_date function

def create_date_wiki_link(date):
    formatted_day = date.strftime("%B_%d")
    link = f'https://en.wikipedia.org/wiki/{formatted_day}'
    print(link)
    return link

now = datetime.datetime.now()

create_date_wiki_link(now)

#TODO: Create loop to gather user input for date to display