def startDataflowProcess(data, context):
    from googleapiclient.discovery import build
	#replace with your projectID
	project = "grounded-pivot-266616"
	job = project + " " + str(data['timeCreated'])
	#path of the dataflow template on google storage bucket
	template = "gs://sample-bucket/sample-template"
	inputFile = "gs://" + str(data['bucket']) + "/" + str(data['name'])
	#user defined parameters to pass to the dataflow pipeline job
	parameters = {
		'inputFile': inputFile,
	}
	#tempLocation is the path on GCS to store temp files generated during the dataflow job
	environment = {'tempLocation': 'gs://sample-bucket/temp-location'}

	service = build('dataflow', 'v1b3', cache_discovery=False)
	#below API is used when we want to pass the location of the dataflow job
	request = service.projects().locations().templates().launch(
		projectId=project,
		gcsPath=template,
		location='europe-west1',
		body={
			'jobName': job,
			'parameters': parameters,
			'environment':environment
		},
	)
	response = request.execute()
	print(str(response))
