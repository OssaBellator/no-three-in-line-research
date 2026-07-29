# GC reserve-queue frontier

GC2nb--GC2ne turns unfunded cleaning repairs into an explicit FIFO debt queue. Oversized repairs, replenishment-window failures, stale chart/height signatures and repair-certificate failures are now distinct. Under the contracts, each head clears within `W` microsteps and cumulative admissions are bounded by initial donor deficit plus support-local cleaning churn.

Remaining work: construct geometric replenishment, prove capacities/windows, revalidate queued repairs, and pay persistent chart or protected-height shortages.