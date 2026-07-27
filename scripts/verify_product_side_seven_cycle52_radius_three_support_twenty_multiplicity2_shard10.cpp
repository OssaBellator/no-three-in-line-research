#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    100,
    10,
    {{1007212ULL,389440ULL}},
    {{3540431ULL,1444494ULL}},
    {{1454231ULL,676481ULL,1556487ULL,545633ULL}},
    9447947952084994573ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
