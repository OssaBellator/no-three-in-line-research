#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    10,
    10,
    {{328680ULL,309618ULL}},
    {{962690ULL,889149ULL}},
    {{452803ULL,577107ULL,629153ULL,398750ULL}},
    13243692266140994388ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
