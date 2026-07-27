#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    900,
    100,
    {{5613366ULL,4495113ULL}},
    {{38524963ULL,27653375ULL}},
    {{10343692ULL,8234478ULL,9276412ULL,7719090ULL}},
    11884124847722068902ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
