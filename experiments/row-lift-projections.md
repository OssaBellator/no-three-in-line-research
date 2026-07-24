# Row-lift projection-dispersion experiments

These finite checks use
[`scripts/analyze_row_lift_projections.py`](../scripts/analyze_row_lift_projections.py)
and the necessary PP3u projection condition from
[`docs/33-off-diagonal-reservoir-obstruction.md`](../docs/33-off-diagonal-reservoir-obstruction.md).

## Exhaustive two- and three-row screen

For every stored certificate with `2<=n<=10`, every reservoir-row subset of
size `t in {2,3}` was tested over all primitive nonaxis coefficient pairs with

\[
1\le a\le n+t,
\qquad
|b|\le n+t.
\]

The results are:

| `n` | `t` | Row subsets | Passing PP3u screen | Minimum projection levels |
|---:|---:|---:|---:|---:|
| 2 | 2 | 1 | 0 | 3 |
| 3 | 2 | 3 | 3 | 4 |
| 3 | 3 | 1 | 0 | 5 |
| 4 | 2 | 6 | 6 | 4 |
| 4 | 3 | 4 | 4 | 6 |
| 5 | 2 | 10 | 10 | 5 |
| 5 | 3 | 10 | 10 | 6 |
| 6 | 2 | 15 | 15 | 5 |
| 6 | 3 | 20 | 20 | 7 |
| 7 | 2 | 21 | 21 | 6 |
| 7 | 3 | 35 | 35 | 7 |
| 8 | 2 | 28 | 28 | 6 |
| 8 | 3 | 56 | 56 | 8 |
| 9 | 2 | 36 | 36 | 6 |
| 9 | 3 | 84 | 84 | 8 |
| 10 | 2 | 45 | 45 | 5 |
| 10 | 3 | 120 | 120 | 9 |

Exactly two reservoirs fail:

- the complete side-two reservoir, with failing direction `(a,b)=(1,1)` and
  only `3=2t-1` sum levels;
- the complete side-three reservoir, with the same direction and only
  `5=2t-1` sum levels.

These are precisely the aligned interval configurations classified by PP3v.

## Interpretation

The earlier exhaustive bank search found no clean full row-lift state for any
of the two- and three-row reservoirs in this table. The projection test explains
only the two complete aligned cases. Every other failed bank occupies at least
`2t` level sets in every tested primitive direction, so no single parallel-line
family forces a triple by pigeonhole.

Thus most small row-lift failures are caused by simultaneous certificate
concentration across several directions or layer assignments, exactly the
phenomenon measured by PP3p, PP3q, and PP3r. Projection dispersion is a useful
fast rejection test, but it is not a sufficient geometric preparation theorem.