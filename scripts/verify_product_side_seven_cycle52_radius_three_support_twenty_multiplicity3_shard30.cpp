#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    3000,
    100,
    {{8389492ULL,5363396ULL}},
    {{68769395ULL,41515152ULL}},
    {{14886610ULL,9288054ULL,14065624ULL,8785112ULL}},
    13070021860948705188ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
