#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    1100,
    100,
    {{4887082ULL,3641746ULL}},
    {{28322709ULL,21853698ULL}},
    {{8537948ULL,6260730ULL,8132293ULL,6040063ULL}},
    4611443749689298654ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
