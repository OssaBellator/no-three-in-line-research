# AC synchronized reserve-queue frontier

AC5gx--AC5ha adds seven typed FIFO repair queues with no cross-ledger borrowing. Oversized jobs, persistent replenishment-window shortages, stale signatures and repair-certificate failures are distinct. Under the contracts, total first admissions are bounded by initial synchronized deficit plus physical churn, and a frozen state drains within `W_* Delta_0` repair microsteps.

Remaining work: construct track replenishment, prove capacities and windows, revalidate queued jobs across macro changes, convert typed shortages into payment/reset/descent, and combine finite queue drain with macro-state recurrence.