#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    540,
    10,
    {{351766ULL,177460ULL}},
    {{1110273ULL,596115ULL}},
    {{518256ULL,288694ULL,506547ULL,240334ULL}},
    5234405795839717689ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
