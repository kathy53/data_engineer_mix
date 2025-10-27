First job

Summary
Seeking N8N Expert to Build AI Agents & Automations

Description:

We are looking for an experienced N8N expert to help us design and implement AI-powered agents that streamline our workflows. The ideal candidate has a strong background in automation, integrations, and applying LLMs (ChatGPT, Claude, Gemini, etc.) to real-world business processes.

Our goal is to build scalable, reliable, and intelligent workflows that automate tasks across multiple tools (CRM, email, scheduling, reporting, etc.), while also creating AI Agents that can:

Analyze incoming data and make intelligent decisions

Trigger multi-step workflows in N8N

Communicate with external APIs (marketing, sales, customer success, legal tech tools, etc.)

Provide summaries, insights, or recommendations to our team

Responsibilities:

Review our current workflows and identify automation opportunities

Build AI Agents within N8N that integrate with third-party apps and APIs

Leverage LLMs for decision-making, text generation, and data analysis

Ensure scalability, reliability, and maintainability of workflows

Provide documentation and handover training

Requirements:

Proven experience with N8N (portfolio/examples required)

Strong understanding of API integrations, webhooks, and data mapping

Experience with AI models (OpenAI, Anthropic, etc.) and how to embed them in automations

Familiarity with CRMs, marketing automation, or legal tech tools is a plus

Strong problem-solving and communication skills

Deliverables:

One or more fully functional AI Agent workflows in N8N

Documentation for setup, usage, and troubleshooting

Recommendations for future improvements

Budget & Engagement:

Open to hourly or fixed-price milestones

Looking for a long-term collaboration if successful

Pro tip for posting: You can add screening questions like:

Share an example of an N8N workflow you’ve built that integrates AI.

How do you ensure your automations remain reliable and scalable?

Which AI models/tools do you have hands-on experience with?

The first project will be to: create an agent that can re-write ebooks in a brand voice and conduct research and share resources... This agent would be created on n8n
Building an agent in n8n for rewriting ebooks requires connecting several distinct functions into a single, seamless workflow: extracting content, processing it through an LLM trained on your brand's voice, conducting additional research, and distributing the final output.
Here is a step-by-step guide to creating this agent in n8n, with details on the nodes and integrations you will need.
1. Set up the workflow trigger
Choose a trigger that will start the process. This provides the input for your ebook.
Manual Trigger: To start the workflow yourself, use the Manual Trigger node. You can add a Set node afterward to define the ebook text you'll work with.
Google Drive/Notion Trigger: Use a Google Drive Trigger or a Notion Trigger to run the workflow automatically when a new document is added to a specific folder or database.
Webhook Trigger: To start the process from an external application, create a Webhook Trigger that receives the ebook text in JSON format.
2. Extract and prepare the ebook content
The trigger will provide the ebook content, but it may require some initial processing.
Read Document Node: If you are using a trigger from a service like Google Drive or Notion, use the corresponding read node to fetch the document's contents.
Text Processing Node: Use the Edit Fields (Set) node to normalize and structure the incoming text data. For example, convert the content into Markdown and remove any unnecessary images or links.
3. Establish your brand voice guidelines
To ensure the LLM rewrites the content correctly, you must first define your brand voice.
HTTP Request Node: Fetch existing examples of your branded content from your website or a storage location using an HTTP Request node.
LLM Node (Voice Analysis): Use an LLM Chat Model node with a prompt to analyze the content and identify key themes, tone, structure, and language patterns. This "voice analysis" model will produce the brand voice guidelines.
Set Node: Store the brand voice guidelines in a Set node to use as a system instruction for later steps.
4. Rewrite the ebook with an LLM
This is the core of the agent, where the rewriting happens.
LLM Chat Model Node (Rewriting): Add another LLM Chat Model node. For the system prompt, provide both the ebook content and the brand voice guidelines created in the previous step. Instruct the AI to rewrite the ebook in that specific style.
Recursive Writing Agent: For more control and higher-quality output, consider using a recursive writing and editing loop. This advanced technique uses two LLMs: one "Writing Agent" that generates the draft and a separate "Editing Agent" that refines it until the content meets quality standards.
5. Conduct additional research
If your ebook requires new or updated information, add a research step.
Sub-workflow for Research: You can call a sub-workflow to handle the research. This workflow can accept a query from the main workflow and perform its own sequence of searches.
Web Search and Scrape Nodes: Use a series of nodes like Apify or a custom HTTP Request with a search API (e.g., Google's) to find information.
LLM Node (Summarization): Use an LLM Chat Model node to summarize the scraped content, making it easier to integrate into the rewritten ebook.
6. Deliver and share resources
After the content is rewritten and researched, you can distribute the output to your team or a storage location.
Google Docs/Notion Node: Automatically save the rewritten ebook to a new Google Doc or a Notion page.
Google Drive Node: Save the document as a specific file type (e.g., PDF) to a Google Drive folder.
Email Node: Notify your team that the new version is ready for review by sending an email with a link to the document.
Slack/Teams Node: Post a notification directly to a Slack or Microsoft Teams channel to update your team on the rewritten ebook.
Workflow Sharing: For seamless collaboration, you can share the entire workflow with your team members in n8n. This allows them to run, edit, or view the execution logs.


__________________________________

Second job 


Summary
We are seeking a skilled specialist in n8n for automating tasks and creating AI agents. The ideal candidate will have a proven track record in designing and implementing complex automation solutions tailored to business needs. You will be responsible for streamlining workflows, enhancing efficiency, and integrating various systems using n8n. If you have a strong understanding of automation principles and a knack for problem-solving, we want to hear from you!