#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    2180,
    100,
    {{4833937ULL,4070638ULL}},
    {{42210376ULL,33267205ULL}},
    {{9150466ULL,7638873ULL,8515848ULL,7117297ULL}},
    6419771693688218342ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
