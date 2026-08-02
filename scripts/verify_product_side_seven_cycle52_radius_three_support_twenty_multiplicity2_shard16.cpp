#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    160,
    10,
    {{485868ULL,518232ULL}},
    {{1510023ULL,1614799ULL}},
    {{739498ULL,840804ULL,775441ULL,756764ULL}},
    18351291531595309837ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
