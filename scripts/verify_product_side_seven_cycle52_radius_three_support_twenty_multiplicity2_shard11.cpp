#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    110,
    10,
    {{488360ULL,1257724ULL}},
    {{3289142ULL,5815562ULL}},
    {{870148ULL,1997533ULL,785909ULL,2054670ULL}},
    17946475240143660ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
