#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    150,
    10,
    {{547371ULL,427344ULL}},
    {{2344967ULL,1842714ULL}},
    {{828227ULL,660408ULL,845989ULL,627730ULL}},
    3048902713011650628ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
