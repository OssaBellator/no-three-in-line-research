# BDA reserve-queue frontier

BDA5id--BDA5ig turns unfunded restoration repairs into an explicit FIFO debt queue. Capacity, replenishment-window, origin and stale-signature failures are separated. Under the queue contracts, each head clears within `W` microsteps, a finite queue drains within `nW`, and cumulative admissions are bounded by initial potential deficit plus support-local churn.

Remaining work: construct restoration replenishment, prove capacities and windows, revalidate jobs after macro edits, and pay persistent rational-gain shortages.