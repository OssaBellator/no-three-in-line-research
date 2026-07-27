#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    220,
    10,
    {{856020ULL,372422ULL}},
    {{5062453ULL,2280524ULL}},
    {{1311611ULL,583837ULL,1223682ULL,613320ULL}},
    7321435250783849553ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
