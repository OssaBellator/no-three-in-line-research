#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2, 3840, 1350, 10,
    {{1149856ULL,816460ULL}},
    {{3489571ULL,2567879ULL}},
    {{1837651ULL,1242983ULL,1905525ULL,1235206ULL}},
    14500902586021413143ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
