#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    70,
    10,
    {{1074048ULL,314588ULL}},
    {{3399294ULL,1101332ULL}},
    {{1620725ULL,564736ULL,1893243ULL,455228ULL}},
    9107125746619132178ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
