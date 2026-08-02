#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    760,
    10,
    {{375076ULL,379526ULL}},
    {{1997711ULL,1988552ULL}},
    {{574265ULL,573289ULL,529680ULL,545837ULL}},
    13093882893357327338ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
