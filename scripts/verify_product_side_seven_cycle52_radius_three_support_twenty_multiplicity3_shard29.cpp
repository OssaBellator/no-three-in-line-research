#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    2900,
    100,
    {{11109348ULL,4713134ULL}},
    {{48656703ULL,21329302ULL}},
    {{20163564ULL,8053425ULL,18778933ULL,8894596ULL}},
    2066368581572695674ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
