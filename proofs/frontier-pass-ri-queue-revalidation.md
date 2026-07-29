# RI frontier pass: queue revalidation

- Proved RI5hy--RI5ib.
- Added complete-footprint persistence for queued repairs.
- Bounded revalidation work by `H eta` per macro edit.
- Preserved debt identity and FIFO priority under signature refresh.
- Converted repeated head interruption into a quantified repeatedly touched footprint primitive.
- Added `scripts/verify_ri_queue_revalidation.py`.

Remaining RI6 work: concrete arithmetic footprints, numerical multiplicity bounds, and payment/reset from repeated-touch certificates.
