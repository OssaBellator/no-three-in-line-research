# Width-two matching-first spread and external defects

PP3bs supplies a spread four-edge matching reservoir, and PP3bu supplies its
canonical adjacent-pair replacement.  This chapter computes the resulting cell
and pair spread and isolates the retained-pair blocker class as the only defect
that can grow with the source side.

## 1. The canonical random rung

Fix a decomposition `S=P_0 dotcup P_1` into two perfect matchings.  Choose a
layer `J` uniformly, choose four of its `m` edges uniformly, and call the chosen
matching `D`.  Sort its four column endpoints and row endpoints and insert the
adjacent-pair state from PP3bt.

Conditional on either layer, the selected columns are a uniform four-subset of
`[m]`.  The selected rows are also a uniform four-subset, although the two sets
are correlated through the chosen perfect matching.

### Proposition PP3bv -- PROVED

For the canonical random rung:

1. every prescribed movement or refill cell has probability at most

\[
 \boxed{\frac4m};
\]

2. every prescribed pair of movement cells, and every prescribed pair of refill
   cells, has probability at most

\[
 \boxed{\frac{12}{m(m-1)}};
\]

3. let one prescribed movement cell use old column `x` and one prescribed refill
   cell use old row `y`.  Their joint probability is at most

\[
 \begin{cases}
 \displaystyle
 \frac2m+\frac6{m(m-1)}, & (x,y)\in S,\\[6pt]
 \displaystyle
 \frac{12}{m(m-1)}, & (x,y)\notin S;
 \end{cases}
\]

4. if `(x,y) in S` and that same source point is additionally required to remain
   undeleted, then the joint probability of the two prescribed cross-component
   cells and the retained anchor is at most

\[
 \boxed{\frac6{m(m-1)}}.
\]

All bounds remain true after imposing the rank conditions that determine whether
an old coordinate is placed on the first or second new line.

#### Proof

A prescribed component cell requires its old coordinate to belong to the
uniform four-subset, giving probability `4/m`.  Two same-component cells require
two specified old coordinates, giving `(4)_2/(m)_2=12/(m(m-1))`.

For a cross-component pair, fix the chosen layer `P_j` and let `x_j` be the
column whose layer edge has row endpoint `y`.  The pair requires both `x` and
`x_j` among the four selected columns.  If `x=x_j`, the probability is `4/m`;
otherwise it is `12/(m(m-1))`.  At most one of the two layers contains the source
point `(x,y)`.  Averaging over the two layers gives the third assertion.

Now suppose `(x,y)` is itself the proposed retained anchor.  In the layer that
contains `(x,y)`, selecting old column `x` selects and deletes that source edge,
so the anchor cannot remain.  In the other layer the two required columns are
distinct, giving probability `12/(m(m-1))`, multiplied by the layer probability
`1/2`.  Rank restrictions can only reduce these probabilities. ∎

The fourth assertion is the main benefit of choosing the matching before the
geometry.  The apparent `O(1/m)` source-edge spike cancels in the exact
deletion-aware anchored-triple event.

## 2. Deterministic external-defect split

Let `Q` be one canonical adjacent-pair rung and `X=S setminus D` its retained
core.

### Proposition PP3bw -- PROVED

1. The vertical old-column blocker through each movement cell and the horizontal
   old-row blocker through each refill cell are automatically destroyed by `D`.
2. The number of retained-anchor triples containing two points of `Q` is at most

\[
 \boxed{48}.
\]

3. Every remaining retained-pair blocker is nonaxis.  For each fixed inserted
   cell its source secants form a matching on `S`, so at most `m-1` nonaxis
   blocker pairs exist before the four-point deletion is applied.

#### Proof

A movement cell lies in one selected old column.  The two source points in that
column form its vertical axis blocker, and the matching reservoir deletes one of
them.  The refill statement is symmetric.

Among the `binom(8,2)=28` inserted pairs, two horizontal pairs inside the movement
component and two vertical pairs inside the refill component lie wholly on new
axis lines and contain no old anchor.  There are therefore at most `24` relevant
inserted pairs.  A line through one such pair contains at most two source points,
because `S` is no-three-in-line.  Hence at most `48` retained-anchor triples
occur.

For an external point, secant pairs of a no-three set form a matching: two pairs
through the point cannot share a source endpoint.  There are at most `m` pairs
on the `2m` source points.  Removing the automatic axis pair leaves at most
`m-1` nonaxis pairs. ∎

Thus the anchored-pair defect is uniformly bounded, while the nonaxis
retained-pair blocker class is the only part that can have order `m` for one
width-two rung.

## 3. Corpus experiment

The script

```bash
python scripts/analyze_matching_first_width_two.py \
  certificates/prime-patching-small.json
```

enumerates every layer-labelled four-edge reservoir from PP3bs, inserts the
canonical state PP3bt, and counts the two external certificate classes exactly.

The stored certificates have no raw clean canonical rung.  Their best states
are:

| Source | States | Minimum total defects | Best blocker count | Best anchor count |
|---:|---:|---:|---:|---:|
| 4 | 2 | 3 | 0 | 3 |
| 5 | 10 | 4 | 2 | 2 |
| 6 | 30 | 1 | 0 | 1 |
| 7 | 70 | 6 | 4 | 2 |
| 8 | 140 | 6 | 4 | 2 |
| 9 | 252 | 8 | 7 | 1 |
| 10 | 420 | 5 | 5 | 0 |

The side-six bank contains a one-anchor near miss, while the side-ten bank
contains states with no retained-anchor defect at all.  The changing minimum is
consistent with PP3bw: the growing obstruction is the retained-pair blocker
class, not internal geometry or a large anchored-pair population.

## 4. Revised asymptotic target

For matching-first width-two rungs, exact matching availability, internal
geometry, cell spread, and same-component pair spread are closed.  A preparation
theorem may now focus on either:

1. selecting four-edge reservoirs whose eight inserted cells have small nonaxis
   secant shadow in the retained core;
2. installing protected trades that hit those nonaxis blocker pairs;
3. grouping many candidate reservoirs into a multistate variable so that blocker
   bad boxes pass PP3bj or PP3bk;
4. combining ordered width-two rungs so reverse ordering controls their
   inter-rung triples.

The matching-first route therefore replaces a rare perfect-matching event by a
concrete secant-shadow minimization problem over a hypergeometric reservoir
bank.