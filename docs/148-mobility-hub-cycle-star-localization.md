# Mobility-hub cycle-star localization

PP3ur reduces a low-mobility alternating component to a small feedback hub
\(U\).  The component is strongly connected, so every vertex still lies on a
nontrivial directed cycle.  Maximum mobility bounds the length of every such
cycle.  Counting these short cycles forces one hub vertex to lie on many of
them.

A vertex-capacitated Menger argument then gives either many cycles whose only
common vertex is that hub, or a second small separator through which all those
cycles pass.  The first case is an exact multistate endpoint-trade bank; the
second is a two-hub concentration core.

## 1. Every alternating cycle is short

Retain the fully credited component notation of PP3um--PP3ur.  Put

\[
r=\nu(C),
\qquad
U=\operatorname{mov}(N_*),
\qquad
|C|=n.
\]

### Proposition PP3us -- PROVED

Every nontrivial directed cycle of \(D_C\) has length at most \(r\).

#### Proof

Switching one directed cycle of length \(s\) gives a perfect matching moving all
\(s\) of its vertices.  The definition of \(r\) therefore gives \(s\le r\). ∎

## 2. One hub lies on many distinct cycles

### Theorem PP3ut -- PROVED

Some hub vertex \(u\in U\) lies on at least

\[
\boxed{
\frac{n-r}{r^2}
}
\]

distinct nontrivial directed cycles.

#### Proof

Every vertex \(v\in C\setminus U\) lies on a directed cycle because \(C\) is a
nontrivial strongly connected component.  Choose one such cycle \(\Gamma_v\).
By PP3us it contains at most \(r\) vertices, so one distinct cycle can be chosen
by at most \(r\) outside vertices.  Hence at least

\[
\frac{n-r}{r}
\]

distinct cycles occur among the choices.

Every chosen cycle meets \(U\) by PP3up.  Assign each distinct cycle to one of
its hub vertices.  Pigeonholing over the \(r\) vertices of \(U\) gives one hub
on at least \((n-r)/r^2\) distinct cycles. ∎

Thus constant or slowly growing mobility forces a polynomially rich alternating
cycle star.

## 3. Directed Menger at one hub

Fix a vertex \(u\), and consider the family of nontrivial directed cycles through
\(u\).

### Theorem PP3uu -- PROVED FROM VERTEX-CAPACITATED MAX FLOW

For every integer \(L\ge1\), exactly one of the following alternatives is
available.

1. There are \(L\) directed cycles through \(u\) whose vertex sets intersect
   pairwise only at \(u\).
2. There is a set
   
   \[
   W\subseteq C\setminus\{u\},
   \qquad
   |W|<L,
   \]
   
   meeting every nontrivial directed cycle through \(u\).

#### Proof

Delete \(u\).  Split every remaining vertex \(v\) into
\(v_{\rm in}\to v_{\rm out}\) with capacity one, and give every transformed
original arc infinite capacity.  Add a source joined to the in-copies of all
out-neighbours of \(u\), and join the out-copies of all in-neighbours of \(u\)
to a sink.

A source--sink path is exactly a directed \(u\)-cycle with \(u\) removed.
Internally vertex-disjoint paths correspond to cycles intersecting only at
\(u\).  Integral max flow either has value at least \(L\), giving alternative
1, or has a vertex cut of size below \(L\), whose original vertices form \(W\)
and meet every \(u\)-cycle. ∎

This is the directed vertex-Menger theorem in the special cycle-through-a-root
form needed here.

## 4. Star or two-hub concentration

Let \(t\) be the number of distinct cycles through the rich hub \(u\) supplied
by PP3ut.

### Corollary PP3uv -- PROVED

For every \(L\ge2\), one of the following holds.

1. There is an \(L\)-petal alternating cycle star through \(u\): the petals meet
   pairwise only at \(u\).
2. There is a second vertex \(w\ne u\) contained with \(u\) in at least
   
   \[
   \frac{t}{L-1}
   \]
   
   of the cycles.

#### Proof

Apply PP3uu.  In the separator alternative, every one of the \(t\) cycles meets
\(W\), where \(|W|<L\).  Pigeonhole the cycles over \(W\). ∎

Taking \(L=\lceil\sqrt t\rceil\) gives either a
\(\sqrt t\)-petal cycle star or a pair of vertices lying on
\(\Omega(\sqrt t)\) distinct alternating cycles.

## 5. Exact multistate cycle-star bank

Suppose

\[
\Gamma_1,\ldots,\Gamma_p
\]

are directed cycles whose pairwise intersection is exactly \(\{u\}\).

For state \(j\in[p]\), switch \(\Gamma_j\) and retain every reference edge outside
that cycle.

### Proposition PP3uw -- PROVED

These \(p\) states form one equal-margin finite-state variable with the following
properties.

1. Every state is a perfect matching of the component host.
2. Every state moves the common hub \(u\) and supplies
   
   \[
   R_j=|V(\Gamma_j)|
   \]
   
   designated credit units.
3. Outside the hub, the moved endpoint resources of distinct states are
   disjoint.
4. Every specific inserted off-diagonal matching edge occurs in at most one
   state.  Under the uniform state law its marginal probability is therefore at
   most \(1/p\).
5. Source validity and insertion cost of state \(j\) are exact deterministic
   quantities computed from the switched cycle.

#### Proof

Cycle switching gives a perfect matching by PP3um.  The cycles share no resource
outside \(u\), so their interior reference and inserted edges are disjoint.
Distinct cycles cannot use the same first or last neighbour of \(u\), since that
would create a second shared vertex.  Hence their off-diagonal edges incident
with \(u\) are also distinct.  The credit count is the number of moved fully
credited vertices. ∎

This distribution is one-state-per-petal rather than a product distribution:
patterns internal to one petal have probability \(1/p\), while patterns requiring
cells from two distinct petals have probability zero.

## 6. Paid averaging over petals

Let \(Z_j\in\{0,1\}\) indicate whether state \(j\) creates any no-three
violation, and let \(I_j\ge0\) be its exact insertion-shadow cost.

### Theorem PP3ux -- PROVED

If

\[
\boxed{
\frac1p
\sum_{j=1}^p
\left(
Z_j+\frac{I_j}{R_j}
\right)
<1,
}
\]

then one cycle-star state is source-admissible and strictly improves the paid
potential.

#### Proof

Some summand is below one.  Since \(Z_j\) is a nonnegative integer, that state
has \(Z_j=0\), and then \(I_j<R_j\).  Apply PP3ts or PP3kx. ∎

A weaker sufficient form replaces every \(R_j\) by the common lower bound two.
Failure of the theorem means that a positive fraction of petals are
source-invalid or that average insertion cost is comparable with their cycle
credit.

## 7. Revised low-mobility endpoint

### Corollary PP3uy -- PROVED

A fully credited unbounded alternating component has one of the following
structured forms.

1. A large resource-disjoint binary cycle bank from PP3uo.
2. A large one-hub multistate cycle-star bank satisfying the exact paid averaging
   interface PP3ux.
3. A pair of mobility-hub vertices lying on many distinct alternating cycles.
4. Concentrated source-invalid or insertion-shadow mass on the cycle-bank or
   cycle-star states.

Thus a small feedback hub is not a terminal abstract state-space obstruction.
It localizes further to a paid cycle star or a two-hub alternating-cycle core.