#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    750,
    10,
    {{405036ULL,349054ULL}},
    {{1806464ULL,1548591ULL}},
    {{635224ULL,522902ULL,574100ULL,496917ULL}},
    4711295851722750288ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
