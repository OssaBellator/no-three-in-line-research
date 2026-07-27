#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    100,
    100,
    {{6341588ULL,5776036ULL}},
    {{35667482ULL,29320319ULL}},
    {{11184684ULL,9969160ULL,10698436ULL,9962634ULL}},
    6981881274263131756ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
