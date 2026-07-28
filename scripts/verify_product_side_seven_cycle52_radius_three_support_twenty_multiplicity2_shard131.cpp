#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2, 3840, 1310, 10,
    {{206360ULL,161340ULL}},
    {{3489989ULL,2675997ULL}},
    {{286206ULL,286891ULL,331910ULL,191072ULL}},
    3796189743782724071ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
