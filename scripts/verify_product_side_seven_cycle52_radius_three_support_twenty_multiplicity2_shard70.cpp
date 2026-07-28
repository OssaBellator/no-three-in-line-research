#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    700,
    10,
    {{382330ULL,304094ULL}},
    {{6104866ULL,5194036ULL}},
    {{574082ULL,534470ULL,607055ULL,399121ULL}},
    7186785514344635808ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
