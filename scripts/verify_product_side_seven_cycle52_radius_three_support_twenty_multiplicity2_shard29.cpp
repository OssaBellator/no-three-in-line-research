#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    290,
    10,
    {{301476ULL,65274ULL}},
    {{847259ULL,196171ULL}},
    {{464366ULL,121890ULL,526491ULL,83990ULL}},
    6776011627925700319ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
