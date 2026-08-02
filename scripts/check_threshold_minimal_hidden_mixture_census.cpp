#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;
using Matrix = array<int,16>;
struct MatrixHash {
    size_t operator()(Matrix const& matrix) const noexcept {
        size_t value = 1469598103934665603ULL;
        for (int entry : matrix) {
            value ^= static_cast<unsigned>(entry + 17);
            value *= 1099511628211ULL;
        }
        return value;
    }
};
long long cross(pair<int,int> a, pair<int,int> b, pair<int,int> c) {
    return 1LL*(b.first-a.first)*(c.second-a.second)
         - 1LL*(b.second-a.second)*(c.first-a.first);
}
bool legal(array<int,4> permutation) {
    vector<pair<int,int>> points;
    for (int row=0; row<4; ++row) points.push_back({row,permutation[row]});
    for (int i=0;i<4;i++) for (int j=i+1;j<4;j++) for (int k=j+1;k<4;k++)
        if (cross(points[i],points[j],points[k])==0) return false;
    return true;
}
int score(Matrix const& matrix) {
    static const int phi[16] = {-1,0,0,0, 1,0,1,0, 0,1,0,0, 0,0,1,-1};
    int answer=0;
    for (int index=0; index<16; ++index) answer += phi[index]*matrix[index];
    return answer;
}
int main() {
    vector<array<int,4>> layers;
    array<int,4> permutation={0,1,2,3};
    do { if (legal(permutation)) layers.push_back(permutation); }
    while (next_permutation(permutation.begin(),permutation.end()));
    if (layers.size()!=18) return 1;

    set<Matrix> legal_matrices;
    const int layer_count=static_cast<int>(layers.size());
    for (int first=0; first<layer_count; ++first)
    for (int second=first; second<layer_count; ++second)
    for (int third=second; third<layer_count; ++third)
    for (int fourth=third; fourth<layer_count; ++fourth) {
        Matrix matrix{};
        for (int layer : {first,second,third,fourth})
            for (int row=0; row<4; ++row)
                matrix[4*row+layers[layer][row]]++;
        legal_matrices.insert(matrix);
    }
    if (legal_matrices.size()!=4475) return 2;

    vector<Matrix> face;
    for (auto const& matrix : legal_matrices)
        if (score(matrix)==0) face.push_back(matrix);
    if (face.size()!=495) return 3;

    const Matrix source={2,1,1,0, 0,2,1,1, 1,0,2,1, 1,1,0,2};
    const Matrix hidden={4,0,0,0, 0,4,0,0, 0,0,4,0, 0,0,0,4};
    Matrix target{};
    for (int index=0; index<16; ++index)
        target[index]=8*source[index]-3*hidden[index];

    unordered_map<Matrix,vector<pair<int,int>>,MatrixHash> pair_sums;
    pair_sums.reserve(face.size()*face.size()/2);
    for (int first=0; first<static_cast<int>(face.size()); ++first)
    for (int second=first; second<static_cast<int>(face.size()); ++second) {
        Matrix sum{};
        for (int index=0; index<16; ++index)
            sum[index]=face[first][index]+face[second][index];
        pair_sums[sum].push_back({first,second});
    }
    if (pair_sums.size()!=12870) return 4;

    long long solutions=0;
    map<int,long long> support_histogram;
    map<array<int,5>,long long> multiplicity_histogram;
    const int face_count=static_cast<int>(face.size());
    for (int third=0; third<face_count; ++third)
    for (int fourth=third; fourth<face_count; ++fourth)
    for (int fifth=fourth; fifth<face_count; ++fifth) {
        Matrix remainder{};
        for (int index=0; index<16; ++index)
            remainder[index]=target[index]-face[third][index]-face[fourth][index]-face[fifth][index];
        auto iterator=pair_sums.find(remainder);
        if (iterator==pair_sums.end()) continue;
        for (auto [first,second] : iterator->second) if (second<=third) {
            array<int,5> indices={first,second,third,fourth,fifth};
            solutions++;
            int support=1;
            for (int index=1; index<5; ++index)
                support += indices[index]!=indices[index-1];
            support_histogram[support]++;

            array<int,5> multiplicities{};
            int slot=0, count=1;
            for (int index=1; index<=5; ++index) {
                if (index<5 && indices[index]==indices[index-1]) count++;
                else { multiplicities[slot++]=count; count=1; }
            }
            sort(multiplicities.begin(),multiplicities.end(),greater<int>());
            multiplicity_histogram[multiplicities]++;
        }
    }

    const map<int,long long> expected_support={{2,5},{3,210},{4,2255},{5,17364}};
    const map<array<int,5>,long long> expected_multiplicity={
        {{{1,1,1,1,1}},17364},
        {{{2,1,1,1,0}},2255},
        {{{2,2,1,0,0}},175},
        {{{3,1,1,0,0}},35},
        {{{4,1,0,0,0}},5},
    };
    if (solutions!=19834) return 5;
    if (support_histogram!=expected_support) return 6;
    if (multiplicity_histogram!=expected_multiplicity) return 7;

    cout << "legal_layers=18 legal_matrices=4475 face=495 pair_sums=12870\n";
    cout << "minimal_equal_weight_batches=" << solutions << " support";
    for (auto [support,count] : support_histogram) cout << " " << support << ":" << count;
    cout << "\npartitions 11111:17364 2111:2255 221:175 311:35 41:5\n";
}
