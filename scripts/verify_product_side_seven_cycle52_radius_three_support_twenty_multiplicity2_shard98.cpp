#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    980,
    10,
    {{734436ULL,340452ULL}},
    {{6604714ULL,2991250ULL}},
    {{1261106ULL,520625ULL,1141735ULL,547442ULL}},
    5207635067091122284ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
