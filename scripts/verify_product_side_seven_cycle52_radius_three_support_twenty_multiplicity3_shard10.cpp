#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    1000,
    100,
    {{3310572ULL,3116324ULL}},
    {{28685755ULL,26324531ULL}},
    {{5764370ULL,5514534ULL,5343998ULL,5010578ULL}},
    12088490713403663561ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
