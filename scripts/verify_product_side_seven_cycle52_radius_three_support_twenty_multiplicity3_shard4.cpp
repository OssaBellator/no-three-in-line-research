#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    400,
    100,
    {{6509108ULL,4316592ULL}},
    {{33529101ULL,21419876ULL}},
    {{11154608ULL,6964716ULL,10631223ULL,7242251ULL}},
    10311187618878375372ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
