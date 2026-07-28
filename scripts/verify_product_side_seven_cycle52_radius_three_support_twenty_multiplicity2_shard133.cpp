#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2, 3840, 1330, 10,
    {{292540ULL,496256ULL}},
    {{948154ULL,1553854ULL}},
    {{428210ULL,776743ULL,484550ULL,737936ULL}},
    6816307819436119681ULL
};

int main(int argc,char** argv) { return verify_tier_shard_digest(argc,argv,EXPECTED); }
