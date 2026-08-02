#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    2200,
    100,
    {{4973041ULL,3288762ULL}},
    {{58776354ULL,42048981ULL}},
    {{8386481ULL,5530262ULL,8321946ULL,5261831ULL}},
    18285130004508838207ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
