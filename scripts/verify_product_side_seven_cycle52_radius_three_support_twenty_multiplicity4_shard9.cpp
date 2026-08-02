#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    4,
    2392,
    880,
    100,
    {{4755656ULL,4229387ULL}},
    {{24637240ULL,24648351ULL}},
    {{8468880ULL,7617110ULL,8536783ULL,6945121ULL}},
    12419190773889184606ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
