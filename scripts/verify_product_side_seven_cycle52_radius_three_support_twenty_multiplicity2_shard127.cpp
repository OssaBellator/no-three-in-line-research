#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1270,
    10,
    {{636288ULL,1068576ULL}},
    {{2739032ULL,4436894ULL}},
    {{1011957ULL,1639251ULL,882264ULL,1539297ULL}},
    14533600534674041241ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
