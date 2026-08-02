#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    3200,
    100,
    {{4956780ULL,3690892ULL}},
    {{45033818ULL,35753478ULL}},
    {{8820920ULL,6740592ULL,8149782ULL,5794287ULL}},
    14519279701100109802ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
