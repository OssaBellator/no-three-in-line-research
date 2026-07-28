#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1020,
    10,
    {{185672ULL,269298ULL}},
    {{3711461ULL,4693032ULL}},
    {{253893ULL,436612ULL,279499ULL,336313ULL}},
    6499844922641713310ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
