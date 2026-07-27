#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    260,
    10,
    {{316666ULL,384476ULL}},
    {{963935ULL,1116593ULL}},
    {{453592ULL,735047ULL,545935ULL,459804ULL}},
    11692544106972541554ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
