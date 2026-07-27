# Signed Hamilton defect census through `m=8`

Compile and run:

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_signed_defect_census_m8.cpp \
  -o /tmp/check_hamilton_signed_defect_census_m8
/tmp/check_hamilton_signed_defect_census_m8
```

The checker precomputes exact collinear-triple contributions for every pair and
triple of signed orbit assignments.  Each signed Hamilton state is then scored
by table lookup rather than by rescanning all point triples.

| `m` | Hamilton cycles | signed states | minimum triples | valid states | cycles with a valid orientation |
|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 96 | 0 | 16 | 2 |
| 5 | 24 | 768 | 0 | 16 | 2 |
| 6 | 120 | 7,680 | 4 | 0 | 0 |
| 7 | 720 | 92,160 | 0 | 36 | 10 |
| 8 | 5,040 | 1,290,240 | 0 | 28 | 10 |

At `m=8`, six Hamilton cycles have exactly two valid orientations and four cycles
have exactly four.  One exact valid state is

```text
rho = [2,5,3,6,7,4,1,0],
e   = [1,0,0,1,1,0,0,0].
```

Every defect count in every audited distribution is divisible by four.  The C++
checker stores and verifies the complete defect-count distribution for each
`m=4,...,8`, not only the summary table above.

This is a finite census.  It does not prove a uniform descent horizon at `m=8`
or asymptotic existence.
