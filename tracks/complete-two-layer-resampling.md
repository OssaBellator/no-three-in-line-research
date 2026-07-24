# Stationary resampling on two edge-disjoint complete matchings

SRR1a treats one perfect matching of \(K_{N,N}\). The exact-cover state
space for SRR3 consists of ordered pairs of edge-disjoint perfect
matchings. A four-cycle switch in one layer has only two possible
cross-layer obstructions, which can be removed while keeping the forward
degree constant.

Let

\[
\Omega_2=
\{(\pi,\rho):\pi,\rho:X\to Y\text{ bijections and }
\pi(x)\neq\rho(x)\text{ for every }x\}.
\]

Fix a labelled layer-one edge \(e=(i,j)\), and let

\[
A=\{(\pi,\rho)\in\Omega_2:\pi(i)=j\}.
\]

Assume \(N\geq4\). For a flawed state define

\[
b_1=\pi^{-1}(\rho(i)),
\qquad
b_2=\rho^{-1}(j).
\]

Both differ from \(i\). Swapping \(\pi(i)\) and \(\pi(u)\) preserves
edge-disjointness exactly when \(u\notin\{b_1,b_2\}\).

Choose a fixed ordering of \(X\). If \(b_1\neq b_2\), allow every row
outside \(\{i,b_1,b_2\}\). If \(b_1=b_2\), additionally discard the first
row outside \(\{i,b_1\}\). In both cases the allowed set has exactly

\[
L=N-3
\]

rows.

## SRR3a -- complete two-layer stationary oracle

### Theorem SRR3a -- PROVED

The selected layer-one four-cycle switches form a bipartite switching
graph between \(A\) and \(\Omega_2\setminus A\) with:

1. forward degree exactly \(N-3\) at every flawed state;
2. reverse degree at most one at every nonflawed state;
3. every switch preserving both perfect matchings and their
   edge-disjointness;
4. every forward switch removing \(e\);
5. symmetric difference equal to one four-cycle in the selected layer.

Consequently the balanced switching kernel of SRR1b is reversible and
stationary for the uniform measure on \(\Omega_2\), and it removes every
labelled forbidden partial matching containing \(e\). The same result
holds with the two layers exchanged.

### Proof

In a flawed state, \(\pi(i)=j\) and \(\rho(i)\neq j\), so
\(b_1,b_2\neq i\). After swapping the images of \(i\) and \(u\), the only
new possible cross-layer collisions are

\[
\pi(u)=\rho(i)
\quad\text{at row }i,
\qquad
j=\rho(u)
\quad\text{at row }u.
\]

These occur exactly at \(u=b_1\) and \(u=b_2\). The selected rows avoid
both, proving edge-disjointness. The canonical extra deletion when they
coincide makes the number of choices exactly \(N-3\).

No selected \(u\) carries \(j\) in \(\pi\), because row \(i\) is its
unique preimage. Thus the swapped layer avoids \(e\). Swapping two images
of one permutation preserves both permutation layers and changes exactly
the four edges of their alternating four-cycle.

