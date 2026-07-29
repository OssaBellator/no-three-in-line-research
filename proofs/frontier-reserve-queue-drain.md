# RI reserve-queue frontier

The new block RI5hu--RI5hx converts typed reserve insufficiency into an explicit FIFO debt process. Capacity, replenishment-window, queue-origin and epoch-signature failures are now separate witnesses. Under the stated contracts, a frozen-state repair queue drains in at most `W` microsteps per job, and cumulative admitted jobs are bounded by initial collateral deficit plus support-local churn.

Remaining physical obligations: construct the arithmetic replenishment mechanism, prove concrete capacities and windows, revalidate jobs across macro edits, and pay persistent shortages.