from datetime import datetime
filename = 'datacamp.csv'

from bs4 import BeautifulSoup
import requests
import urllib
import csv
usrnm = ['aroonkp','adityakeshri' ,'aav1' ,'preethip12' ,'adityaarun007', 'dntandan' ,'swapnilshikhar10' ,'harshith207' , 'pradyumnahebbar552-71d547dd-110e-4e5b-8b1d-a657a7a98845', 'AswinGopinathan' , 
'mohitsinha1108' , 'deeparsh98' ,'sombolafatty' ,'siddhant26ranjan' , 'pulkitbansl' ,'pallavikumari1601' ,'akashashu17', 'thesolver' ,'impiyush' ,'itsauselessid' ,'shrutisss2511' , 'simranise','aishwarya2241' , 'ruchikajain101' , 'akshatjaipuria' , 'pratheekr33' , 'vimmu1598' , 'anushackulal' ]

csv_file = open(filename, 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'XP', 'Course Completed' , 'Exercises Aced' , 'date'])
for url in usrnm:
	source = urllib.request.urlopen("https://www.datacamp.com/profile/" + url).read()

	soup = BeautifulSoup(source, 'lxml')

	
	try:
		for div in soup.find_all('div'):		
			  name_stu = str(div.find('div', class_='profile-header__name').text)
			  stat_stu = str(div.find('div', class_='row profile-header__stats').text)
				
			  print(name_stu.strip() , end = ' ')
			  stat_stu = stat_stu.replace('\n', ' ')
			  stat_stu = stat_stu.replace(',', '')
			  arr = stat_stu.split(' ')
			  #for x in range(len(stat_stu)):
			  print(arr[3] , arr[10] , arr[17])

			  csv_writer.writerow([name_stu.strip(), arr[3], arr[10], arr[17] , filename])
	except (AttributeError):	
		pass
		  
csv_file.close()
print()
print('				TechHub DS Ranking')
import pandas as pd
df = pd.read_csv(filename)
df = df[['Name', 'XP', 'Course Completed' , 'Exercises Aced']]
dff = df.sort_values('XP' , ascending = False).reset_index(drop = True)
print(dff)

s = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">'
s = s +'<table class="table table-striped table-dark"><thead><tr><th scope="col">#</th><th scope="col">Name</th></th><th scope="col">XP</th><th scope="col">Course Completed</th><th scope="col">Exercises Aced</th></tr></thead><tbody>'
    
for index , x  in dff.iterrows():
	s = s+'<tr>'
	s = s+ '<th scope="row">' + str(index) + '</th>'
	s = s+'<td>'+ str(x['Name']) + '</td>' 
	s = s+'<td>'+ str(x['XP']) + '</td>'
	s = s+'<td>'+ str(x['Courses Completed']) + '</td>'
	s = s+'<td>'+ str(x['Exercises Aced']) + '</td>'
	s = s+ '</tr>'
    
s = s + '</tbody></table>'

text_file = open("rank.html", "w")

text_file.write(s)

text_file.close()