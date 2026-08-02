#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    770,
    10,
    {{288028ULL,382038ULL}},
    {{1161218ULL,1429488ULL}},
    {{459950ULL,635199ULL,432593ULL,502468ULL}},
    17928620657005057642ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
