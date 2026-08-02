#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    620,
    10,
    {{805842ULL,495852ULL}},
    {{4477204ULL,2881024ULL}},
    {{1243986ULL,715247ULL,1168757ULL,797495ULL}},
    16112937728120265129ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
