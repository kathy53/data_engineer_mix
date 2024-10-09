# Steps to update data in a Google Sheet using the Google Sheets API
To update data in a GS using Python automatically, follow the next steps:

__Learn about the GS API__
* Read about the GS API Concepts https://developers.google.com/sheets/api/guides/concepts
* Read about the GS API Python Quickstart https://developers.google.com/sheets/api/quickstart/python

__Create a Google Cloud project__
* First, navigate to https://console.cloud.google.com/ 
* You can create a new project or use an existing one.

__Create a Service Account and Credentials__

In this work, a Service Account was created because it is used for server-side automation, like uploading to Google Sheets. The steps to create the account and the necessary credentials are:
1. Enable the APIs access:\
        * Go to "for APIs & Services" in the Google Cloud Console.\
        * Click on "ENABLE APIS AND SERVICES".\
        * Search for and enable "Google Drive API". Do the same for "Google Sheets API".
2. Create Service Account Credentials:\
        * Under the same "APIs & Services" menu, navigate to "Credential".\
        * Click "CREATE CREDENTIALS" and select "Service Account".\
        * Fill out the form and click "Create".\
3. Geenrate a JSON Key for the Service Account:\
        * On the Service Accounts listing, in the right side, find and click "Manage service accounts".\
        * Click the "⋮" (three dots) icon of your created Service Account and select "Manage keys".\
        * Click "ADD KEY" and select "JSON".\
        * Finally, click “Create”. A JSON file will be downloaded automatically. Save it in a secure location and rename it to something descriptive.

__Set up the Google Sheet__
* Create a GS, the one that will be automatically updated by your script.
* Share the spreadsheet with the client_email found in the JSON credential file. Share it as you normaly share with other email accounts, provide "Edit" access.

__Edit the Python Script__
* Edit the update_gs.py script according to your needs :)

Here some sources used for the creation of this work: 
- https://www.youtube.com/watch?v=X-L1NKoEi10
- https://www.craftsmensoftware.com/from-csv-to-google-sheet-using-python/ 
- https://www.craftsmensoftware.com/from-csv-to-google-sheet-using-python/