#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    0,
    100,
    {{4545839ULL,3856995ULL}},
    {{22273454ULL,16803083ULL}},
    {{7437610ULL,6498551ULL,8049399ULL,6030205ULL}},
    3064849620408509937ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
