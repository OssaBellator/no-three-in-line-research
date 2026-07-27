#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    1200,
    100,
    {{4899054ULL,4287820ULL}},
    {{24836222ULL,22387466ULL}},
    {{8805636ULL,7370353ULL,8101190ULL,7198789ULL}},
    10436604609621675837ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
