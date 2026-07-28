#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    790,
    10,
    {{555032ULL,498812ULL}},
    {{1786222ULL,1635810ULL}},
    {{918549ULL,814925ULL,885359ULL,793281ULL}},
    4230035789429227200ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
