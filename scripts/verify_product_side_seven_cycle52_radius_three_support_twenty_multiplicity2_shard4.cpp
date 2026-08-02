#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    40,
    10,
    {{571454ULL,268770ULL}},
    {{1705775ULL,829779ULL}},
    {{839088ULL,469423ULL,1001764ULL,358638ULL}},
    4618887835585757129ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
