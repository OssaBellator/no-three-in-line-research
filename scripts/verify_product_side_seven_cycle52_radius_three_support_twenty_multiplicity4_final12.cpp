#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    2380,
    12,
    {{333578ULL,347478ULL}},
    {{5829983ULL,8718578ULL}},
    {{479309ULL,579006ULL,599385ULL,423526ULL}},
    5163944326560678257ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
