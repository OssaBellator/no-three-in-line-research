#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    800,
    10,
    {{697318ULL,606006ULL}},
    {{3347770ULL,2570932ULL}},
    {{1095179ULL,994655ULL,1147626ULL,1054345ULL}},
    2741874371339139127ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
