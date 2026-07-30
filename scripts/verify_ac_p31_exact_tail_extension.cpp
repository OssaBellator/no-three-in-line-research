#include <bits/stdc++.h>
using namespace std;

struct Line {
    int a,b,c;
    bool operator==(Line const& o) const { return a==o.a && b==o.b && c==o.c; }
};
struct LineHash {
    size_t operator()(Line const& x) const noexcept {
        return ((uint64_t)(x.a+100)<<42)^((uint64_t)(x.b+100)<<32)^(uint32_t)(x.c+100000);
    }
};
struct Move { int layer,i,j; };

vector<int> pairLine;
vector<unsigned char> lineCount;
vector<int> touched;
int choose3[1771];

Line canonical_line(int x1,int y1,int x2,int y2) {
    int A=y2-y1, B=x1-x2, C=A*x1+B*y1;
    int g=gcd(abs(A),gcd(abs(B),abs(C)));
    A/=g; B/=g; C/=g;
    if(A<0 || (A==0 && B<0)) { A=-A; B=-B; C=-C; }
    return {A,B,C};
}

void init_lines() {
    unordered_map<Line,int,LineHash> ids;
    ids.reserve(500000);
    pairLine.assign(810000,-1);
    int next=0;
    for(int u=0;u<900;u++) for(int v=u+1;v<900;v++) {
        auto line=canonical_line(u/30,u%30,v/30,v%30);
        auto [it,inserted]=ids.emplace(line,next);
        if(inserted) next++;
        pairLine[u*900+v]=pairLine[v*900+u]=it->second;
    }
    lineCount.assign(next,0);
    touched.reserve(1770);
    memset(choose3,0,sizeof(choose3));
    for(int k=0;k<=60;k++) choose3[k*(k-1)/2]=k*(k-1)*(k-2)/6;
}

string state_from(vector<int> const& r, vector<int> const& b) {
    string s;
    for(int x:r) s.push_back((char)x);
    for(int x:b) s.push_back((char)x);
    return s;
}

int potential(string const& s) {
    int cells[60];
    for(int i=0;i<30;i++) {
        cells[2*i]=30*i+(unsigned char)s[i]-1;
        cells[2*i+1]=30*i+(unsigned char)s[30+i]-1;
    }
    touched.clear();
    for(int i=0;i<60;i++) for(int j=i+1;j<60;j++) {
        int id=pairLine[cells[i]*900+cells[j]];
        if(lineCount[id]++==0) touched.push_back(id);
    }
    int answer=0;
    for(int id:touched) {
        answer += choose3[lineCount[id]];
        lineCount[id]=0;
    }
    return answer;
}

bool legal(string const& s, Move m) {
    int own=30*m.layer, other=30*(1-m.layer);
    return (unsigned char)s[own+m.j]!=(unsigned char)s[other+m.i]
        && (unsigned char)s[own+m.i]!=(unsigned char)s[other+m.j];
}

string apply(string s, Move m) {
    assert(legal(s,m));
    swap(s[30*m.layer+m.i],s[30*m.layer+m.j]);
    return s;
}

vector<int> replay(string& s, vector<Move> const& moves) {
    vector<int> values={potential(s)};
    for(auto m:moves) {
        s=apply(s,m);
        values.push_back(potential(s));
    }
    return values;
}

size_t component_size(string const& start, int barrier) {
    unordered_set<string> seen;
    seen.reserve(10000);
    vector<string> queue;
    queue.push_back(start);
    seen.insert(start);
    for(size_t pos=0;pos<queue.size();pos++) {
        string s=queue[pos];
        for(int layer=0;layer<2;layer++) for(int i=0;i<30;i++) for(int j=i+1;j<30;j++) {
            Move m{layer,i,j};
            if(!legal(s,m)) continue;
            string z=s;
            swap(z[30*layer+i],z[30*layer+j]);
            if(seen.count(z)) continue;
            if(potential(z)>barrier) continue;
            seen.insert(z);
            queue.push_back(move(z));
        }
    }
    return queue.size();
}

int main() {
    init_lines();
    vector<int> r6={19,15,26,18,23,17,8,2,25,13,9,4,20,28,1,12,7,24,29,5,3,30,27,11,14,6,21,16,22,10};
    vector<int> b6={12,10,23,9,7,15,26,6,21,1,20,2,8,29,30,16,27,25,3,11,14,18,4,5,22,28,24,13,17,19};
    vector<Move> m65={{0,0,5},{0,5,17},{1,7,10},{1,5,7},{1,5,17},{0,1,5},{1,17,26},{1,6,22},{1,1,25},{1,1,7},{0,1,12},{0,0,3},{1,12,26},{0,2,6},{1,6,26},{1,22,26},{0,0,3},{0,2,12},{1,2,26},{0,6,11},{1,11,22},{0,7,11},{0,7,25},{0,20,25},{1,18,23},{1,19,26}};
    vector<Move> m54={{0,19,23},{1,2,22},{1,23,26},{1,18,19},{1,2,7},{1,2,8},{0,7,13},{1,18,22},{0,20,23},{0,1,13},{0,1,25},{0,1,29},{0,20,29},{0,20,23},{1,2,22},{0,2,26},{1,22,26},{1,10,22},{0,23,29},{0,1,29},{0,1,25},{0,20,23},{0,1,10},{0,1,29},{0,5,29},{1,1,5},{0,1,29},{1,3,10},{0,3,5},{1,3,21},{1,21,26},{0,2,26}};
    vector<int> expected65={6,7,7,8,10,10,10,9,9,10,7,9,10,8,10,10,9,10,10,9,9,8,10,9,8,8,5};
    vector<int> expected54={5,7,10,10,9,10,9,10,9,10,10,9,10,10,10,9,10,10,8,10,8,10,10,10,10,9,10,7,10,10,10,8,4};

    string s=state_from(r6,b6);
    assert(potential(s)==6);
    auto actual65=replay(s,m65);
    assert(actual65==expected65);
    string state5=s;
    assert(potential(state5)==5);
    assert(component_size(state5,6)==2);
    assert(component_size(state5,7)==18);
    assert(component_size(state5,8)==68);
    assert(component_size(state5,9)==501);

    auto actual54=replay(s,m54);
    assert(actual54==expected54);
    string state4=s;
    assert(potential(state4)==4);
    assert(component_size(state4,5)==2);
    assert(component_size(state4,6)==10);
    assert(component_size(state4,7)==29);
    assert(component_size(state4,8)==286);
    assert(component_size(state4,9)==2033);

    cout << "AC p=31 exact tail extension audit\n";
    cout << "six_to_five_switches: " << m65.size() << "\n";
    cout << "six_to_five_maximum: " << *max_element(actual65.begin(),actual65.end()) << "\n";
    cout << "five_to_four_switches: " << m54.size() << "\n";
    cout << "five_to_four_maximum: " << *max_element(actual54.begin(),actual54.end()) << "\n";
    cout << "five_checkpoint_lower_components: 2,18,68,501\n";
    cout << "four_checkpoint_lower_components: 2,10,29,286,2033\n";
    cout << "extension_switches: " << m65.size()+m54.size() << "\n";
    cout << "cumulative_switches_from_AN_successor: 212\n";
    cout << "final_potential: " << potential(state4) << "\n";
}
