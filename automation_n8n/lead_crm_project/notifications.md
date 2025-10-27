# Notifications

Automated notifications are essential for accelerating sales follow-up and ensuring that leads are acted upon quickly. In this workflow, we use n8n to send structured Slack messages to the sales team, combining contact data, deal information, and AI-powered insights.

## Overview
1. Configure Slack credentials and select the target channel.
2. Compose the notification message with contact, deal, and AI insights.
3. Send the notification to the sales team.

## Notification Architecture
### Configure Slack credentials
__Setup Slack API token__

Go to your Slack workspace and create an app to obtain an API token. Visit https://api.slack.com/apps, click "Create New App", and follow the instructions. Assign permissions (chat:write, channels:read, etc.) and install the app to your workspace. Copy the OAuth token.

__Add Slack credentials in n8n workflow__

In n8n, add a `Slack` node and create new credentials using your OAuth token. Then configure the node as follow: 

    Resource: Message
    Operation: Send
    Send Message To: Channel (in this case, but ou can select a specific user)
    Channel:
        By name: #<name_of_channel>
    Messagge Type: Simple Text Message
    Message Text: <your_customized_notification_message>

### Compose the notification message
Include the following in your message:
- Contact details (name, company, email, phone)
- Deal information (title, CRM link)
- AI insights (summary, intent, lead quality, next action)
- Draft of the initial email

Example message:
```
New Lead Received!
Name: John Doe
Company: Acme Inc.
Email: john@acme.com
Phone: +1-555-1234

AI Insights:
- Summary: Interested in demo
- Intent: Sales inquiry
- Lead Quality: 5
- Next Action: Schedule call

Draft Email:
Hi John, thank you for reaching out to Acme Inc. We'd love to schedule a demo with you. Please let us know your availability!

[View Deal in Bitrix24](https://yourcompany.bitrix24.com/rest/123/abc123xyz/crm.deal.list)
```

An exmple of a Slack notification sent using this workflow is showed below in Figure 1.  

<p align="center">
	<img src="images/slack_notification.png" width="400"/>
	<br>
	<em>Figure 1: Slack Notification sent to the sales team with lead details and AI insights.</em>
</p>

## Best Practices
- Test the node and verify it is sending the Slack notifications.
- Handle sensitive data securely (API tokens, contact info).
- Customize the message format for your team's needs.
- Use AI insights to prioritize and tailor outreach.

## Final Notes
Automated notifications eliminate manual follow-up delays and empower the sales team with instant, actionable information. This workflow can be extended to other channels (Teams, email) or enriched with additional AI features (sentiment analysis, business intelligence).
