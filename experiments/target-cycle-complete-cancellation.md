# Target-cycle complete insertion-cancellation diagnostic

Run

```text
python scripts/check_target_cycle_complete_cancellation.py \
  experiments/target-cycle-complete-cancellation-example.json
```

The first cycle has length twelve and removal credit twelve.  Its insertion table
has total multiplicity 1,000, so the first trade alone increases the potential by
988.

The second strictly alternating trade moves every first-cycle inserted cell.  It
has zero insertion cost and destroys all 1,000 first-step insertion incidences.
The two-step package therefore changes the potential by

```text
(1000-12)+(0-1000)=-12.
```

The exact output is

```text
cycle length 12
first removal credit 12
first insertion cost 1000
first-step change 988
second insertion cost 0
destroyed first insertion 1000
second-step change -1000
composite change -12
reduced composite bound -12
outcome target_cycle_complete_insertion_cancellation
```

This verifies PP3arx--PP3asa: arbitrary first-cycle insertion multiplicity cancels
against the second removal term, leaving exactly the negative first-cycle credit in
the zero-cost second-host branch.
