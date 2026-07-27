# Repair owner-cover and derangement-cycle diagnostic

Run:

```bash
python scripts/check_repair_owner_cover_and_derangement_cycles.py \
  experiments/p37-swapped-quarter-turn-near-example.json \
  experiments/p41-swapped-quarter-turn-near-example.json
```

The checker reconstructs every four-cell signed orbit block, identifies the
unique orbit owner of each bad-line cell, verifies collinearity, and confirms
that the owner multiset is invariant around each stored quarter-turn bad-line
orbit.

For the audited near-states it obtains:

```text
p=37: owner multiset {3:1,15:1,17:1}, minimum covers {3},{15},{17}
p=41: owner multiset {15:1,18:1,20:1}, minimum covers {15},{18},{20}
```

At support thirteen the owner filter leaves:

```text
p=37:  8,463 support subsets
p=41: 75,140 support subsets
```

For a fixed exact support of size `k`, the changed target map is a derangement
of that support.  The checker verifies the subfactorial recurrence and the
cycle-type formula through `k=13`.  In particular:

```text
13!  = 6,227,020,800
!13  = 2,290,792,932
13!/!13 = 2.718281828538486
```

There are only `24` possible cycle partitions of a support-thirteen
derangement.  The single thirteen-cycle class contains `12! = 479,001,600`
derangements.

The diagnostic validates exact combinatorial reductions.  It does not claim a
support-thirteen repair for `p=41` and does not prove the asymptotic seed
theorem.
