# Trigger
## Goal
Create a Google form and use a Webhook to trigger the n8n automated workflow each time a form is submmited.
## Overview
1. Create a Google Form.
2. Link the Form responses to a Google Sheet.
3. Add a "Webhook" node to the n8n workflow.
4. Create a Google Apps Script to send a data from a submission to your n8n Webhook URL.
## Trigger architecture
### Google Form
1. Navigate to `https://docs.google.com/forms/`
2. You can create a new Form from scratch or select a template.\
We create a From fromt scratch. Add a title and as many questions as contact data you need (Figure 1). 
<p align="center">
  <img src="../images/form_1.png" alt="Create a Google From from scratch" width="400"/>
  <br>
  <em>Figure 1: Create a Google Form. Don't forget to add a title.</em>
</p>

The basic data are the next:

- First name
- Last name
- Company
- Email address
- Phone number
- Message
In some cases the type of answer will be automatically recognized as soon as you type the question as you can see in the image below (Figure 2). You can also set as required some questions. Suggestion: set as "required" your questions after finishing all test related to the Form creation.
<p align="center">
  <img src="../images/form_2.png" width="400"/>
  <br>
  <em>Figure 2: Add questions to collect data contact.</em>
</p>
After gfinishing an testing your form you can share or embedd into an HTML the form link.

### Google Sheet
Once you have created an tested your form go to the "Responses" tab and link a new spreedsheet or an exiting one (Figure 3).
<p align="center">
  <img src="../images/form_3.png" width="400"/>
  <br>
  <em>Figure 3: Link a spreadsheet to you form.</em>
</p>
We create a new Google Sheet it automatically generate colums as many questions you added to your form. You will use those columns in the Apps Script to send data to yourr n8n workflow.

### Add a "Webhook" node to the n8n workflow
In order to send data from the Google Form to our n8n workflow we will use the Webhook link asociated to our n8n domain. We also working on the n8n GUI (browser), click on "Create Workflow". Click on the "+" button to add a "Webhook" node to set a trigger.\
Configure the node as follow:

  HTTP Method: POST
  Path: googleform (Customize this according to your needs)
  Authentication: None
  Respond: Inmediately

The node will provide both the "Test URL" and  "Production URL" at the top of the parameters. We use the test URL while developing the workflow. The production URL will be set at the end of the project when we set the workflow as "Active".
### Google Apps Script
Google do not provide a Webhook, then, in our case we create an Apps Script to use the n8n Webhook URL (which we generate previously) to send data each time a new form response is submitted.\
Go to your Apps Script and navigate to the "Editor" in the left menu, create a new file and add the content of the `n8n_lead.gs` file. Don't forget to update with your own data.

Now, create a trigger. Go to "Triggers" in the left menu, click on the "Add Trigger" and configure it as follow:

    -Function to run: <your_function_name>
    -Select event source: From spreadsheet
    -Select event type: On form Submit

finally click save.

__NOTE__ Once you set "Active" your n8n workflow, change the Webhook URL to "Production URL", also update the new URL (given by the node after selecting Production URL)) in the Apps Script. The URL will look like as "https://<your_n8n_webhook>/webhook/<your_path>"

__EXTRA__ You can develop a test to run your script including mock data. Check the `test.gs` script.

## Final notes
- You should enable authentication in n8n Webhook for a production system. In the case of CRM service use the "Basic Auth" protocol which include the username and password parameters.
- Test each new step. For example, test your form by submitting a response and check a new row was added to the linked Google Sheet. 

