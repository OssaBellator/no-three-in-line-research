#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    90,
    10,
    {{605356ULL,463504ULL}},
    {{2796119ULL,1959414ULL}},
    {{913135ULL,717599ULL,979474ULL,727875ULL}},
    3834793925943032802ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
