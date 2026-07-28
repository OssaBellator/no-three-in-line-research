#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    690,
    10,
    {{1325422ULL,465616ULL}},
    {{8466153ULL,4443011ULL}},
    {{2193873ULL,766991ULL,2037309ULL,745209ULL}},
    13237971452873956928ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
