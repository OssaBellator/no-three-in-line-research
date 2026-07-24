# Complete width-two matching-reservoir cross patches

The parabolic constructions form a structured subfamily of a simpler finite
interface at width two.  This chapter classifies every patch that deletes one
point from each of four old columns and four old rows and refills the deficits
using only the two old/new cross rectangles.

## 1. Degree classification

Let `S subseteq [m]^2` be saturated.  Add two new rows

\[
 r_1=m+1,\qquad r_2=m+2
\]

and two new columns

\[
 c_1=m+1,\qquad c_2=m+2.
\]

Choose four old columns `C` and four old rows `Y`.  Let

\[
 D\subseteq S\cap(C\times Y)
\]

be a perfect matching between `C` and `Y`, so `|D|=4` and every coordinate in
`C union Y` occurs exactly once in `D`.

A **cross-only width-two replacement** inserts points only in

\[
 (C\times\{r_1,r_2\})
 \cup
 (\{c_1,c_2\}\times Y).
\]

### Proposition PP3au -- PROVED

Every cross-only replacement that fills all deficits and gives exactly two
points to each new row and column is obtained uniquely by:

1. choosing an ordered partition

\[
 C=C_1\sqcup C_2,
 \qquad |C_1|=|C_2|=2,
\]

and inserting `C_i x {r_i}`;

2. choosing an ordered partition

\[
 Y=Y_1\sqcup Y_2,
 \qquad |Y_1|=|Y_2|=2,
\]

and inserting `{c_i} x Y_i`.

For fixed `C,Y,D` there are exactly

\[
 \binom42^2=36
\]

such degree states.

#### Proof

Deleting the matching creates deficit one in every old coordinate of `C` and
`Y`.  Because old-column deficits may be filled only in the two new rows, each
old column must occur exactly once among the movement points.  Each new row
must contain exactly two points, so the four columns are partitioned into two
labelled pairs `C_1,C_2`.

The row argument is identical: every old row occurs once among the refill
points, and each new column receives exactly two, giving labelled pairs
`Y_1,Y_2`.  Conversely, any two such ordered partitions fill every old deficit
once and every new coordinate twice.  There are `binom(4,2)=6` choices for each
ordered partition. ∎

The inserted state always contains eight distinct points and the operation
changes the point count by `8-4=4=2t`.

## 2. Exact geometric criterion

Let `Q` be one of the 36 inserted states and put `X=S setminus D`.

### Corollary PP3av -- PROVED

The width-two matching patch is valid if and only if:

1. `Q` is internally no-three-in-line;
2. no point of `Q` lies on a secant through two points of `X`;
3. no pair of points of `Q` is collinear with a point of `X`.

#### Proof

The degree statement follows from PP3au.  The retained set `X` is no-three
because it is a subset of `S`.  Every possible final triple is therefore
internal to `Q`, has two retained points and one inserted point, or has one
retained point and two inserted points.  The three displayed conditions exclude
exactly those classes. ∎

This is a complete finite interface: there are no additional cross-only
width-two degree states hidden outside the ordered-partition list.

## 3. Exhaustive stored-corpus result

The script

```bash
python scripts/search_width_two_matching_patches.py \
  certificates/prime-patching-small.json
```

enumerates every four-column set, four-row set, perfect matching reservoir, and
all 36 ordered-partition states.  It first removes states with an internal
triple and then counts the two external certificate classes exactly.

### Proposition PP3aw -- PROVED BY EXHAUSTIVE FINITE CHECK

For every stored certificate with `4<=m<=10`, no cross-only width-two matching
patch is valid.  The exhaustive counts are:

| `m` | Matching reservoirs | Degree states | Internally clean states | Minimum external triples |
|---:|---:|---:|---:|---:|
| 4 | 4 | 144 | 20 | 2 |
| 5 | 25 | 900 | 149 | 2 |
| 6 | 105 | 3,780 | 969 | 1 |
| 7 | 295 | 10,620 | 3,686 | 1 |
| 8 | 660 | 23,760 | 9,813 | 3 |
| 9 | 1,287 | 46,332 | 22,555 | 4 |
| 10 | 2,275 | 81,900 | 43,539 | 5 |

Thus `80,731` internally clean states were checked and none cleared both
external certificate classes.  The side-six and side-seven minima are genuine
one-certificate near misses.

The result is finite and seed-specific.  It does not refute width-two matching
patches for other saturated no-three source configurations.  It does show that
neither the parabolic parameterization nor a different partition of the same
four-coordinate reservoirs can repair the current stored chain at width two.

## 4. Revised finite target

The one-certificate states isolate a precise preparation problem.  A source
trade that deletes or moves the final retained anchor or one endpoint of the
final blocker secant would turn the corresponding degree state into a valid
patch.  Consequently useful next experiments should expose the exact final
certificate and search for a protected local trade around its old points,
rather than continue enlarging the width-two partition family.
