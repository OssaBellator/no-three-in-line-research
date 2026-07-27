#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    230,
    10,
    {{479544ULL,1190348ULL}},
    {{7190673ULL,9813454ULL}},
    {{772763ULL,1878908ULL,708609ULL,1809103ULL}},
    10637276132094415816ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
