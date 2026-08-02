#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    910,
    10,
    {{558940ULL,205412ULL}},
    {{2233515ULL,819539ULL}},
    {{1025277ULL,323512ULL,886032ULL,349726ULL}},
    12938349699372377995ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
