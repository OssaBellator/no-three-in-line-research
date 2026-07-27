#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    2100,
    100,
    {{8258402ULL,4931106ULL}},
    {{55510853ULL,40759840ULL}},
    {{15011755ULL,8973290ULL,14619133ULL,8198957ULL}},
    9853376004029332515ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
