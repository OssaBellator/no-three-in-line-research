# Fixed-template secant-shadow diagnostic

Run

```text
python scripts/check_fixed_template_secant_shadow.py \
  experiments/fixed-template-secant-shadow-example.json
```

The stored tentative state has six internally no-three old-grid cells.  Its fifteen
secants cast a shadow of 25 cells on the tied `6 x 6` endpoint rectangle.

The initial selected permutation layer consists entirely of bad retained witnesses:

```text
initial selected bad witnesses 6.
```

With the same opposite source layer, a second saturated no-three permutation uses four
secant-clean replacements and only two bad replacements.  The complete source shadow
count changes from

```text
10 to 6,
```

so the fixed-template witness potential decreases by four.

The nonaxis secant traces have sizes

```text
2, 3, 4, and 6,
```

with only one full nonaxis trace, consistent with PP3ayn.

The expected output is

```text
endpoint side 6
template size 6
template secant lines 15
axis secant lines 5
nonaxis secant lines 10
nonaxis trace-size counts [(2, 3), (3, 5), (4, 1), (6, 1)]
full nonaxis traces 1
secant-shadow cells 25
initial selected bad witnesses 6
final selected bad witnesses 2
secant-clean replacements 4
full-source shadow count before 10
full-source shadow count after 6
exact shadow change -4
outcome fixed_template_secant_shadow_descent
```

This verifies the exact simple-shadow identity in PP3ayh and exhibits the clean-arc
strict-descent mechanism of PP3ayj in a pair of genuine saturated no-three sources.
