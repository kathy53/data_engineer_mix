function onFormSubmit(e) {
  const data = e.namedValues;
  const payload = {
    first_name: data["First Name"][0],
    last_name: data["Last Name"][0],
    email_address: data["Email Address"][0],
    company: data["Company"][0],
    phone_number: data["Phone number"][0],
    message: data["Message"][0]
  };

  const options = {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify(payload)
  };

  UrlFetchApp.fetch("https://<your_n8n_webhook>/webhook-test/<path>", options);
}
