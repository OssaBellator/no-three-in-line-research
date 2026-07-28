#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    640,
    10,
    {{359512ULL,349564ULL}},
    {{1206687ULL,1213432ULL}},
    {{588071ULL,566602ULL,517621ULL,509672ULL}},
    9118922863212401361ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
