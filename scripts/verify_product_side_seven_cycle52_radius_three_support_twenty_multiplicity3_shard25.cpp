#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    2500,
    100,
    {{6170218ULL,3639364ULL}},
    {{40890878ULL,26985174ULL}},
    {{10555033ULL,6089946ULL,10437366ULL,6535796ULL}},
    11824482046511188436ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
