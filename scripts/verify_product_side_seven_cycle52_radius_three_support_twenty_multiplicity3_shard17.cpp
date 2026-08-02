#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    1700,
    100,
    {{5302962ULL,4215652ULL}},
    {{32972336ULL,24912718ULL}},
    {{8890568ULL,7194248ULL,8855909ULL,6877928ULL}},
    13427787607035111628ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
