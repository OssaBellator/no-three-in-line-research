#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    130,
    10,
    {{495974ULL,461046ULL}},
    {{2114175ULL,1994371ULL}},
    {{741335ULL,734470ULL,799870ULL,635934ULL}},
    15736712881480794511ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
