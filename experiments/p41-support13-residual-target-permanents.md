# Exact p=41 support-thirteen residual target permanents

Compile and run:

```bash
g++ -O3 -std=c++17 \
  scripts/check_p41_support13_residual_target_permanents.cpp \
  -o /tmp/check_p41_support13_permanents

/tmp/check_p41_support13_permanents
```

For each of the `75,140` owner-feasible supports of size thirteen, the checker
removes the old orbit blocks on that support and constructs a `13 x 13` matrix.
Rows are changed sources and columns are old-target owners.  The diagonal is
zero.  An entry is:

```text
0, 1, or 2
```

according to the number of canonical orientations that individually avoid all
retained orbit blocks and fit every residual maximal-line capacity.

The permanent of the binary support of this matrix counts target derangements
surviving every one-edge residual test.  The weighted permanent counts signed
target/orientation choices surviving those same individual tests.  Neither
permanent enforces duplicate orbit blocks between two changed assignments or
joint line-capacity interactions among changed blocks.

Exact aggregate:

```text
owner-feasible supports                    75,140
zero binary permanent                           8
positive binary permanent                  75,132
minimum positive permanent                  6,270
maximum permanent                     779,891,623
total binary permanent              2,356,482,881,132
total weighted permanent          178,613,770,154,696
```

The eight zero-permanent supports are stored in
`p41-support13-residual-target-permanents.json`.  The minimum is attained at

```text
{1,2,4,5,6,8,9,10,14,17,18,19,20}
```

and the maximum at

```text
{1,3,5,6,7,9,11,14,15,16,17,18,19}.
```

Before one-edge residual filtering, the owner-feasible outer space contains

```text
75,140 * !13 = 172,130,180,910,480
```

target derangements.  Therefore the exact binary survival fraction is

```text
2,356,482,881,132 / 172,130,180,910,480
= 0.013690120283772545....
```

The weighted signed survival fraction relative to the crude `2^13` orientation
upper bound is

```text
0.00012666830781364404....
```

This is an exact one-edge residual census.  It does not prove support-thirteen
infeasibility and does not produce a `p=41` seed.
