#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    2700,
    100,
    {{6102049ULL,3739533ULL}},
    {{40679052ULL,24336395ULL}},
    {{10878334ULL,6554512ULL,10737512ULL,7011562ULL}},
    12950518957910341982ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
