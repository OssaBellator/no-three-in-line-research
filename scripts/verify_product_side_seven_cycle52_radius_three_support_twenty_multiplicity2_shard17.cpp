#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    170,
    10,
    {{337416ULL,99350ULL}},
    {{1068085ULL,354568ULL}},
    {{478133ULL,154974ULL,495956ULL,133185ULL}},
    576955961683063087ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
