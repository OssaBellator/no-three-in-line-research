#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    0,
    10,
    {{217122ULL,541548ULL}},
    {{640749ULL,1521127ULL}},
    {{282364ULL,926841ULL,404053ULL,643479ULL}},
    10095218108694584973ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