Now fix a nonflawed output \((\pi',\rho)\). Any reverse switch introducing
\((i,j)\) must use the unique row

\[
u=(\pi')^{-1}(j).
\]

That row determines the predecessor by swapping \(i\) and \(u\), so there
is at most one reverse switching edge. SRR1b applies with
\(L=N-3\): a flawed state chooses each forward edge with probability
\(1/L\); a nonflawed state uses each reverse edge with probability
\(1/L\) and puts the remaining mass on its self-loop. The kernel is
symmetric, stochastic, stationary, and reversible.

If a labelled forbidden partial matching contains \(e\) in layer one,
removing \(e\) removes that event. Layer symmetry gives the other case.
\(\square\)

## SRR3b -- same-layer remote-event bound

Let \(F\) and \(B\) be compatible partial matchings in layer one of
ranks \(k\) and \(s\), respectively. Assume their row sets and column
sets are disjoint, \(F\) contains the distinguished edge \(e\), and
\(k+s\leq N\). Start the SRR3a forward oracle from the uniform measure on
\(\Omega_2\) conditioned on \(F\), and write \(M'_1\) for the resampled
first layer.

### Theorem SRR3b -- PROVED

The oracle cannot create \(B\) pathwise, and

\[
\boxed{
\Pr(B\subseteq M'_1\mid F\subseteq M_1)
\leq
\frac1{(N-k)_s}.
}
\]

Since the unconditioned layer-one marginal satisfies

\[
\Pr(B\subseteq M_1)=\frac1{(N)_s},
\]

the remote-event inflation relative to its stationary marginal is at
most

\[
\boxed{
\frac{(N)_s}{(N-k)_s}
=
\prod_{r=0}^{s-1}
\left(1+\frac{k}{N-k-r}\right)
\leq
\exp\!\left(\frac{ks}{N-k-s+1}\right).
}
\]

In particular, this is \(1+O(ks/N)\) for fixed event ranks.

### Proof

An SRR3a switch changes the first-layer edges at the distinguished row
\(i\) and at one partner row \(u\). Its two inserted edges have,
respectively, row \(i\) and column \(j\), where \(e=(i,j)\). Because
\(B\) uses neither a row nor a column of \(F\), neither inserted edge can
belong to \(B\). The switch may delete an edge of \(B\) when \(u\) is one
of its rows, but it cannot create one. Hence

\[
\mathbf1_{\{B\subseteq M'_1\}}
\leq
\mathbf1_{\{B\subseteq M_1\}}
\]

for every forward choice.

For each fixed first-layer permutation \(\pi\), exactly \(!N\)
second-layer permutations are edge-disjoint from it: after relabelling
columns by \(\pi^{-1}\), they are the derangements. Thus the first-layer
marginal of the uniform measure on \(\Omega_2\) is uniform on all
permutations. Conditioned on \(F\), it is uniform on the
\((N-k)!\) extensions of \(F\). Exactly \((N-k-s)!\) of those extensions
also contain the vertex-disjoint partial matching \(B\). Therefore

\[
\Pr(B\subseteq M_1\mid F\subseteq M_1)
=\frac{(N-k-s)!}{(N-k)!}
=\frac1{(N-k)_s}.
\]

The pathwise inequality gives the first box. Dividing by
\(1/(N)_s\) gives the product. Finally
\(\log(1+x)\leq x\) and
\(N-k-r\geq N-k-s+1\) give the exponential bound. \(\square\)

## SRR3c -- untouched-layer remote-event bound

Retain a layer-one flaw \(F\), and let \(B\) now be a rank-\(s\) partial
matching entirely in layer two. Assume the row and column vertices of
\(B\) are disjoint from those of \(F\), and \(N\geq2s\).

For \(0\leq q\leq n\), let

\[
D(n,q)
=
\sum_{j=0}^q(-1)^j\binom qj(n-j)!
\]

be the number of permutations of \(n\) points avoiding \(q\) prescribed
positions in distinct rows and columns. Put

\[
d_N=\frac{!N}{N!},
\qquad
A(n,q)=\frac{D(n,q)}{n!}.
\]

### Theorem SRR3c -- PROVED

The SRR3a oracle leaves \(B\) unchanged pathwise, and

\[
\boxed{
\Pr(B\subseteq M'_2\mid F\subseteq M_1)
\leq
\frac{D(N-s,N-2s)}{!N}.
}
\]

Relative to the stationary marginal
\(\Pr(B\subseteq M_2)=1/(N)_s\), the inflation is at most

\[
\boxed{
R_{N,s}
=
\frac{A(N-s,N-2s)}{d_N}
=1+O_s(N^{-1}).
}
\]

Hence pure remote events in the untouched layer also satisfy the
\(1+o(1)\) locality requirement for every fixed rank.

### Proof

The oracle changes only layer one, so it preserves the truth of \(B\)
in every state.

Fix a first-layer permutation \(\pi\) extending \(F\). If \(\pi\)
contains any edge of \(B\), no edge-disjoint second layer can contain
\(B\), and the desired upper bound is immediate. Otherwise delete the
\(s\) rows and \(s\) columns prescribed by \(B\). The remaining
second-layer permutation has size \(n=N-s\). Among the \(N\) forbidden
positions supplied by \(\pi\), at most \(2s\) were deleted: at most \(s\)
meet a deleted row and at most \(s\) meet a deleted column. Thus at least
\(N-2s\) forbidden positions survive, still in distinct rows and
columns.

Avoiding more prescribed positions can only decrease the number of
permutations. Inclusion--exclusion on any \(q\) disjoint positions gives
exactly \(D(n,q)\), so the number of second-layer extensions of \(B\)
which avoid \(\pi\) is at most \(D(N-s,N-2s)\). There are exactly \(!N\)
second layers avoiding each fixed \(\pi\). The pointwise conditional
bound therefore holds for every \(\pi\), and averaging over the
first-layer permutations conditioned on \(F\) proves the first box.

The second-layer marginal on \(\Omega_2\) is uniform, so division by
\(1/(N)_s=(N-s)!/N!\) gives \(R_{N,s}\).

For completeness, write \(n=N-s\). Then

\[
A(n,n-s)
=
\sum_{j=0}^{n-s}
\frac{(-1)^j}{j!}
\prod_{\ell=0}^{j-1}
\left(1-\frac{s}{n-\ell}\right).
\]

For fixed \(s\), the product differs from one by \(O_s(j/n)\) while
\(j\leq n/2\); the remaining factorial tail is \(o(n^{-1})\). Summing
against \(1/j!\) gives

\[
A(n,n-s)=e^{-1}+O_s(n^{-1}).
\]

The alternating derangement series gives
\(d_N=e^{-1}+O((N+1)!^{-1})\). Their ratio is
\(1+O_s(N^{-1})\), as claimed. \(\square\)

## SRR3d -- mixed-layer remote-event bound

Let a remote event \(B=B_1\cup B_2\) prescribe \(s_1\) edges in the
resampled layer and \(s_2\) edges in the untouched layer. Assume that the
row sets and column sets used by \(F,B_1,B_2\) are pairwise disjoint.
This is the compatibility carried by a nonhorizontal, nonvertical
collinear triple. Assume also \(N\geq2s_2\).

### Theorem SRR3d -- PROVED

The mixed event cannot be created pathwise. Moreover,

\[
\Pr(B\subseteq M'\mid F\subseteq M)
\leq
\frac1{(N-k)_{s_1}}
\cdot
\frac{D(N-s_2,N-2s_2)}{!N}.
\]

Its stationary probability has the lower bound

\[
\Pr_\mu(B)
\geq
\frac{
D(N-s_1,s_2)\,!(N-s_2)
}{
N!\,!N
}.
\]

Consequently its resampling inflation is at most

\[
\boxed{
Q_{N;k,s_1,s_2}
=
\frac{
N!\,D(N-s_2,N-2s_2)
}{
(N-k)_{s_1}\,
D(N-s_1,s_2)\,
!(N-s_2)
}
=1+O_{k,s_1,s_2}(N^{-1}).
}
\]

### Proof

SRR3b shows that the switch cannot create the \(B_1\) part, while the
\(B_2\) part is unchanged. Hence it cannot create their conjunction.

Conditioned on \(F\), the first layer is a uniform extension of \(F\),
so it contains the vertex-disjoint \(B_1\) with probability
\(1/(N-k)_{s_1}\). For each such first layer, the argument of SRR3c
bounds the conditional probability of \(B_2\) by
\(D(N-s_2,N-2s_2)/!N\). Multiplication proves the first display.

For the stationary lower bound, first choose a layer-one permutation
which contains \(B_1\) and avoids every cell of \(B_2\). After deleting
the \(s_1\) fixed rows and columns of \(B_1\), inclusion--exclusion on the
\(s_2\) surviving forbidden positions gives exactly
\(D(N-s_1,s_2)\) choices. For each such first layer, fix \(B_2\) in the
second layer and delete its rows and columns. At most \(N-s_2\)
first-layer forbidden positions survive, so at least \(!(N-s_2))\)
second-layer extensions avoid them. Divide this product by
\(|\Omega_2|=N!\,!N\).

The ratio of the conditional upper bound to the stationary lower bound
is \(Q_{N;k,s_1,s_2}\). To read its asymptotics, factor it as

\[
\frac{(N)_{s_1}}{(N-k)_{s_1}}
\cdot
\frac1{A(N-s_1,s_2)}
\cdot
\frac{A(N-s_2,N-2s_2)}{d_{N-s_2}}.
\]

The first factor is \(1+O_{k,s_1}(N^{-1})\). A union bound gives
\(1-s_2/(N-s_1)\leq A(N-s_1,s_2)\leq1\), so the second is
\(1+O_{s_1,s_2}(N^{-1})\). The third is
\(1+O_{s_2}(N^{-1})\) by the argument in SRR3c. This proves the final
box. \(\square\)

## SRR3e -- general compatible-cylinder locality

A labelled two-layer cylinder \(E=(E_1,E_2)\) prescribes \(a\) edges in
layer one and \(b\) edges in layer two. Call it globally compatible when
all its prescribed cells have distinct row coordinates and distinct
column coordinates, even across the two layers. Define

\[
U_N(a,b)
=
\frac{(N-a)!\,D(N-b,N-2b)}{N!\,!N}
\]

when \(N\geq2b\), and

\[
L_N(a,b)
=
\frac{D(N-a,b)\,!(N-b)}{N!\,!N}.
\]

### Lemma SRR3e -- PROVED

Every globally compatible cylinder of layer ranks \((a,b)\) satisfies

\[
\boxed{
L_N(a,b)\leq\Pr_\mu(E)\leq U_N(a,b).
}
\]

For fixed \(a,b\),

\[
L_N(a,b),\,U_N(a,b)
=
\frac{1+O_{a,b}(N^{-1})}{(N)_a(N)_b}.
\]

Now let a globally compatible flaw \(F\) have ranks \((k_1,k_2)\), contain
the distinguished layer-one edge, and let a globally compatible remote
event \(B\) have ranks \((s_1,s_2)\). Assume all row and column vertices
of \(F\) and \(B\) are disjoint and
\(N\geq2(k_2+s_2)\). Then

\[
\boxed{
\frac{
\Pr(B\subseteq M'\mid F\subseteq M)
}{
\Pr_\mu(B)
}
\leq
\frac{
U_N(k_1+s_1,k_2+s_2)
}{
L_N(k_1,k_2)L_N(s_1,s_2)
}
=1+O_{k_1,k_2,s_1,s_2}(N^{-1}).
}
\]

The same statement holds with the layers exchanged.

### Proof

For the upper cylinder count, choose a layer-one extension of \(E_1\) in
\((N-a)!\) ways. For each such permutation, either it already uses a
cell of \(E_2\), giving no edge-disjoint extension, or SRR3c bounds the
number of layer-two extensions of \(E_2\) by
\(D(N-b,N-2b)\). Division by \(N!\,!N\) gives \(U_N(a,b)\).

For the lower count, choose a layer-one extension of \(E_1\) which avoids
all \(b\) cells of \(E_2\). Global compatibility leaves those \(b\)
positions intact after the \(a\) fixed rows and columns are deleted, so
there are exactly \(D(N-a,b)\) choices. For each, the number of
layer-two extensions of \(E_2\) avoiding layer one is at least
\(!(N-b)\), as in SRR3d. This gives \(L_N(a,b)\).

The identities

\[
U_N(a,b)
=
\frac1{(N)_a(N)_b}
\cdot
\frac{A(N-b,N-2b)}{d_N}
\]

and

\[
L_N(a,b)
=
\frac1{(N)_a(N)_b}
\cdot
A(N-a,b)\frac{d_{N-b}}{d_N}
\]

together with the estimates proved in SRR3c--SRR3d give the two
asymptotics.

Pathwise, a switch cannot create the layer-one part of \(B\), and it
does not alter the layer-two part. Hence it cannot create \(B\).
Furthermore \(F\cup B\) is a globally compatible cylinder of ranks
\((k_1+s_1,k_2+s_2)\), so

\[
\Pr(B\mid F)
=
\frac{\Pr(F\cup B)}{\Pr(F)}
\leq
\frac{
U_N(k_1+s_1,k_2+s_2)
}{
L_N(k_1,k_2)
}.
\]

Divide by \(\Pr(B)\geq L_N(s_1,s_2)\). The fixed-rank asymptotics make
the resulting quotient \(1+O(N^{-1})\). \(\square\)

## Scope

This proves the stationary and exact-cover-preservation parts of SRR3 in
the complete host. A geometric conflict can be split into at most
\(2^3\) labelled layer assignments, and each labelled event may choose
one distinguished edge for this oracle.

SRR3b proves the required \(1+o(1)\) estimate for remote events lying
entirely in the resampled layer. SRR3c proves it for events lying entirely
in the untouched layer, and SRR3d handles mixed events whose prescribed
cells are globally row-column compatible when the flaw is in one layer.
SRR3e extends the result to globally compatible mixed-layer flaws and
remote events. This completes the remote-event calculation for the
complete two-layer host and the canonical pair/triple events relevant
here. In a superregular host, missing cross edges still require longer
switching cycles and a Hall/flow argument.

`scripts/verify_complete_two_layer_resampling.py` exhaustively checks the
switching degrees, exact-cover invariants, reversibility, stationarity,
and the pure- and mixed-layer remote bounds for \(N=4,5\).
