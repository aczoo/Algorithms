//Annie Zhu
//acz2npn
//4.14.2020

//1. Read the source file and determine the frequencies of the characters in the file
//2. Store the character frequencies in a heap (priority queue)
//3. Build a tree of prefix codes (a Huffman code) that determines the unique bit codes for each character
//4. Write the prefix codes to the output file, following the file format above
//5. Re-read the source file and for each character read, write its prefix code to the output, following the file format described below
//File Format:
	//1. ASCII characters that are encoded, followed by their bit encoding
	//format is the character, a single space, and then the encoding
	//separator of 40 dashes and no spaces
	//2. Encoded messsage
	//separator of 40 dashes and no spaces
	//3. Display compression ratio and the cost of the Huffman tree

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <map>
#include <vector>
#include "heap.h"
#include "heapNode.h"

using namespace std;
map<string, string> encodes;
void printPC(heapNode* current, string code);

int main(int argc, char** argv) {
     if (argc != 2) {
        cout << "Must supply the input file name as the one and only parameter" << endl;
        exit(1);
    }
    ifstream file(argv[1]);
    if (!file.is_open()) {
        cout << "Unable to open '" << argv[1] << "' for reading" << endl;
        exit(2);
    }
    //1
    char g;
    vector<char> order;
    map<char, int> dict;
    while (file.get(g)) {
    	if (dict.find(g)!= dict.end()){
    		dict[g]+=1;
    	}
    	else{
    		if(g!='\n'){
    			dict[g]=1;
    			order.push_back(g);
    		}

    	}
    }
    //2
    heap bob;
    int total=0;

 	for (auto i :order){
 		total+=dict[i];
 		heapNode* temp = new heapNode(i, dict[i]);
 		bob.insert(temp);
 	}
 	//3
 	//tree of prefix codes
 	while(bob.size()>1){
 		 heapNode* removal_1 = bob.findMin();
 		 bob.deleteMin();
  		 heapNode* removal_2 = bob.findMin();
  		 bob.deleteMin();
  		 heapNode* merged = new heapNode('=', removal_1->getFreq() + removal_2->getFreq());
  		 merged->setLeft(removal_1);
  		 merged->setRight(removal_2);
  		 bob.insert(merged);
  		}
  	//4
  	printPC(bob.findMin(),"");
  	cout << "----------------------------------------" << endl;
  	//5
    file.clear();
    file.seekg(0);
    int og=0;
    int compressedsize=0;
    while (file.get(g)) {
    	string s(1,g);
    	cout<<encodes[s]<<" ";
    	if (s!="\n")
    		{   compressedsize+=encodes[s].size();
    			og+=8;}
    }
    file.close();
    cout<<"\n";
    cout << "----------------------------------------" << endl;
    //compression ratio and cost of tree
    // ratio = (size of the original file)/(size of compressed file)
    // cost = summation p*n
    double cost=0.0;
     for (auto i: dict){
     	string s(1,i.first);
     	cost+=((double)i.second/(double)total)* encodes[s].length();
     }
    cout<<"This gives a compression ratio of "<<(double)og/compressedsize<<"."<<endl;
    cout<<"The cost of the Huffman tree is "<< cost<<" bits per character."<<endl;
}



void printPC(heapNode* current, string code){
    if(current->getLeft() ==NULL and current->getRight()==NULL){
        if (current->getData()== ' '){
            cout<<"space "<<code<<endl;
            encodes["space"]=code;
        }
        else{
        	string s(1, current->getData());
            cout<<s<<" "<<code<<endl;
            encodes[s]=code;
        }
    }
    else{
        if(current->getLeft()!=NULL){
            printPC(current->getLeft(), code+"0");
        }
        if (current->getRight()!=NULL){
            printPC(current->getRight(),code+"1");
        }
    }
}







