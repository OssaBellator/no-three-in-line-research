#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    670,
    10,
    {{949630ULL,486200ULL}},
    {{4212538ULL,2230378ULL}},
    {{1541653ULL,770566ULL,1379244ULL,758120ULL}},
    11247092659769912659ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
