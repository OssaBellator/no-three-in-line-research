#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    510,
    10,
    {{580184ULL,397636ULL}},
    {{1844698ULL,1281300ULL}},
    {{879107ULL,600169ULL,902856ULL,572757ULL}},
    6799617504066900155ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
