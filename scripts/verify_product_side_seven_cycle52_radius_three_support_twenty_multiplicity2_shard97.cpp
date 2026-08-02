#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    970,
    10,
    {{336740ULL,389452ULL}},
    {{6254070ULL,5812266ULL}},
    {{492003ULL,659996ULL,489691ULL,482754ULL}},
    764748930000373914ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
