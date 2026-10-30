---
doc_title: API Error Codes Reference
doc_type: error_reference
source_url: https://docs.nimbuspay.example/api/errors
updated_at: 2026-09-02
allowed_groups: [support, engineering]
---

# API Error Codes Reference

All NimbusPay API errors return a JSON body with `code`, `message` and `request_id`. Always include the `request_id` when escalating to engineering.

## 4xx errors (problem with the request)

### ERR-4001: Invalid API key
The API key is missing, malformed or revoked. Check that the merchant is using a **live** key (`sk_live_...`) in production and a **test** key (`sk_test_...`) in the sandbox. Mixing them up is the most common cause.

### ERR-4003: Permission denied
The API key is valid but lacks permission for this action. Restricted keys must be granted the needed scope in Dashboard → Developers → API keys.

### ERR-4012: Bank account verification failed
NimbusPay could not verify the merchant's payout bank account. The most common cause is that the **account holder name does not match the legal business name** on the merchant's NimbusPay profile. Other causes: closed account, wrong routing number, or the bank rejected the micro-deposit check.

What to do:
1. Ask the merchant to confirm the account holder name matches their legal business name exactly.
2. Have them re-enter the bank details in Dashboard → Settings → Payouts.
3. If it fails again, escalate to the Payouts team with the `request_id`.

Payouts are paused until the bank account is verified.

### ERR-4029: Rate limit exceeded
The merchant sent more than **100 requests per second** in live mode (25 per second in test mode). Advise exponential backoff and retry.

### ERR-4091: Duplicate idempotency key
The same `Idempotency-Key` header was reused with a different request body within 24 hours. Generate a new key per unique request.

## 5xx errors (problem on our side)

### ERR-5002: Upstream processor timeout
The card network or bank did not respond in time. The payment may still succeed. Tell the merchant **not to retry immediately**; check the payment status after 5 minutes.

### ERR-5031: Scheduled maintenance
The API is temporarily unavailable for maintenance. Maintenance windows are announced at least 72 hours in advance on the status page.
