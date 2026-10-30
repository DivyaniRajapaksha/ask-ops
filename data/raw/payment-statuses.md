---
doc_title: Payment Statuses Explained
doc_type: reference
source_url: https://docs.nimbuspay.example/payments/statuses
updated_at: 2026-08-12
allowed_groups: [support, engineering]
---

# Payment Statuses Explained

Every payment in NimbusPay moves through a series of statuses. This page explains what each status means and what a merchant should do.

## Status lifecycle

A typical successful card payment goes: `CREATED` → `PROCESSING` → `AUTHORIZED` → `SUCCEEDED`.

| Status | Meaning |
|---|---|
| CREATED | The payment object exists but the customer has not submitted payment details yet. |
| PROCESSING | Payment details were submitted and NimbusPay is waiting for the card network or bank to confirm. |
| AUTHORIZED | The bank approved the payment and the funds are reserved, but not yet captured. |
| SUCCEEDED | Funds were captured and will be included in the merchant's next settlement. |
| FAILED | The bank or NimbusPay declined the payment. See the `failure_code` field. |
| REFUNDED | All or part of the payment was returned to the customer. |
| DISPUTED | The customer opened a chargeback with their bank. |

## How long does PROCESSING last?

- **Card payments** usually leave `PROCESSING` within seconds and settle within **1–2 business days**.
- **Bank transfers (ACH, SEPA)** can stay in `PROCESSING` for **3–5 business days**. This is normal.
- **Wallet payments** (Apple Pay, Google Pay) behave like card payments.

If a **card** payment is still `PROCESSING` after **3 business days**, the merchant should contact NimbusPay support and include the transaction ID (format `txn_` followed by 24 characters). Do not ask the customer to pay again; this can cause a duplicate charge.

## AUTHORIZED but not captured

Authorizations expire after **7 days**. If the merchant does not capture the payment in that window, the funds are released back to the customer and the payment moves to `FAILED` with failure code `authorization_expired`.

## FAILED payments

A failed payment never moves money. Common failure codes:
- `card_declined`: the issuing bank refused the charge. The customer should contact their bank.
- `insufficient_funds`: the customer's account did not have enough balance.
- `authorization_expired`: see above.

For API errors (codes like `ERR-4012`), see the API Error Codes reference.

Was this article helpful? Yes / No
