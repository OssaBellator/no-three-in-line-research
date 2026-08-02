#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    1500,
    100,
    {{7266748ULL,4135428ULL}},
    {{35429821ULL,21178323ULL}},
    {{12992091ULL,6973894ULL,12496155ULL,7178897ULL}},
    2105066167187410418ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
