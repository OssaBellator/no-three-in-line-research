#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    930,
    10,
    {{290052ULL,687500ULL}},
    {{1404012ULL,2659628ULL}},
    {{510626ULL,1121948ULL,431342ULL,985014ULL}},
    13473758246526618952ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
