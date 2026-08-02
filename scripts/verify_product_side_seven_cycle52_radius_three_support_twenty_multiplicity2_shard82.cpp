#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    820,
    10,
    {{293080ULL,344826ULL}},
    {{916970ULL,1070533ULL}},
    {{445440ULL,551097ULL,410543ULL,458906ULL}},
    8488868181964210369ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
