# Exact switching shell after one quartic bridge

PX109 classifies every overlapping trade after two adjacent root-square moves.
Apply one of the four bridges.  The resulting mapping differs from the affine
root on nine rows and is the first state outside every disjoint root-square
packing cube.

This chapter determines its complete one-step PX98 neighbourhood.

Normalize

\[
F(x)=ix,
\qquad i^2=-1,
\]

and put

\[
S=C_4=\{1,i,-1,-i\},
\]

\[
T=(1+i)C_4.
\]

Apply the root trades on \(S\) and \(T\), followed by the bridge with support

\[
U=\{0,1,i,1+i\}.
\]

Call the final mapping \(G\), and put

\[
W=S\cup T\cup\{0\}.
\]

Thus \(|W|=9\).  The bridge changes all nine rows relative to \(F\).

## Theorem PX112 -- PROVED

For every prime \(p\equiv1\pmod4\) with \(p\ge13\), every PX98 trade support
available at \(G\) is exactly one of the following.

1. The support \(U\), which reverses the bridge and returns to the two-square
   packing state.
2. An affine-square block of the root design \(\mathcal B_i\) which is disjoint
   from \(W\).

There are no other supports meeting the nine-row nonlinear core.

### Proof

On \(W\), the normalized bridge state has the exact values

\[
\begin{array}{c|c}
x&G(x)\\
\hline
0&1-i\\
1&1\\
i&-i\\
1+i&0\\
-1&i\\
-i&-1\\
-1-i&-1+i\\
-1+i&1+i\\
1-i&-1-i.
\end{array}
\]

Outside \(W\), one has \(G(x)=ix\).

Write a prospective ordered trade support as

\[
x_0,\quad x_1,\quad x_2,\quad x_3=x_1+x_2-x_0.
\]

As in PX109, the PX98 conditions are the three linear equations

\[
G(x_1)-G(x_0)=x_0-x_2,
\]

\[
G(x_2)-G(x_0)=x_1-x_0,
\]

\[
G(x_3)-G(x_0)=x_1-x_2.
\]

Choose which ordered roles lie in \(W\), assign distinct values from the
nine-row table to those roles, and use \(G(x)=ix\) on the remaining roles.
Exact Gaussian elimination gives:

| Number of prescribed \(W\)-roles | Ordered assignments | Algebraic solutions | Exact-intersection solutions |
|---:|---:|---:|---:|
| 1 | 36 | 0 | 0 |
| 2 | 432 | 0 | 0 |
| 3 | 2,016 | 4 | 0 |
| 4 | 3,024 | 4 | 4 |

In the four apparent three-role solutions, the computed fourth row also lies in
\(W\), so none has exact intersection size three.  The four full-intersection
solutions are the four parameter representations of the same support

\[
U=\{0,1,i,1+i\}.
\]

They reverse the bridge.

If a support is disjoint from \(W\), all four values agree with the affine root.
The PX98 supports of an affine root are exactly the affine-square blocks from
PX103--PX104.  Conversely every root block disjoint from \(W\) remains
available because its four values are unchanged.  This proves the
classification. \(\square\)

The elimination uses Gaussian constants of bounded norm.  Direct reduction
shows that no new solution occurs in any characteristic \(p\ge13\).

## 2. Exact degree

Let

\[
M_j
=
\#\{B\in\mathcal B_i:|B\cap W|=j\}.
\]

### Theorem PX112a -- PROVED

For every prime \(p\equiv1\pmod4\) with \(p\ge29\),

\[
\boxed{
M_4=6,
\qquad
M_3=4,
\qquad
M_2=60,
\qquad
M_1=9p-165,
}
\]

and

\[
\boxed{
M_0
=
\frac{p^2-37p+380}{4}.
}
\]

Consequently the exact switching degree of the bridge state is

\[
\boxed{
1+M_0
=
\frac{p^2-37p+384}{4}.
}
\]

At the two smaller admissible primes the exact profiles are

\[
\begin{array}{c|ccccc|c}
p&M_0&M_1&M_2&M_3&M_4&\deg(G)\\
\hline
13&1&0&12&20&6&2\\
17&2&12&36&12&6&3.
\end{array}
\]

### Proof

The six blocks contained in \(W\) are the parent blocks \(S,T\) and the four
PX108 bridge supports.  A finite Gaussian-affine enumeration of triples in
\(W\) gives exactly four further root blocks meeting \(W\) in three points for
all characteristics outside \(13\) and \(17\); no other four-point block is
contained in \(W\).  Hence \(M_4=6\) and \(M_3=4\) for \(p\ge29\).

Use the design moment identities from PX104:

\[
\sum_j M_j=\frac{p(p-1)}4,
\]

\[
\sum_j jM_j=9(p-1),
\]

and

\[
\sum_j\binom j2M_j
=3\binom92
=108.
\]

Substitution of \(M_3=4\) and \(M_4=6\) gives

\[
M_2=60,
\qquad
M_1=9p-165,
\]

and then

\[
M_0
=
\frac{p(p-1)}4-(M_1+M_2+M_3+M_4)
=
\frac{p^2-37p+380}{4}.
\]

PX112 adds the one reverse bridge to the \(M_0\) disjoint root-square trades.
The exceptional profiles at \(13\) and \(17\) follow from the same exact finite
intersection calculation. \(\square\)

## 3. Frozen core

The reverse bridge support \(U\) contains four of the nine changed rows.  Every
other available trade is disjoint from all nine.  Therefore the five rows

\[
W\setminus U
\]

are untouched by every one-step trade at \(G\).

This is the first exact frozen-core phenomenon in the strong-complete switching
system.  It is not an isolated vertex: PX112a gives quadratic total degree and
PX110 gives linearly many exits for every affine-exterior edge.  The freezing
is confined to altered edges in a constant-size nonlinear core.

To move one of those five edges, a path must first add one or more disjoint
root-square trades and then activate another bridge.  The next flow problem is
therefore an unlocking theorem for finite nonlinear cores, not a global
minimum-degree theorem.

## 4. Verification

Run

```bash
python scripts/verify_product_exact_bridge_state_shell.py
```

The verifier constructs the bridge state at primes \(13,17,29,37,41,53\),
checks the complete trade classification, reproduces the exceptional profiles,
and verifies the exact degree formula from prime 29 onward.
