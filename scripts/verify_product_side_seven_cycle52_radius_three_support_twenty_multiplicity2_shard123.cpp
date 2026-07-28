#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    1230,
    10,
    {{669054ULL,423490ULL}},
    {{4175930ULL,2599290ULL}},
    {{1010855ULL,617776ULL,970218ULL,636229ULL}},
    9154343577324608262ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
