#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    140,
    10,
    {{552263ULL,395328ULL}},
    {{2114001ULL,1575926ULL}},
    {{832788ULL,578855ULL,860773ULL,584157ULL}},
    11228535735195360597ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
