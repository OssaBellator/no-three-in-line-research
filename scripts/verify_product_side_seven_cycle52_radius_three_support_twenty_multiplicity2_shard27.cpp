#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    270,
    10,
    {{451884ULL,716862ULL}},
    {{1311851ULL,2065824ULL}},
    {{671074ULL,1261700ULL,782307ULL,982028ULL}},
    13591523195064408722ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
