To scrape a site,give a POST request to "http://127.0.0.1:5000/upload",
feeding in the following parameters.
1. excel input file as a value for "file" as a key.

wait until execution is finished and respective response is 
generated in console window

Status code and their meanings:

when a 201 code is returned it indicates that execution is completed 
successfully and in order to view the results check the files under
output folder of project dir

when a 500 code is returned it indicates an unknown error has come
up, reach out to the provider to resolve the issue or check the logs.

when a 400 code is returned it indicates a json syntax error which is usually from the user end
and generally it is the error in the way input file is uploaded, check if file is of type csv.
If the error is still there, reach out to the provider.

XXXXXXXXXXXX---END---XXXXXXXXXXXX
