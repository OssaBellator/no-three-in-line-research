# OP reserve-queue frontier

OP4ha--OP4hd turns unfunded quotient-phase repairs into a FIFO debt queue with typed capacity and replenishment-window witnesses. Under the contracts, each head clears within `W` microsteps and cumulative admissions are bounded by initial source deficit plus support-local phase churn.

Remaining work: construct quotient/action replenishment, prove capacities and windows, revalidate phase jobs, and pay persistent unit, valuation, holonomy or carry shortages.