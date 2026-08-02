#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    530,
    10,
    {{525492ULL,579212ULL}},
    {{1635136ULL,1800580ULL}},
    {{815404ULL,957259ULL,819683ULL,853410ULL}},
    11100554868985595416ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
