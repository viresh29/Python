

url_file = open('./urls.txt')

for row in url_file:
    url = row.strip()
    print(url)
