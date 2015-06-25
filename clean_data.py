import csv
from collections import defaultdict

disease_list = []

def return_list(disease):
	disease_list = []
	match = disease.replace('^','_').split('_')
	ctr = 1
	for group in match:
		if ctr%2==0:
			disease_list.append(group)
		ctr = ctr + 1

	return disease_list

with open("dataset_dirty1.csv") as csvfile:
	reader = csv.reader(csvfile)
	disease=""
	weight = 0
	disease_list = []
	dict_wt = {}
	dict_=defaultdict(list)
	for row in reader:
		
		if row[0]!="\xc2\xa0" and row[0]!="":
			disease = row[0]
			disease_list = return_list(disease)
			weight = row[1]

		if row[2]!="\xc2\xa0" and row[2]!="":
			symptom_list = return_list(row[2])
		
			for d in disease_list:
				for s in symptom_list:
					dict_[d].append(s)
				dict_wt[d] = weight

	print dict_

with open("dataset_clean1.csv","wb") as csvfile:
	writer = csv.writer(csvfile)

	for key,values in dict_.iteritems():
		for v in values:
			writer.writerow([key,v,dict_wt[key]])

slist = []
dlist = []
with open("nodetable.csv","wb") as csvfile:
	writer = csv.writer(csvfile)

	for key,values in dict_.iteritems():
		for v in values:
			if v not in slist:
				writer.writerow([v,v,"symptom"])
				slist.append(v)
		if key not in dlist:
			writer.writerow([key,key,"disease"])
			dlist.append(key)


			
			

		

