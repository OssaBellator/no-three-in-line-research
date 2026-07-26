// Exact radius-three selector-layer census for PX546--PX550.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <unordered_set>
#include <vector>

constexpr int PAIRS[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
using Selector=std::array<std::uint16_t,14>;

struct SelectorHash {
    std::size_t operator()(const Selector& selector) const noexcept {
        std::uint64_t hash=1469598103934665603ULL;
        for(std::uint16_t row:selector){hash^=row;hash*=1099511628211ULL;}
        return hash;
    }
};

struct CaseData {
    std::string name;
    std::array<int,7> h;
    std::array<int,7> p;
    std::array<int,14> options;
    int expected_radius_one;
    int expected_radius_two;
    int expected_radius_three;
    std::uint64_t expected_directed_three;
    std::map<int,std::size_t> expected_histogram;
};

const std::array<CaseData,2> CASES={{
    {
        "cycle322",
        {1,2,0,4,3,6,5},
        {4,6,5,3,1,2,0},
        {5,0,3,1,0,5,0,5,5,0,4,3,5,0},
        112,
        4433,
        77026,
        632828ULL,
        {{12,6604},{14,11096},{16,17677},{18,18264},{20,13126},
         {22,6928},{24,2891},{26,400},{28,40}}
    },
    {
        "cycle43",
        {1,2,3,0,5,6,4},
        {3,5,4,2,1,0,6},
        {5,5,2,0,0,5,2,0,0,5,5,0,3,3},
        180,
        10531,
        231765,
        3813896ULL,
        {{12,3950},{14,3288},{16,14526},{18,22964},{20,30306},
         {22,41168},{24,36290},{26,40456},{28,21200},{30,12756},
         {32,3457},{34,1404}}
    }
}};

Selector centre_selector(const CaseData& data){
    Selector selector{};
    for(int scalar_row=0;scalar_row<14;++scalar_row){
        int outer=scalar_row/7;
        int fine=scalar_row%7;
        int label=outer?data.p[fine]:fine;
        int adjacency[4]={label,data.h[label],7+label,7+data.h[label]};
        int abstract_row=7*outer+label;
        for(int index=0;index<2;++index){
            selector[abstract_row]|=1u<<adjacency[PAIRS[data.options[scalar_row]][index]];
        }
    }
    return selector;
}

std::array<std::uint16_t,14> abstract_host(const CaseData& data){
    std::array<std::uint16_t,14> host{};
    for(int outer=0;outer<2;++outer){
        for(int label=0;label<7;++label){
            host[7*outer+label]=(1u<<label)|(1u<<data.h[label])
                |(1u<<(7+label))|(1u<<(7+data.h[label]));
        }
    }
    return host;
}

struct CycleEnumerator {
    Selector selector{};
    std::array<std::uint16_t,14> host{};
    std::array<std::uint16_t,14> selected_rows_at_column{};
    std::unordered_set<Selector,SelectorHash> neighbours;
    std::vector<int> rows;
    std::vector<int> columns;
    int start_row=0;

    void search(int row,std::uint16_t used_rows,std::uint16_t used_columns){
        std::uint16_t unselected=host[row]&~selector[row];
        while(unselected){
            int column=__builtin_ctz(unselected);
            unselected&=unselected-1;
            if(used_columns>>column&1u)continue;
            std::uint16_t next_rows=selected_rows_at_column[column];
            while(next_rows){
                int next_row=__builtin_ctz(next_rows);
                next_rows&=next_rows-1;
                if(next_row==start_row){
                    if(rows.size()<2)continue;
                    Selector flipped=selector;
                    for(std::size_t index=0;index<columns.size();++index){
                        int old_column=columns[index];
                        flipped[rows[index]]^=1u<<old_column;
                        flipped[rows[index+1]]^=1u<<old_column;
                    }
                    flipped[rows.back()]^=1u<<column;
                    flipped[start_row]^=1u<<column;
                    neighbours.insert(flipped);
                }else if(!(used_rows>>next_row&1u)&&next_row>=start_row){
                    rows.push_back(next_row);
                    columns.push_back(column);
                    search(next_row,used_rows|(1u<<next_row),used_columns|(1u<<column));
                    columns.pop_back();
                    rows.pop_back();
                }
            }
        }
    }

    void run(){
        selected_rows_at_column.fill(0);
        neighbours.clear();
        for(int column=0;column<14;++column){
            for(int row=0;row<14;++row){
                if(selector[row]>>column&1u)selected_rows_at_column[column]|=1u<<row;
            }
        }
        for(start_row=0;start_row<14;++start_row){
            rows={start_row};
            columns.clear();
            search(start_row,1u<<start_row,0);
        }
    }
};

void verify_case(const CaseData& data){
    Selector centre=centre_selector(data);
    CycleEnumerator enumerator;
    enumerator.selector=centre;
    enumerator.host=abstract_host(data);
    enumerator.run();
    assert(static_cast<int>(enumerator.neighbours.size())==data.expected_radius_one);
    auto radius_one=enumerator.neighbours;

    std::unordered_set<Selector,SelectorHash> radius_two;
    for(const Selector& parent:radius_one){
        enumerator.selector=parent;
        enumerator.run();
        for(const Selector& child:enumerator.neighbours){
            if(child!=centre&&!radius_one.count(child))radius_two.insert(child);
        }
    }
    assert(static_cast<int>(radius_two.size())==data.expected_radius_two);

    std::unordered_set<Selector,SelectorHash> radius_three;
    std::uint64_t directed=0;
    for(const Selector& parent:radius_two){
        enumerator.selector=parent;
        enumerator.run();
        directed+=enumerator.neighbours.size();
        for(const Selector& child:enumerator.neighbours){
            if(child==centre||radius_one.count(child)||radius_two.count(child))continue;
            radius_three.insert(child);
        }
    }
    assert(directed==data.expected_directed_three);
    assert(static_cast<int>(radius_three.size())==data.expected_radius_three);

    std::map<int,std::size_t> histogram;
    for(const Selector& selector:radius_three){
        int difference=0;
        for(int row=0;row<14;++row){
            difference+=__builtin_popcount(selector[row]^centre[row]);
        }
        ++histogram[difference];
    }
    assert(histogram==data.expected_histogram);
    std::cout<<data.name<<": radius3="<<radius_three.size()
             <<" directed="<<directed
             <<" support12="<<histogram.at(12)<<" PASS\n";
}

int main(int argc,char** argv){
    assert(argc==2);
    std::string requested=argv[1];
    for(const CaseData& data:CASES){
        if(requested==data.name){verify_case(data);return 0;}
    }
    assert(false&&"unknown completed side-seven class");
}
