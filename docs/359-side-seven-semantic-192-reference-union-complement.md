# Side-seven semantic 192-reference union complement

This chapter measures how much of the complete clean-top family is reached by the first 192 relaxed semantic references for multiplicity-two case zero, orientation three.

## PX1167 — complete clean-top family size

The exact top enumerator contains `35,112` clean top orders in orientation three and uses `97,189` enumeration nodes.

The 150-key semantic vocabulary from the first 192 references covers exactly 204 of those orders.

## PX1168 — uncovered complement

Therefore the current semantic union leaves

```text
35,112 - 204 = 34,908
```

clean top orders uncovered. Its coverage fraction is exactly

```text
204 / 35,112 = 17 / 2,926
```

which is about 0.581%.

This changes the compression priority. The 115-key irredundant basis is useful inside the measured union, but expanding the union is the dominant task: 34,908 clean top orders remain outside it.

GitHub Actions run `30359535550` compiled and executed the exact complement verifier.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_union_complement192.cpp \
  -o /tmp/verify-semantic-complement192
/tmp/verify-semantic-complement192
```
