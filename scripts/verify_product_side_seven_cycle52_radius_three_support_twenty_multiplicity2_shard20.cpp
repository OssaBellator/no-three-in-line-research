#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    200,
    10,
    {{1052036ULL,555719ULL}},
    {{4548494ULL,2240053ULL}},
    {{1632348ULL,909912ULL,1652343ULL,894195ULL}},
    14184090767390867316ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
