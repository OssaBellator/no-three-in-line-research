#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    310,
    10,
    {{1053394ULL,753236ULL}},
    {{3433572ULL,2472650ULL}},
    {{1687863ULL,1116699ULL,1651420ULL,1231381ULL}},
    18126001820985620447ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
