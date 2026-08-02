#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    450,
    10,
    {{2288608ULL,816166ULL}},
    {{8218337ULL,3040216ULL}},
    {{3767837ULL,1252689ULL,3601957ULL,1417119ULL}},
    14092422409558173123ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
