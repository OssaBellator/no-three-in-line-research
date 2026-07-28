#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    810,
    10,
    {{204912ULL,283412ULL}},
    {{1348097ULL,1191568ULL}},
    {{316626ULL,485452ULL,317083ULL,377143ULL}},
    16772310416434152769ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
