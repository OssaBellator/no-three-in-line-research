# SAS reserve-queue frontier

SAS5oa--SAS5od turns unfunded sparse repairs into a FIFO debt queue with explicit capacity, replenishment-window, origin and stale-lineage witnesses. Under the contracts, each head clears within `W` microsteps and cumulative admissions are bounded by initial neutral deficit plus sparse-move churn.

Remaining work: construct sparse replenishment, prove capacities/windows, revalidate queued jobs, and pay persistent orientation, legality, boundary or lineage shortages.