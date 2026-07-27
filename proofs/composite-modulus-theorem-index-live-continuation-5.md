# Live composite-modulus theorem ledger continuation 5

The authoritative live ledger is split across:

- `composite-modulus-theorem-index-live.md` through CMR747;
- `composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `composite-modulus-theorem-index-live-continuation-2.md` through CMR1197;
- `composite-modulus-theorem-index-live-continuation-3.md` through CMR1629;
- `composite-modulus-theorem-index-live-continuation-4.md` through CMR1829; and
- this file from CMR1830 onward.

| IDs | Contents | Status | Location |
|---|---|---|---|
| CMR1830--1837 | Occupancy moments, uniform background-height compiler, exact height-layer identity, maximum line-occupancy distributions, third-moment distributions, denominator-specific side-four/five moment tables, and the occupancy-moment endpoint | PROVED; all 740 raw hosts, 89,664 host-line capacities, 1,188,144 response-line comparisons, 5,180 uniform-height bounds and 5,180 exact height-layer identities checked | `docs/332-prime-power-geometric-fibre-occupancy-moment-census.md` |
| CMR1838--1845 | Label linearization, weighted nested peeling, one weighted outer score, row Lyapunov criterion, simultaneous rational dual LP, rational/integer certificates, SCC/auxiliary assembly, and the labelled-LP endpoint | PROVED; 600 labelled systems, 4,645 response bounds, 4,645 label-linearization and outer-assignment checks, 600 rational duals and 600 denominator clearings checked | `docs/333-prime-power-label-weighted-unified-assignment-lp.md` |
| CMR1846--1853 | Full-length line classification, zero main-diagonal capacity, even and odd anti-diagonal laws, odd-side sharp construction, exact line-length occupancy census, side-four/five anti-diagonal distributions, and the diagonal-parity endpoint | PROVED; full-line classification through side twelve, parity checks through side eight, 28 odd-side constructions and all 89,664 raw host-line capacities checked | `docs/334-prime-power-diagonal-parity-line-occupancy-census.md` |

The branch still does not prove the all-`n` conjecture.

## Current exact certificate surfaces

### Occupancy moments and background-height classes

For every raw host, define

\[
M_r(G)=\sum_\ell\binom{\tau_G(\ell)}r,
\qquad r=1,2,3.
\]

If every relevant background line has load at most `H`, then

\[
\mathcal C_G(B)
\le
\binom H2M_1(G)+HM_2(G)+M_3(G).
\]

For a triple-free background this becomes

\[
E_2(G)=M_1(G)+2M_2(G)+M_3(G).
\]

Exact denominator-specific maxima of all four host scores are tabulated through
side five.  Nonuniform background heights retain the exact layer identity

\[
\mathcal C_G(B)
=
M_3(G)
+
\sum_{s\ge2}(s-1)
\sum_{\ell:h_\ell\ge s}\tau_G(\ell)
+
\sum_{s\ge1}
\sum_{\ell:h_\ell\ge s}\binom{\tau_G(\ell)}2.
\]

### Label-weighted final certificate LP

For proposed positive child weights `x_j`, aggregate every labelled primitive
coefficient before peeling.  For parent `i`, the weighted outer score is

\[
\gamma_i(e;x)
=
q_i(e;x)
+\frac12J_{2,i}(e;x)
+\frac16H_{3,i}(e;x).
\]

Every labelled row satisfies

\[
\sum_jA_{ij}x_j
\le
\mathcal A_{G_i}(\gamma_i(.;x)).
\]

All inner and outer assignment maxima may be replaced by dual variables.  Using
the sixfold score

\[
\Theta_i(e;x)=6q_i(e;x)+3j_{2,i}(e)+h_{3,i}(e),
\]

the constraints

\[
U_{i,u}+V_{i,v}\ge\Theta_i((u,v);x)
\]

and

\[
\sum_uU_{i,u}+\sum_vV_{i,v}
\le
6x_i-6\epsilon_i
\]

form a finite rational LP.  Every strict feasible point gives `Ax<x`; clearing
denominators gives a signed-integer assignment certificate with positive row
slacks.

### Diagonal parity

The only full-length nonaxis lines are the main and anti-diagonals.  The main
diagonal has response capacity zero.  For the anti-diagonal:

- even `d>=4`: the undeleted host has capacity `d`, and a raw host has capacity
  `d` exactly when its deletion trace misses the anti-diagonal;
- odd `d>=5`: every host has capacity at most `d-2`, and the undeleted host
  attains `d-2`.

Through side five the exact anti-diagonal distributions are:

| side | capacity distribution |
|---:|---|
| 4 | 11 hosts at 0, 40 at 2, 35 at 4 |
| 5 | 1 host at 0, 34 at 1, 67 at 2, 552 at 3 |

The full line-length/occupancy census is now exact for every one of the 740 raw
hosts.

## Active frontier

1. Attach actual background-height, owner and provenance classes to the 740 raw
   hosts and evaluate the exact height-layer or moment scores.
2. Populate the label-weighted LP with the actual return, selector, rank-one,
   rank-two and rank-three labelled coefficients.
3. Use exact rank-three numerators and diagonal capacities immediately; restrict
   new assignment work to shorter-line rank-one/rank-two data and corrected
   provenance routing.
4. Produce one strict assignment-dual row certificate for each surviving thin,
   fixed-interface and reused-support state.
5. Eliminate certified auxiliary modules through exact rational resolvents.
6. Certify the remaining collision/local-line SCCs, clear all denominators and
   publish the global integer quotient before applying CRT gluing.
