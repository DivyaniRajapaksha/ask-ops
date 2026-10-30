---
doc_title: Payout Review Policy
doc_type: policy
source_url: https://docs.nimbuspay.example/payouts/review-policy
updated_at: 2026-07-21
allowed_groups: [support, finance]
---

# Payout Review Policy

A payout is the transfer of a merchant's available balance to their bank account. Some payouts are held for manual review to protect merchants and NimbusPay from fraud.

## When is a payout held?

A payout enters `PENDING_REVIEW` if any of these are true:
- It is the merchant's **first payout**.
- The payout amount is more than **3x the merchant's 30-day average** payout.
- The payout bank account was **changed in the last 72 hours**.
- The merchant's dispute rate is above **1%** in the last 30 days.

## Review timelines

Reviews take **up to 5 business days**. Most are completed within 2 business days. The merchant receives an email when the review is finished.

If a payout is still in `PENDING_REVIEW` after **5 business days**, support should escalate to the Risk team through the internal escalation form, with the payout ID (format `po_` followed by 24 characters).

## What can the merchant do to speed it up?

- Make sure KYC verification is complete (see KYC Verification Guide).
- Respond quickly if the Risk team asks for invoices or proof of delivery.
- Avoid changing bank details right before a large payout.

Support agents must **not** promise a specific release date. Use the wording: "Reviews usually complete within 2 business days and take no longer than 5."

## Outcomes

- **Approved**: the payout is sent on the next payout cycle.
- **Partially held**: part of the balance moves to a rolling reserve (see Settlement & Reconciliation, finance only).
- **Rejected**: the funds stay in the balance and the merchant is contacted by the Risk team.
