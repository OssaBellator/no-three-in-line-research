#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    860,
    10,
    {{1085438ULL,630530ULL}},
    {{4725732ULL,2626621ULL}},
    {{1830872ULL,989426ULL,1644093ULL,980260ULL}},
    5676021412180323776ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
