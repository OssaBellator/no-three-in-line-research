#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    430,
    10,
    {{1199108ULL,1351242ULL}},
    {{5673041ULL,6244197ULL}},
    {{1941384ULL,2094053ULL,1936491ULL,2258572ULL}},
    10652007544342656566ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
