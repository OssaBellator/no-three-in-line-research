#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2, 3840, 1340, 10,
    {{211626ULL,461778ULL}},
    {{602359ULL,1286785ULL}},
    {{288329ULL,844824ULL,350406ULL,526636ULL}},
    15976464783720629267ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
