# KPIs to assess the CRM automation project

In this file we lists suggested Key Performance Indicators (KPIs) to evaluate the effectiveness, reliability, and business impact of the CRM automation workflow (n8n → Bitrix24 → Slack and AI enrichment).

Each KPI includes: definition, formula (if applicable), data source, recommended frequency, example target, and suggested owner.


## Key variables
Here some concepts involved in the KPI creation and :
1. Inputs: 
    - Form submissions (Google Forms → n8n webhook) 
    - Bitrix24 contact/deal creation logs 
    - n8n execution logs 
    - Slack notifications 
    - AI enrichment outputs
2. Outputs:
    - Numeric KPI values (counts, rates, latencies)
    - Dashboards
    - Alerts.
3. Success criteria:
    - Improved lead-to-contact latency
    - Reduced manual-entry errors
    - Measurable increase in qualified leads and conversion activity.

## Data quality & correctness

1) Data Entry Error Rate
- Definition: Percentage of created contacts/deals that require manual correction afterwards (wrong/missing fields, duplicates).
- Formula: (Number of records flagged for correction / Total records created) * 100
- Data source: Bitrix24 audit/change logs, manual QA tags, or a deduplication report.
- Frequency: Weekly
- Example target: < 2% after rollout
- Owner: CRM admin / Ops

2) Duplicate Lead Rate
- Definition: Percentage of new leads that are duplicates of existing contacts/deals.
- Formula: (Number of duplicates detected / Total leads created) * 100
- Data source: Bitrix24 duplicate detection results or dedupe job output.
- Frequency: Weekly
- Example target: < 1.5%
- Owner: Data Engineer / CRM admin


## Lead flow & responsiveness

3) Lead-to-Contact Creation Time (Latency)
- Definition: Time between form submission timestamp and Bitrix24 Contact creation timestamp.
- Formula: Median/95th percentile of (contact_created_at - form_submitted_at)
- Data source: n8n webhook timestamps + Bitrix24 contact creation timestamps
- Frequency: Daily (report percentile weekly)
- Example target: median < 30 seconds; 95th percentile < 5 minutes
- Owner: Automation owner / Sales Ops

4) Lead-to-Notification Time
- Definition: Time between form submission and Slack notification delivered to sales channel.
- Formula: median/95th percentile of (slack_sent_at - form_submitted_at)
- Data source: n8n logs + Slack message timestamps
- Frequency: Daily
- Example target: median < 1 minute
- Owner: Automation owner

5) First-response Rate (within SLA)
- Definition: Percentage of leads receiving a human-first-response (call/email) within defined SLA after automation (e.g., 4 hours).
- Formula: (Number of leads with first response <= SLA / Total assigned leads) * 100
- Data source: Bitrix24 activity logs (first outgoing activity), assignment records
- Frequency: Weekly
- Example target: >= 80% within 4 hours
- Owner: Sales Manager


## Lead quality & prioritization

6) AI Lead Quality Distribution
- Definition: Distribution of AI-generated lead quality labels (rating: 1-5) and % of leads in each bucket.
- Formula: Count by label / Total leads
- Data source: AI enrichment node outputs saved to Bitrix24 fields
- Frequency: Weekly
- Example target: High >= 20% (depends on lead source)
- Owner: Product / Sales Ops

7) Conversion Rate by AI Quality
- Definition: Conversion rate (lead → qualified → deal closed) segmented by AI lead_quality label.
- Formula: (Closed deals from leads with label X / Total leads with label X) * 100
- Data source: Bitrix24 pipeline stages, AI label in lead fields
- Frequency: Monthly
- Example target: High label conversion > Medium > Low (expected ordering)
- Owner: Sales Manager / Data Analyst


## Process efficiency & automation impact

8) Manual Intervention Rate
- Definition: Share of workflow executions that required human intervention (errors, retries, manual fixes) to complete.
- Formula: (Number of executions with intervention / Total executions) * 100
- Data source: n8n execution logs (error states, manual re-runs) and incident tickets
- Frequency: Weekly
- Example target: < 3%
- Owner: Automation owner / SRE

9) Automation Coverage
- Definition: Percentage of form submissions handled fully by automation (contact & deal created + AI enrichment + Slack notification) without manual fallback.
- Formula: (Number of fully handled submissions / Total submissions) * 100
- Data source: n8n execution outcomes + Bitrix24 record existence checks
- Frequency: Weekly
- Example target: >= 95%
- Owner: Automation owner


## Reliability & system health

10) Workflow Success Rate (n8n)
- Definition: Percentage of n8n workflow runs that complete successfully without unhandled errors.
- Formula: (Successful runs / Total runs) * 100
- Data source: n8n execution logs
- Frequency: Daily
- Example target: >= 99.5%
- Owner: SRE / Automation owner

11) Mean Time to Detect (MTTD) and Mean Time to Recover (MTTR)
- Definition: MTTD — time between issue occurrence and detection/alert; MTTR — time between detection and restoration of normal operation.
- Data source: Monitoring/alerting system + incident logs
- Frequency: Monthly review
- Example target: MTTD < 5 minutes; MTTR < 30 minutes for critical failures
- Owner: SRE


## User adoption & satisfaction

12) Sales Team Adoption Rate
- Definition: Share of sales users who actively use the automated notifications / AI notes or mark them as used in follow-up actions.
- Formula: (Active users interacting with Slack notifications or CRM AI fields / Total assigned users) * 100
- Data source: Slack interaction logs, Bitrix24 user activity logs
- Frequency: Monthly
- Example target: >= 90% of active sales team members
- Owner: Sales Manager

13) Sales Satisfaction Score (qualitative)
- Definition: Periodic (monthly/quarterly) short survey to measure sales team's satisfaction with automation outputs (usefulness of AI draft email, accuracy of lead_quality, timeliness).
- Data source: Survey responses (1–5 scale) or NPS
- Frequency: Monthly or quarterly
- Example target: Average >= 4/5
- Owner: Head of Sales


## Business outcomes

14) Lead-to-Deal Conversion Rate
- Definition: Percentage of leads that become closed/won deals.
- Formula: (Closed-won deals from automated leads / Total automated leads) * 100
- Data source: Bitrix24 pipeline/reporting
- Frequency: Monthly/Quarterly
- Example target: Improve baseline by X% after automation (baseline must be measured before rollout)
- Owner: Sales Ops / Business Analyst

15) Time-to-Revenue (for closed deals)
- Definition: Time from form submission to first invoice or revenue recognition event (if trackable in CRM).
- Data source: Bitrix24 + billing system linkage
- Frequency: Quarterly
- Owner: Finance / Sales Ops

