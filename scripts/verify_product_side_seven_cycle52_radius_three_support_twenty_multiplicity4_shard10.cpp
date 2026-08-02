#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    980,
    100,
    {{6721748ULL,3646959ULL}},
    {{36472101ULL,22274418ULL}},
    {{12773829ULL,6614905ULL,12378517ULL,6211748ULL}},
    5499058393039379395ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
