---
doc_title: Webhooks Guide
doc_type: reference
source_url: https://docs.nimbuspay.example/developers/webhooks
updated_at: 2026-04-02
allowed_groups: [support, engineering]
---

# Webhooks Guide

Webhooks let a merchant's server receive notifications when something happens in their NimbusPay account, such as a payment succeeding.

## Common events

| Event | When it is sent |
|---|---|
| `payment.succeeded` | A payment moved to `SUCCEEDED`. |
| `payment.failed` | A payment moved to `FAILED`. |
| `payout.paid` | A payout arrived in the merchant's bank. |
| `payout.held` | A payout entered `PENDING_REVIEW`. |
| `dispute.created` | A customer opened a chargeback. |

## Responding to webhooks

The merchant's endpoint must return an HTTP **2xx** status within **10 seconds**. Anything else counts as a failure.

## Retries

Failed deliveries are retried with exponential backoff for up to **3 days**. After that, the event is marked as failed and can be resent manually from Dashboard → Developers → Webhooks.

## Verifying signatures

Every webhook includes a `Nimbus-Signature` header. It is an **HMAC-SHA256** of the raw request body, signed with the endpoint's signing secret (starts with `whsec_`). Merchants must verify the signature before trusting the event, and reject events older than **5 minutes** to prevent replay attacks.

## Troubleshooting

- **Not receiving webhooks?** Check the endpoint URL is public HTTPS, not localhost.
- **Signature mismatch?** The merchant is probably verifying a parsed JSON body instead of the raw body.
- **Duplicate events?** Webhooks can be delivered more than once. Use the event `id` to ignore duplicates.
