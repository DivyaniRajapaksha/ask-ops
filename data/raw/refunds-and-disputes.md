---
doc_title: Refunds and Disputes
doc_type: policy
source_url: https://docs.nimbuspay.example/payments/refunds-disputes
updated_at: 2026-06-30
allowed_groups: [support, finance]
---

# Refunds and Disputes

## Refunds

A refund is when the **merchant** chooses to return money to a customer.

- Refunds can be issued up to **180 days** after the original payment.
- Partial refunds are allowed; multiple partial refunds can be issued until the full amount is returned.
- The customer sees the money in **5–10 business days**, depending on their bank.
- NimbusPay's processing fee on the original payment is **not returned** when a refund is issued.
- If the merchant's balance is too low to cover a refund, the refund stays `PENDING` until the balance is topped up.

## Disputes (chargebacks)

A dispute is when the **customer** asks their bank to reverse a payment. The merchant does not choose this.

When a dispute is opened:
1. The payment moves to `DISPUTED`.
2. The disputed amount plus a **dispute fee** is withdrawn from the merchant's balance (see Fees and Pricing).
3. The merchant has **7 calendar days** to submit evidence in Dashboard → Disputes.

### What evidence helps?

- Proof of delivery (tracking number, signed receipt).
- Customer communication showing they received the product.
- Refund policy shown to the customer at checkout.

### Outcomes

- **Won**: the disputed amount and the dispute fee are returned to the merchant.
- **Lost**: the amount stays with the customer and the dispute fee is not returned.
- If the merchant does not respond within 7 days, the dispute is **automatically lost**.

## Refund vs dispute: which is better for the merchant?

If the customer's complaint is valid, refunding early is cheaper than losing a dispute, because a refund has no dispute fee and does not count toward the merchant's dispute rate.
