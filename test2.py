import csv

# open the file in universal line ending mode 
with open('output.csv', 'rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

# extract the variables you want
sender = data['from']
mail = {}
for address in sender:
	if (address in mail):
		mail[address] += 1
	else:
		mail[address] = 1
for key, value in mail.items():
	print(key, value, "\n")
with open ("mail.csv", "w") as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(["id", "value"])
	writer.writerow([',', ''])
	for key, value in mail.items():
		headerString = key+","
		writer.writerow([headerString,''])
		writer.writerow([key, value])
