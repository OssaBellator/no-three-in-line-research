#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    710,
    10,
    {{411522ULL,372618ULL}},
    {{1286310ULL,1185836ULL}},
    {{593221ULL,586317ULL,610182ULL,478422ULL}},
    3876622946876399712ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
