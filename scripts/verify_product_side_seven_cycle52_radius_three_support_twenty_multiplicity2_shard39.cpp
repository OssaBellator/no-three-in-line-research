#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    390,
    10,
    {{515836ULL,447798ULL}},
    {{1997922ULL,1795588ULL}},
    {{786654ULL,696072ULL,742054ULL,637115ULL}},
    13987574131200629039ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
