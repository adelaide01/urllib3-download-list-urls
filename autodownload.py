#https://media.readthedocs.org/pdf/urllib3/latest/urllib3.pdf
import urllib3
urllib3.disable_warnings()
http = urllib3.PoolManager()

urls = [
'2018-12-11',
'2018-12-12',
'2018-12-13',
'2018-12-14',
'2018-12-15',
'2018-12-16',
'2018-12-17',
'2018-12-18',
'2018-12-19',
'2018-12-20',
'2018-12-21',
'2018-12-22',
'2018-12-23',
'2018-12-24',
'2018-12-25',
'2018-12-26',
'2018-12-27',
'2018-12-28',
'2018-12-29',
'2018-12-30',
'2018-12-31',
]
 
print("downloading the file contents in binary format")

n = 0

for url in urls:
	response = http.request('GET', 'https://apps.osceola.org/Apps/CorrectionsReports/Report/Download/' + url)
	data = response.data.decode('utf-8')
	name = str(n + 1)
	n += 1
	with open("osceola-arrests" + name + ".txt", "wb") as code:
		code.write(response.data)
