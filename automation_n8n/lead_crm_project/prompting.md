# AI insights
We use AI insights to create context around a contact based on their form responses. In this way, we provide helpful information to the sales team and add value in the following areas:
- Reducing delays in contacting leads
- Increase sales opportunities.
- Extract structured business intelligence from raw text.
## Overview
1. Configure OpenAI credentials.
2. Message an OpenAI model to enhance the CRM process with intelligence.
## AI insights architecture
### Configure OpenAI credentials
__Setup OpenAI API key__

Navigate to the page platform.openai.com and create an account if you don't already have one. Once you are logged in to`https://platform.openai.com/api-keys` and click on `Create new secret key`, then configure the information:

 Owned by: You**
 Name (optional): n8n-key
 Project: Default project***
 Permissions: All****

** For this project, we use a personal API key, but after setting the workflow in Production, you need to evaluate if using the "Service account" API key is a better option for you based on your entire platform/service. Key factors are:
- scalability
- tied to a company
- discounts offered by Cloud providers.

*** You can opt for creating a new and dedicated Project for it by clicking on the "Default project" upper left button, then select "Create project", set a name, and click on Create.\
**** It is better to opt for "Restricted" permissions. In this case, you can select the "Assistant" options and include that configuration in your n8n workflow by selecting the corresponding "Assistant Actions" nodes.

Finally, click on "Creating key" and copy the generated "Secret key"

To use your API key, you need to provide billing information. Navigate to your settings account (gear icon in the upper right corner), search for "Billing" in the left menu, and click "Add payment details." Provide the required information and select a plan.

__Add OpenAI credentials in n8n workflow__

We use a `Message a Model` node. In this project, we use `gpt-4o-mini` (a cost-effective, fast, and high-quality model) from OpenAI, however you can also choose from other pairs of providers and models, such as Groq or Gemini. Additionally, n8n has many built-in nodes for OpenAI actions and events. For example, you can opt for `Message an assistant` under `Assistant Actions` rather than using `Text Actions` as in this workflow. You need to select the option that best fits your requirements.\
In any case, you are asked for an API key in the first parameter of the node, then click on `Create new credentials`. For now, include your API Key and leave the remaining parameters with the default information. 

__NOTE__ Remember to check your permissions for the API key before setting your workflow into Production.
### Message an OpenAI model to enhance the CRM process with intelligence.


This node processes the lead data to provide structured business intelligence:
- Next action: recommended step for the sales team
- Summary: one-sentence description of the lead
- Intent: sales inquiry, support, spam, or other
- Lead quality: rating (1–5)

Additionally, we ask the model for a draft of an initial email based on the following constraints:
- Keep the email under 150 words.
- Thank them for reaching out.
- Mention their company name.
- Suggest the next step (e.g., scheduling a call, demo, or more info).
- Use a warm, approachable tone.

This setup saves you time in cases when a submission is spam or misses a message.

These business insights are shared with the Sales team through a Slack message.