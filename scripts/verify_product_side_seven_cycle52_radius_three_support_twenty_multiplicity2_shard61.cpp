#include "product_side_seven_tier_shard_digest.hpp"

const TierShardDigestExpectations EXPECTED = {
    2,
    3840,
    610,
    10,
    {{406468ULL,915278ULL}},
    {{3659998ULL,5135856ULL}},
    {{630642ULL,1429988ULL,594449ULL,1397148ULL}},
    8631982483106294843ULL
};

int main(int argc,char** argv) {
    return verify_tier_shard_digest(argc,argv,EXPECTED);
}
