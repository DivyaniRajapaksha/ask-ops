---
doc_title: Settlement and Reconciliation (Finance Internal)
doc_type: runbook
source_url: https://wiki.nimbuspay.example/finance/settlement-reconciliation
updated_at: 2026-09-18
allowed_groups: [finance]
---

# Settlement and Reconciliation (Finance Internal)

**Internal only. Do not share with merchants or support.**

## Daily settlement file

The processor settlement file arrives every day at **06:00 UTC** in the `finance-settlements` bucket. The reconciliation job compares it with NimbusPay's internal ledger and finishes by 07:30 UTC.

## Mismatch handling

- Differences under **$50** per merchant per day are auto-written off to the `recon-variance` account.
- Differences of **$50 or more** create a ticket in the Finance Ops queue and must be resolved within **2 business days**.
- If the total daily variance across all merchants is above **$10,000**, page the on-call Finance lead.

## Rolling reserves

High-risk merchants (dispute rate above 1%, or flagged by Risk) have a **rolling reserve of 10%** of each settlement, held for **90 days**. Reserved funds are released automatically on day 91.

Reserve percentage changes require approval from the Head of Risk.

## Month-end close

Month-end close starts on the **3rd business day** of the following month. No manual ledger adjustments are allowed after close without CFO sign-off.
