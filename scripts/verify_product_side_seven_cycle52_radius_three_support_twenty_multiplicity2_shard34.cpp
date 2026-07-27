#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    340,
    10,
    {{241716ULL,293448ULL}},
    {{768235ULL,936765ULL}},
    {{347415ULL,458891ULL,353286ULL,393136ULL}},
    16622973091455341356ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
