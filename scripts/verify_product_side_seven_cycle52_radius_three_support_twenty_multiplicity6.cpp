#include "product_side_seven_tier_digest.hpp"

const TierDigestExpectations EXPECTED = {
    6,
    524,
    {{24004326ULL,17430207ULL}},
    {{182105002ULL,135396810ULL}},
    {{48133628ULL,34573453ULL,46688221ULL,32838128ULL}},
    17309853148831689366ULL
};

int main(int argc,char** argv) {
    return verify_tier_digest(argc,argv,EXPECTED);
}
