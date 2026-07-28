#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1040,
    10,
    {{577576ULL,457774ULL}},
    {{1918467ULL,1550354ULL}},
    {{854581ULL,692652ULL,856236ULL,656512ULL}},
    13851204348897764996ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
