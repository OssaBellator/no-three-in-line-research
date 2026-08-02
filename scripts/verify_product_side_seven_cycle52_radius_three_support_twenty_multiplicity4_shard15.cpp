#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    1480,
    100,
    {{5504876ULL,4051886ULL}},
    {{48887465ULL,36656613ULL}},
    {{8591057ULL,6162767ULL,8593780ULL,5850288ULL}},
    3651704852006478728ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
