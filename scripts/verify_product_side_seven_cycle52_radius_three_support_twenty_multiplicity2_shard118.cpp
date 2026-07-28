#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1180,
    10,
    {{539069ULL,383831ULL}},
    {{2583385ULL,1934593ULL}},
    {{814728ULL,578745ULL,773571ULL,567102ULL}},
    9647236515249463310ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
