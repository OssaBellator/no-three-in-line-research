#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    3300,
    100,
    {{5181861ULL,3957781ULL}},
    {{50345297ULL,40233222ULL}},
    {{9480573ULL,7266236ULL,9099237ULL,6479853ULL}},
    9297774443006448587ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
