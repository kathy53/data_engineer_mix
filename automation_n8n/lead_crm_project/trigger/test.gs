function testWebhook() {
  const payload = {
    first_name: "James",
    last_name: "Smith",
    email_address: "j.smith@example.com",
    company: "Startup Inc.",
    phone_number: "+1 555 444 3333",
    message: "Could we schedule a demo next Friday?",
    contact_preference: "Email"
  };

  const url = "https://<your_n8n_webhook>/webhook/<path>";
  const options = {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  console.log(response.getContentText());
}

