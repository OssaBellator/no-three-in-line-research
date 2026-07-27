#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    2080,
    100,
    {{5334880ULL,6322753ULL}},
    {{40890192ULL,38384873ULL}},
    {{9657567ULL,11801429ULL,8907044ULL,10667171ULL}},
    16866968297745794325ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
