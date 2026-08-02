#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    830,
    10,
    {{487099ULL,479009ULL}},
    {{1799488ULL,1739695ULL}},
    {{783465ULL,753468ULL,689864ULL,679378ULL}},
    14980970733442961720ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
