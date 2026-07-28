#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    870,
    10,
    {{731196ULL,484803ULL}},
    {{3936838ULL,2758630ULL}},
    {{1189059ULL,770007ULL,1113075ULL,727090ULL}},
    16425776743378338066ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
