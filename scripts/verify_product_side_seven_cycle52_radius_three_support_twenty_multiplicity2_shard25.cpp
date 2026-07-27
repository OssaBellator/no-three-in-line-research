#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    250,
    10,
    {{472138ULL,376748ULL}},
    {{2911376ULL,1923238ULL}},
    {{685979ULL,580732ULL,734443ULL,497897ULL}},
    1131586997605564077ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
