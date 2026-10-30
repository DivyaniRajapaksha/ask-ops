---
doc_title: Postmortem - Webhook Delivery Outage (March 2026)
doc_type: postmortem
source_url: https://wiki.nimbuspay.example/eng/postmortems/2026-03-14-webhooks
updated_at: 2026-03-20
allowed_groups: [engineering]
---

# Postmortem: Webhook Delivery Outage, March 14, 2026

## Summary

On **March 14, 2026**, NimbusPay stopped delivering webhooks for **47 minutes** (13:05 to 13:52 UTC). Payments themselves were processed normally; only the notifications to merchants were delayed.

## Impact

- About **3,200 merchants** missed webhooks during the window.
- Merchants who relied on `payment.succeeded` webhooks to ship orders saw delays.
- No webhooks were lost. All were delivered after recovery thanks to automatic retries.

## Root cause

The TLS certificate on the internal webhook dispatcher **expired**. The automated certificate renewal job had been silently failing for 3 weeks because of a permissions change, and no alert was configured for it.

## Timeline (UTC)

- 13:05: certificate expires; dispatcher starts failing all outbound requests.
- 13:19: `WebhookDeliveryFailureRate` alert fires.
- 13:31: root cause identified.
- 13:48: new certificate deployed.
- 13:52: delivery fully recovered; retry backlog cleared by 14:40.

## Action items

1. Add an alert for certificates expiring within **14 days**. (Done)
2. Alert when the renewal job fails. (Done)
3. Add a status-page template for webhook-only incidents. (In progress)
