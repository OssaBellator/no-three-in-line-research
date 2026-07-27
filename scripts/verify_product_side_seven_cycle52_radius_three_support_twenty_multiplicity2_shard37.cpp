#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    370,
    10,
    {{1339516ULL,848016ULL}},
    {{4107992ULL,2647309ULL}},
    {{2167538ULL,1327358ULL,2200675ULL,1329231ULL}},
    16735768237502152273ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
