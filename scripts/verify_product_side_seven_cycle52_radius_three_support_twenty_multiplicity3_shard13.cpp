#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    1300,
    100,
    {{3387028ULL,3513002ULL}},
    {{33130720ULL,28472042ULL}},
    {{5696899ULL,6279800ULL,6018454ULL,5448632ULL}},
    13401041420045109676ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
