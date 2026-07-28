#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1100,
    10,
    {{331472ULL,360344ULL}},
    {{1021045ULL,1081185ULL}},
    {{515341ULL,582280ULL,524853ULL,498429ULL}},
    15829640899376239907ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
