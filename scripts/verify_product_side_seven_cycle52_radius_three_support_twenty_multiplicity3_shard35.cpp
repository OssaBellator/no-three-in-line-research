#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    3500,
    44,
    {{1265142ULL,2044936ULL}},
    {{20047930ULL,24376146ULL}},
    {{2072548ULL,3742522ULL,2481739ULL,3188650ULL}},
    3731072057743112162ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
