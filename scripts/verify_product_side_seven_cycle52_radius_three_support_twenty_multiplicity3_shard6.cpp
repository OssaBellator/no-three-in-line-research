#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    3,
    3544,
    600,
    100,
    {{8080650ULL,6781398ULL}},
    {{61266632ULL,47608431ULL}},
    {{14542238ULL,12109860ULL,13433301ULL,12184856ULL}},
    4240448745985646561ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
