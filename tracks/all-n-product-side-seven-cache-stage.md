# All-n product track: side-seven radius-three cache stage

**Branch:** `research/all-n-product-construction`

This stage classifies the `(5,2)` radius-three support-twenty layer of the canonical `[14]^2` host. It is a finite census, not an infinite closure theorem.

## Current exact ledger

The layer contains `71,860` selectors grouped into `38,553` top signatures. All selectors of multiplicity at least three are classified:

- `37,600` are infeasible in all four radix orientations;
- one multiplicity-four selector has a verified no-three embedding.

Multiplicity two contains `3,840` signatures and `7,680` selectors. Cases `0` through `719` are closed in seventy-two ten-signature proof units:

- `1,440` multiplicity-two selectors are certified infeasible;
- every shard has an ordered-transcript digest verifier;
- the prefix uses `307,371,264` shared bottom-CSP nodes.

The committed support-twenty boundary is:

- `39,040` certified-infeasible selectors;
- one constructive selector;
- `32,819` unclassified selectors;
- `3,073,826,508` certified rejection-CSP nodes.

The unresolved cache is exactly:

- `3,120` multiplicity-two signatures containing `6,240` selectors;
- all `26,579` multiplicity-one selectors.

An exact workflow is registered for cases `720` through `799`. It is not counted until every transcript is promoted.

## Exact finite proof units

The committed multiplicity-two family is:

- `multiplicity2_pilot10.cpp` for cases `0`--`9`;
- `multiplicity2_shard1.cpp` through `multiplicity2_shard71.cpp` for cases `10`--`719`.

Each wrapper asserts its tier, interval, both clean-top and top-node totals, all four bottom-CSP totals, and one ordered digest.

## Certificate compression and master learning

For case zero, orientation three, every one of 128 obligations through 64 top orders has a seven-triple cover. A 55-triple dictionary and 93 cover lists encode all 896 entries.

Two repeated-support studies now cover thirty references:

1. support `6975`: twelve references reduce to five actual keys and cover fourteen clean top orders;
2. supports `7487`, `11039`, `11071`, `11551`, `11583`: eighteen references reduce to sixteen keys and cover forty-seven clean top orders.

Both selectors always minimize to the same semantic mask in these groups, eliminating selector-union penalty. A combined census is measuring the true cross-group union of all 21 keys.

## Immediate tasks

1. Promote cases `720--799`, then continue the multiplicity-two census.
2. Finish the combined 30-reference semantic union.
3. Extend semantic deletion to unequal-support and singleton classes.
4. Select a compact top-master set-cover basis.
5. Defer multiplicity one until multiplicity-two proof size and symmetry are understood.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_next_equal.py

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1..71}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

The classical no-three-in-line conjecture and infinite product closure remain open.
