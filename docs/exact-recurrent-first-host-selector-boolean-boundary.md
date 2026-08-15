# First-host selector Boolean boundary gates

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact symbolic selector classification on the chart-safe background class. It does not prove physical restoration legality, persistent owner identity, or finite boundary capacities.

## Two-bit restoration context

Write

```text
r02=1 iff deletion edge 02 is restored
r20=1 iff deletion edge 20 is restored.
```

The four menu states and their canonical selected responses are

```text
(r02,r20)=(0,0)  blocked       -> 3012
(r02,r20)=(1,0)  restore 02    -> 2031
(r02,r20)=(0,1)  restore 20    -> 3201
(r02,r20)=(1,1)  restore both  -> 2031.
```

The selected-response predicates on the Boolean cube are therefore

```text
3012 current iff not r02 and not r20
2031 current iff r02
3201 current iff not r02 and r20.
```

These predicates are exact consequences of the chart-safe restoration selector-face theorem.

## Exact single-bit recreation gates

A symbolic response label is recreated when one single restoration bit changes and that label changes from nonselected to selected.

```text
3012:
  01 -> 00  delete 20
  10 -> 00  delete 02

2031:
  00 -> 10  restore 02
  01 -> 11  restore 02

3201:
  00 -> 01  restore 20
  11 -> 01  delete 02.
```

Thus the exact single-bit gate stock is

```text
3012 gates: 2
2031 gates: 2
3201 gates: 2
total:      6.
```

Four changing gates flip `r02`; two flip `r20`.

## Selector-neutral context edges

The two remaining directed edges of the restoration cube are

```text
10 -> 11  restore 20
11 -> 10  delete 20.
```

Both retain selected response `2031`. Hence the eight directed single-bit context edges split exactly into six selector-changing and two selector-neutral edges.

## Selected-label transition obstruction

Project each changing menu edge to its old and new selected-response labels. The six projected edges are

```text
3012 -> 2031
2031 -> 3012
3012 -> 3201
3201 -> 3012
2031 -> 3201
3201 -> 2031.
```

Thus the selected-label transition graph is the complete bidirected triangle. It has one strongly connected component containing all three labels and three directed two-cycles.

Consequently there is no scalar function depending only on the selected response label that strictly decreases on every one of the six symbolic selector-changing edges.

A strict scalar ordering can pay at most one direction from each unordered label pair, hence at most three of the six edges. Therefore at least three selector-changing gates must use a non-label-descent route:

```text
physical exclusion
richer-state strict progress
finite gate capacity
terminal or improving output
outer builder reset.
```

The full four-state restoration graph is also bidirected on each of its four cube edges. A scalar depending only on the menu state can strictly pay at most four of the eight directed menu edges, so at least four require a non-menu-descent route.

These are symbolic graph lower bounds. They do not prove that all six selector gates or all eight menu edges are physically legal or jointly realizable.

## Exact improvement over the generic Boolean bound

For three symbolic labels on two Boolean context bits, the generic alternating-core single-bit boundary bound is

```text
3 * J * 2^(J-1) = 3 * 2 * 2 = 12.
```

The exact selector predicates realize only six gates.

For arbitrary context jumps, the three exact false-to-true stocks have sizes

```text
3012: 3
2031: 4
3201: 3
total: 10,
```

compared with the generic three-label bound `3*2^(2J-2)=12`.

## Alternating-core import boundary

The alternating-core finite Boolean boundary theorem can therefore be instantiated **symbolically** with this exact six-gate stock. A recurrence or termination promotion still requires each gate to be attached to the same exact physical owner token and to satisfy at least one registered closure route.

None of those physical gate routes is currently populated. The repository has no proof that a response label such as `2031` denotes one persistent owner token across menu states, no legal transition trace, and no boundary capacity ledger.

Therefore

```text
symbolic Boolean boundary interface available   yes
strict selected-label-only potential             no
strict menu-state-only potential                  no
minimum non-label-descent selector routes         3
minimum non-menu-descent transition routes        4
physical owner-token gate identification         no
promotion to recurrent closure                   no.
```

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_selector_boolean_boundary.py \
  --check data/exact_recurrent_first_host_selector_boolean_boundary.json
```

The checker reconstructs the four menu states, all eight directed single-bit edges, the six exact recreation gates, the two neutral edges, the complete bidirected selected-label graph, both minimum non-descent route bounds, both exact gate-stock improvements, and rejects nineteen deliberate corruptions.

Physical chart confinement, occurrence coverage, operation legality, boundary capacities, recurrent child rows, strict Lyapunov slack, global termination, and `all_n_proved_by_checker` remain zero.
