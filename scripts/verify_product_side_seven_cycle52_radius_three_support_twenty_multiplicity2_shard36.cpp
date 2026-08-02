#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    360,
    10,
    {{489338ULL,482774ULL}},
    {{1535876ULL,1504623ULL}},
    {{689995ULL,790781ULL,726925ULL,625858ULL}},
    1284622885101910788ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
