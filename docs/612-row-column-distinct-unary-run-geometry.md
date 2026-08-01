# Row-column-distinct unary-run geometry

`docs/606` separates coincident unary-run points but places each run on an
abstract vertical line, reusing a column.  This chapter gives a canonical greedy
integer embedding with globally distinct rows and columns and no cross-run
collinear triples.

## 1. Greedy run-line embedding

### Theorem PP3cvc -- PROVED / DISTINCT ROW-COLUMN RUN REALIZATION

For every ordered list of positive unary-run lengths, there is an integer point
embedding such that

- all point columns are distinct;
- all point rows are distinct;
- the points of each run are collinear; and
- every collinear triple lies entirely inside one run.

#### Proof

Process runs in order.  Give run `r` slope `r+1` and choose an integer intercept
whose line contains no earlier point.  On that line, skip every column already
used, every row already used, and every intersection with a line determined by
two earlier points.  Only finitely many values are forbidden, so enough integer
points remain for the run.

The new run line contains no earlier point, excluding triples with two new and
one old point.  Skipping all old pair-line intersections excludes triples with
one new and two old points.  Induction proves the claim. ∎

## 2. Complete profile audit

### Theorem PP3cvd -- PROVED / ALL UNARY-RUN COMPOSITIONS CHECKED

At encoded size thirty with nine binary nodes, there are exactly eleven unary
nodes.  The checker constructs the greedy embedding for all `2^10=1024` ordered
compositions of eleven.  Every embedding has distinct rows and columns and zero
cross-run triples.  In the chosen search order, all coordinates have absolute
value at most `113`.

#### Proof

The exhaustive composition generator lists every ordered positive composition of
eleven.  The checker runs the construction from `PP3cvc`, audits row and column
uniqueness, enumerates every point triple, and verifies that its run labels agree
whenever it is collinear. ∎

## 3. Exact tree-family census

### Theorem PP3cve -- PROVED / EXACT ROW-COLUMN-DISTINCT TRIPLE AGGREGATE

For the full thirty-node, nine-binary tree profile, the total number of collinear
triples in the canonical run embedding is exactly

```text
396499770810,
```

with mean

```text
33/14.
```

There are no extra cross-run triples.

#### Proof

A maximal unary run of length `r` contributes exactly `C(r,3)`.  The exact
unary-binary dynamic program carries the open top-run length and closes a run
when a binary root is attached.  It reconstructs the family size
`168212023980` and the displayed aggregate.  `PP3cvc--PP3cvd` show that these are
all geometric triples in the embedding, not merely a lower bound. ∎

## 4. Remaining source gap

The construction now respects distinct row and column resources and has an exact
ancestry-sensitive incidence census.  Its run lines are still canonical encoding
objects rather than support chords derived from the prime-patching source.  The
next decoder must identify these lines, or an equivalent incidence statistic,
with actual support events.
