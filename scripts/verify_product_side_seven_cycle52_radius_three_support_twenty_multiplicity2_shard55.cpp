#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    550,
    10,
    {{806514ULL,865282ULL}},
    {{3492884ULL,3740823ULL}},
    {{1335151ULL,1362131ULL,1248030ULL,1409004ULL}},
    12678841959537449495ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
