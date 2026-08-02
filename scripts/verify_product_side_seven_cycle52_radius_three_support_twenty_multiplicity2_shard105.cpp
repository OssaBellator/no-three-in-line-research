#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1050,
    10,
    {{784012ULL,414300ULL}},
    {{3061721ULL,1745796ULL}},
    {{1140050ULL,611218ULL,1149817ULL,629214ULL}},
    2257177977923349832ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
