#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1250,
    10,
    {{358122ULL,313983ULL}},
    {{2304741ULL,2093850ULL}},
    {{560026ULL,462447ULL,503954ULL,445305ULL}},
    13781225323153859254ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
