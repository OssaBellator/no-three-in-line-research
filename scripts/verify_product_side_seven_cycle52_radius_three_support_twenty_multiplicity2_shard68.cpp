#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    680,
    10,
    {{1303940ULL,217012ULL}},
    {{5789166ULL,1179668ULL}},
    {{2318307ULL,335648ULL,1946725ULL,359812ULL}},
    5893286243712271176ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
