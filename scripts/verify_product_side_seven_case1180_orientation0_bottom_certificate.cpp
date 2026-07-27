#include "product_side_seven_cache_engine.hpp"
#include <cstring>

struct CertHeader {
    char magic[8];
    uint32_t version;
    uint32_t global_case;
    uint32_t orientation;
    uint32_t candidate_count;
    uint32_t permutation_count;
    int8_t top_assignment[SIDE];
    uint64_t transcript_digest;
};

static uint64_t mix64(uint64_t h,uint64_t v){h^=v;return h*1099511628211ULL;}

static std::vector<int> state_edges(State const&s){
    std::vector<int> e;
    for(int r=0;r<SIDE;++r){uint16_t m=s[r];while(m){int c=__builtin_ctz(unsigned(m));m&=uint16_t(m-1);e.push_back(SIDE*r+c);}}
    return e;
}

static Point point_for_edge(int edge, Assignment const&top, std::array<int8_t,N> const&bottom,int orientation){
    int row=edge/SIDE,c=edge%SIDE;
    int y=orientation%2==0?N*(c/N)+top[c]:2*top[c]+c/N;
    int x;
    if(row<N) x=orientation<2?row:2*row;
    else x=orientation<2?N+bottom[row%N]:2*bottom[row%N]+1;
    return {x,y};
}

static std::array<uint8_t,3> first_bad_triple(State const&s,Assignment const&top,std::array<int8_t,N>const&bottom,int orientation){
    auto edges=state_edges(s); assert(edges.size()==28);
    for(size_t i=0;i<edges.size();++i)for(size_t j=i+1;j<edges.size();++j)for(size_t k=j+1;k<edges.size();++k){
        auto a=point_for_edge(edges[i],top,bottom,orientation),b=point_for_edge(edges[j],top,bottom,orientation),c=point_for_edge(edges[k],top,bottom,orientation);
        if(det(a,b,c)==0)return {uint8_t(edges[i]),uint8_t(edges[j]),uint8_t(edges[k])};
    }
    std::cerr<<"survivor candidate\n";std::abort();
}

static void locate_case(std::vector<State>const&layer,int wanted,Signature&sig,std::vector<State>&group){
    std::map<Signature,std::vector<State>>groups;
    for(auto const&s:layer){Signature x{};for(int i=0;i<N;++i)x[i]=s[i];groups[x].push_back(s);}
    int idx=0;
    for(auto const&[x,g]:groups)if((int)g.size()==4){if(idx==wanted){sig=x;group=g;std::sort(group.begin(),group.end());return;}++idx;}
    std::abort();
}

static int generate(char const*path){
    auto layer=generate_layer();
    Signature sig{};std::vector<State>group;locate_case(layer,1180,sig,group);
    TopEnumerator top;top.sig=sig;top.run(0);assert(!top.solutions.empty());Assignment chosen=top.solutions.front();
    CertHeader h{};std::memcpy(h.magic,"NTLCERT",7);h.version=1;h.global_case=1180;h.orientation=0;h.candidate_count=4;h.permutation_count=5040;for(int i=0;i<SIDE;++i)h.top_assignment[i]=chosen[i];
    std::vector<std::array<uint8_t,3>>records;records.reserve(5040*4);
    std::array<int8_t,N>perm{};for(int i=0;i<N;++i)perm[i]=i;
    uint64_t digest=1469598103934665603ULL;uint32_t pi=0;
    do{
        digest=mix64(digest,pi++);for(auto v:perm)digest=mix64(digest,uint8_t(v));
        for(int ci=0;ci<4;++ci){auto t=first_bad_triple(group[ci],chosen,perm,0);records.push_back(t);digest=mix64(digest,ci);for(auto v:t)digest=mix64(digest,v);}
    }while(std::next_permutation(perm.begin(),perm.end()));
    assert(pi==5040);assert(digest==16630590496048926721ULL);h.transcript_digest=digest;
    std::ofstream f(path,std::ios::binary);f.write((char*)&h,sizeof h);f.write((char*)records.data(),records.size()*sizeof(records[0]));f.close();
    std::cout<<"generated records="<<records.size()<<" bytes="<<(sizeof h+records.size()*3)<<" digest="<<digest<<"\n";return 0;
}

static int check(char const*path){
    auto layer=generate_layer();
    Signature sig{};std::vector<State>group;locate_case(layer,1180,sig,group);
    std::ifstream f(path,std::ios::binary);CertHeader h{};f.read((char*)&h,sizeof h);assert(std::memcmp(h.magic,"NTLCERT",7)==0&&h.version==1&&h.global_case==1180&&h.orientation==0&&h.candidate_count==4&&h.permutation_count==5040);
    TopEnumerator top;top.sig=sig;top.run(0);assert(!top.solutions.empty());Assignment chosen=top.solutions.front();for(int i=0;i<SIDE;++i)assert(h.top_assignment[i]==chosen[i]);
    std::array<int8_t,N>perm{};for(int i=0;i<N;++i)perm[i]=i;uint64_t digest=1469598103934665603ULL;uint32_t pi=0;
    do{
        digest=mix64(digest,pi++);for(auto v:perm)digest=mix64(digest,uint8_t(v));
        for(int ci=0;ci<4;++ci){std::array<uint8_t,3>t{};f.read((char*)t.data(),3);assert(f);auto edges=state_edges(group[ci]);for(auto e:t)assert(std::binary_search(edges.begin(),edges.end(),int(e)));auto a=point_for_edge(t[0],chosen,perm,0),b=point_for_edge(t[1],chosen,perm,0),c=point_for_edge(t[2],chosen,perm,0);assert(det(a,b,c)==0);digest=mix64(digest,ci);for(auto v:t)digest=mix64(digest,v);}
    }while(std::next_permutation(perm.begin(),perm.end()));
    assert(pi==5040&&digest==h.transcript_digest&&digest==16630590496048926721ULL);char extra;assert(!f.read(&extra,1));
    std::cout<<"certificate_digest="<<digest<<" permutations=5040 candidates=4 PASS\n";return 0;
}

int main(int argc,char**argv){if(argc!=3){std::cerr<<"generate|check path\n";return 2;}return std::string(argv[1])=="generate"?generate(argv[2]):check(argv[2]);}
