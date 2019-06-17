from bs4 import BeautifulSoup
import pandas as pd
import requests

def scrape(ticker_symbol):
    url = f'https://www.streetinsider.com/ec_earnings.php?q={ticker_symbol}'

    cookie = 'D_HID=1EBE988A-3691-32A6-936C-6B9CE4F5100A; D_IID=3C3B9C01-4D76-3E33-9B8A-4C135E4AD36D; D_UID=CDD3A95A-772D-30FA-8160-81D19FE02564; D_ZID=B68E42BE-1E2F-3A2C-BE02-1A7EEAD46721; D_ZUID=D350923E-AF5E-374F-90C1-C4C475B8EA36; bounceClientVisit2938=N4IgZgbgLiBcCMBWAbABgOwCYAc7vIBoQIBLAEziTS2wGZFEAWATmWedqIEMB7OVIgBsADnBAALKFGEBnAKS0AgnMwAxFaoDu2gHQyoAJwCmRqCQB2M8kYM6AxjwC2Go3YD6RrgfMWA5jJ1hcWEFVQBHBQARCBBuGX4iCGEY2E4QClh02JADMW1NHV8eHl9BI3snbLtoShQMHHpEIisMwhBfO1zYZGwiRwT08jFMTHR4Wkx4VB6OWmxEeHhMZmzBGoQ6mjxkAF8gA; _ga=GA1.2.351990870.1560728354; _gid=GA1.2.1163975291.1560728354; __browsiSessionID=77f84637-b21b-417f-b7b6-006fb6224421&false&false&DEFAULT&us&desktop-1.16.1&false; __browsiUID=cad7c3d6-acf0-44d5-9a75-7745b98a6213&{"bt":"Browser","os":"macOS","osv":"10.14.5","m":"Macintosh","v":"Apple","b":"Safari","p":2}; IC_viewcount_www.streetinsider.com=7; __gads=ID=e2a0e1812b69faf9:T=1560728348:RT=1560728530:S=ALNI_MZcTKK2X6XHyFYh1221Fja_BcAFgg; __idcontext=eyJjb29raWVJRCI6IlVKNFJHTEc2UENDV0o2UlNWWTVVQkdaQkk1NDVERDNGQUZRWFVVQU4yVUNBPT09PSIsImRldmljZUlEIjoiVUo0UkdMRzZQRERHSlpZRFY1RVdaR0xFT0pZWkRNMklIUk9XRVVZT1ZZS1E9PT09IiwiaXYiOiIzMzU3V0ZPUFNHQksyMkhRUU1NMlBDREJMTT09PT09PSIsInYiOjF9; fi_utm=www.google.com%7Corganic%7C%7C%7C%7C; fitracking_12=no; bounceClientVisit2938v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgO6kB0KCATgKY0ICWAdigwCY1VkDGA9gLZEa3APo0AhlSbMA5ijIQ4ETPgCOmACIA3EABoQVGCFLEyM3rxlgaPASAC+QA; __qca=P0-1568873715-1560728349361; cto_lwid=1a0a395c-6972-4b7c-9da5-a441127c525d; D_SID=67.164.106.213:Skej23yTS0HaLnNOKrJhBs7cQ4NcmeyCWV8XholjFTA; PHPSESSID=iotqo1pdlrcejq93beh4fqq2a2'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
    referer = 'https://www.google.com/'
    headers = {
        'User-Agent': user_agent,
        'Referer': referer,
        'Cookie': cookie,
    }

    r = requests.get(url, headers=headers)

    page = r.text
    soup = BeautifulSoup(page, 'lxml')

    tables = soup.find_all('table', {'class': 'earning_history'})

    data = []
    for table in tables:
        rows = table.find_all('tr', {'class': 'is_hilite'})
        for row in rows:
            cells = row.find_all('td')
            row_text = [cell.text for cell in cells]
            data.append(row_text)
    earn = pd.DataFrame(data)

    cols = [1, 8, 9, 10, 11]
    earn = earn.drop(cols, axis=1)

    renamed_cols = {
        0: 'DATE',
        2: 'QTR',
        3: 'EPS',
        4: 'EPS_CONSENSUS',
        5: 'SURPRISE',
        6: 'REVENUE',
        7: 'REVENUE_CONSENSUS',
    }
    earn = earn.rename(index=str, columns=renamed_cols)

    earn['DATE'] = pd.to_datetime(earn['DATE'])
    earn = earn.sort_values('DATE', ascending=False)

    return earn