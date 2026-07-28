#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    890,
    10,
    {{632323ULL,466171ULL}},
    {{3457133ULL,2695899ULL}},
    {{987348ULL,708384ULL,892293ULL,698241ULL}},
    3470846642447975920ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
