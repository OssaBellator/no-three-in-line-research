#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    190,
    10,
    {{748698ULL,600041ULL}},
    {{3579557ULL,2823439ULL}},
    {{1179604ULL,876603ULL,1138416ULL,978742ULL}},
    12273077452420250578ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
