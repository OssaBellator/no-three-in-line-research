#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    660,
    10,
    {{1515896ULL,665712ULL}},
    {{6032426ULL,2879174ULL}},
    {{2567595ULL,1019797ULL,2325338ULL,1150807ULL}},
    13670699828197759913ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
