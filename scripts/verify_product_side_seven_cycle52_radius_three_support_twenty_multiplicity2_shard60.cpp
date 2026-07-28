#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    600,
    10,
    {{526564ULL,1011416ULL}},
    {{3959504ULL,5243214ULL}},
    {{892999ULL,1579604ULL,808318ULL,1645936ULL}},
    17027528386304151835ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
