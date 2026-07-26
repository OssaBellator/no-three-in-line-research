#include "product_side_seven_tier_digest.hpp"

const TierDigestExpectations EXPECTED = {
    5,
    725,
    {{39457291ULL,30013327ULL}},
    {{271756171ULL,215692788ULL}},
    {{71190922ULL,53985045ULL,68865985ULL,51864073ULL}},
    97485168211241114ULL
};

int main(int argc,char** argv) {
    return verify_tier_digest(argc,argv,EXPECTED);
}
