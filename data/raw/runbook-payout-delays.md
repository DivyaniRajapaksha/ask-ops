---
doc_title: Runbook - Payout Delays
doc_type: runbook
source_url: https://wiki.nimbuspay.example/eng/runbooks/payout-delays
updated_at: 2026-08-27
allowed_groups: [engineering]
---

# Runbook: Payout Delays

Use this runbook when the `PayoutQueueLagHigh` alert fires, or when support reports many merchants with late payouts.

## 1. Check the scope

- Open the **payout-queue** dashboard in Grafana.
- If queue lag is above **15 minutes**, this is an incident. Open an incident channel and page the Payouts on-call.
- If only one merchant is affected, it is probably not a platform problem. Check whether their payout is in `PENDING_REVIEW` (a Risk hold, not an outage).

## 2. Check the banking partner

- Look at the banking partner status page and the `bank-gateway` error rate.
- A spike of `ERR-5002` (upstream timeout) means the partner is slow. Do **not** manually retry payouts; the gateway retries automatically up to 5 times.

## 3. Check the payout worker

- Confirm the `payout-worker` deployment has all replicas healthy.
- If workers are crash-looping after a deploy, roll back to the previous release.

## 4. Communicate

- Post an update on the public status page within **30 minutes** of declaring an incident.
- Give support a short customer-facing message. Never share internal service names with merchants.

## 5. After recovery

- Confirm the queue lag is back under 2 minutes for 30 minutes.
- Write a postmortem within **5 business days** for any incident longer than 30 minutes.
