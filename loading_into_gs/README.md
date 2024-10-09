# Loading data into Google Sheet (GS)
To update information into a (GS) we ae going to follow the next steps:

* Read about the GS API https://developers.google.com/sheets/api/guides/concepts
* Read https://developers.google.com/sheets/api/quickstart/python\
* First create a Google project by navigating to your GCC https://console.cloud.google.com/ or you can use the default one.
* Now create a Google Acoount and credentials, in this work, I created a Service Account, this type of account is used for server-side automation, like uploading to Google Sheets. The steps are as follows:\
        1. Enable the APIs accsess, go to "for APIs & Services" click on "ENABLE APIS AND SERVICES", search and enable "Google Drive API". Now do the same for "Google Sheets API".\
        2. Under the same "APIs & Services" menu navigate to "Credential". Click on "CREATE CREDENTIALS", select "Service Account". Fill out the form and click "Create".\
        3. On the Service Accounts listing, in the right side, find and click "Manage service accounts". Click on the "⋮" icon. of your created Service Account. Then, click on "Manage keys" and "ADD KEY"\
        4. Select the JSON key and click “Create”. A file will be automatically downloaded, move it to a safety location and rename it.
* Now create a GS, the one that is going to be updated and manage automatically.
* Share the spreadsheet with the client_email that appears in the JSON credential file as you normaly share with other email accounts, provide "Edit" access.
* Finally, edit the update_gs.py script according to your needs :)

Here some sources used for the creation of this work: 
- https://www.youtube.com/watch?v=X-L1NKoEi10
- https://www.craftsmensoftware.com/from-csv-to-google-sheet-using-python/ 
- https://www.craftsmensoftware.com/from-csv-to-google-sheet-using-python/