#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    350,
    10,
    {{238348ULL,307204ULL}},
    {{759048ULL,976354ULL}},
    {{342713ULL,467877ULL,345061ULL,404695ULL}},
    7917794102842155404ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
