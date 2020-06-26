//Annie Zhu
//acz2npn
//4.21.2020

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <list>
using namespace std;
/**
 * @brief Node class
 */
class Node{
public: 
    string value;
    int indegree;
    list<Node*> adjacent;
/**
 * @brief Constructor of Node
  *
 * @param v the value of the Node
 * @param i the indegree of the Node
 */
    Node(string v, int i){
        value=v;
        indegree=i;
    }
};

vector<Node*> graph;
/**
 * @brief Sort the graph
 * @details This function performs a topological sort on the global graph.
 * A topological sort of a directed acyclic graph is a linear listing of the 
 * vertices such that, for all pairs of vertices, the starting vertice is listed before
 * the ending vertice in the sort.
 */

void topologicalsort(){
    queue<Node*> q;
    int counter=0;
    for (Node* name: graph){
        if(name->indegree==0){
            q.push(name);
        }
    }
    while(!q.empty()){
        Node* x=q.front();
        q.pop();
        cout<<x->value<<" ";
        counter+=1;
        for (Node* name:x->adjacent){
            name->indegree-=1;
            if(name->indegree==0){
                q.push(name);
            }
        }
    }
    if (counter!=graph.size()){
        cout<<"Cycle Found!"<<endl;
    }

}
/**
 * @brief Add an edge to the graph
* @details This function takes in an edge in the form of two strings. The first string
* represents the value of the starting node and the second string represents the value
* of the ending node. We do not need to pass in our graph as it was declared a global variable.
 * @param x the value of the starting node
 * @param y the value of the ending node
 */
void addToGraph(string x, string y){
//if start is in graph, then do not do anything
//if the start is not in the graph, then we have to push a new node* into the graph with in degree 0
//if the end is in the graph, then we increase indegree
//if the end is not in the graph, then we have to push a new node* into the graph with indegree 1
    for(Node* temp:graph){
        if (temp->value==x){
            for(Node* temp2:graph){
                if(temp2->value==y){
                    temp2->indegree+=1;
                    temp->adjacent.push_back(temp2);
                    return;
                }
            }
            //end of edge is not in the graph
            Node* bobby=new Node(y,1);
            graph.push_back(bobby);
            temp->adjacent.push_back(bobby);
            return;
        }
    }
    //beginning of edge is not in the graph
    Node* billy=new Node(x,0);
    graph.push_back(billy);
    for(Node* temp:graph){
        if(temp->value==y){
            temp->indegree+=1;
            billy->adjacent.push_back(temp);
            return;
        }
    }
    //end of edge is not in the graph
    Node* bobby=new Node(y,1);
    graph.push_back(bobby);
    billy->adjacent.push_back(bobby);
    return;
}
/**
* @brief Prints out the graph by each Node and its adjacent Nodes
*/
void printGraph(){
    for(Node* temp:graph){
        cout<<temp->value<<" : ";
        for (Node* temp2:temp->adjacent){
            cout<<temp2->value<<" ";
        }
        cout<<"\n";
    }    
}
/**
* @brief Cleans the graph so that there are no memory leaks
*/
void cleanGraph(){
    for (Node* temp: graph){
            delete(temp);}
    

}
int main(int argc, char** argv) {
    if (argc != 2) {
        cout << "Must supply the input file name as the one and only parameter" << endl;
        exit(1);
    }
    ifstream file(argv[1], ifstream::binary);
    if (!file.is_open()) {
        cout << "Unable to open file '" << argv[1] << "'." << endl;
        exit(2);
    }
    string s1, s2;
    while (!file.eof()){
        file >> s1;
        file >> s2;
        if (s1=="0" && s2=="0"){
            break;
        }
        addToGraph(s1,s2);
    }
    //printGraph();
    //cout<<"\n";
    topologicalsort();
    cout<<"\n";
    file.close();
    cleanGraph();
}