import os
import sys

dbName = ''

if "--db=" not in str((sys.argv)):
	print ("Please specify db name where you want to import collections using flag --db=dbName")
else:
	# get db name form flag arguments
	dbName = (sys.argv)[1].rsplit('--db=', 1)[1]
	print ('Using db: ' + dbName)

	listCollections = os.listdir('collections')

	if len(listCollections) == 0:
		print ("There are no files in 'collections' directory. Please make sure you have your 'collectionName.json' files in this directory")
	else:
		for file in listCollections:

			# filename = os.fsdecode(file)
			filename = file

			if filename.endswith(".json"):
				print("Current file: " + filename)

				jsonFileName = 'collections/' + filename
				collectionName = filename.rsplit('.', 1)[0]
				print("Importing collection: " + collectionName)

				command = 'mongoimport -d ' + dbName + ' -c ' + collectionName + ' --file ' + jsonFileName
				os.system(command)
				print ("Successfully imported " + collectionName)

			else:
				print ("There are no files in 'collections' directory. Please make sure you have your 'collectionName.json' files in this directory")

		print ("All collections imported Successfully")