#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    60,
    10,
    {{1283272ULL,1050612ULL}},
    {{4275863ULL,3372727ULL}},
    {{2008611ULL,1527565ULL,2110353ULL,1622905ULL}},
    3249460517323103648ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
