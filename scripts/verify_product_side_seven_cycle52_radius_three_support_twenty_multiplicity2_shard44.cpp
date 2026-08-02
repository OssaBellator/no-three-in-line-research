#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    440,
    10,
    {{1432264ULL,845640ULL}},
    {{5503177ULL,3881813ULL}},
    {{2276801ULL,1386326ULL,2305170ULL,1339096ULL}},
    1665996365935274379ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
