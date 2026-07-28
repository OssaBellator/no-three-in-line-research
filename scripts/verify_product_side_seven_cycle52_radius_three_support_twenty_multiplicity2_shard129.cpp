#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2, 3840, 1290, 10,
    {{478736ULL,546252ULL}},
    {{6554330ULL,6182410ULL}},
    {{727765ULL,880330ULL,697093ULL,732213ULL}},
    3350805294673612655ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
