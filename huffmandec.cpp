//Annie Zhu
//acz2npn
//4/17/2020
// Read in the prefix code structure from the encoded file
// Re-create the Huffman tree from the code structure read in from the file
// Read in one bit at a time from the encoded file and move through the prefix code tree until a leaf node is reached
// Output the character stored at the leaf node
// Repeat the last two steps until the encoded file has been entirely decoded

#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include "node.h"
using namespace std;

//void printCharacter(node* current, string code);
void insertPrefix(node* t, string path, string character);
void deleteTree(node* t);
int main (int argc, char** argv) {
    if (argc != 2) {
        cout << "Must supply the input file name as the only parameter" << endl;
        exit(1);
    }

    ifstream file(argv[1], ifstream::binary);
    if (!file.is_open()) {
        cout << "Unable to open file '" << argv[1] << "'." << endl;
        exit(2);
    }
    node* tree = new node();
    // Read in the prefix code structure from the encoded file
    while (true) {
        string character, prefix;
        file >> character;
        if (character[0] == '-' && character.length() > 1) {
            break;
        }

        if (character == "space") {
            character = " ";
        }
        file >> prefix;
        insertPrefix(tree, prefix, character);
    }
    // read in the second section of the file: the encoded message
    stringstream sstm;
    while (true) {
        string bits;
        // read in the next set of 1's and 0's
        file >> bits;
        // check for the separator
        if (bits[0] == '-') {
            break;
        }
        // add it to the stringstream
        sstm << bits;
    }
    string allbits = sstm.str();
    file.close();
    node* temp = tree;
    for(int i=0;i<allbits.length();i++){
        if(allbits.at(i)=='1'){
            temp=temp->right;
        }
        else if(allbits.at(i)=='0'){
            temp=temp->left;
        }
        if(temp->right==NULL and temp->left==NULL){
            cout<<temp->getData();
            temp=tree;
        }
      }
      cout<<"\n";
      deleteTree(tree);


}

//No longer needed, thought would traverse the encoded file by each prefix haha!
/*void printCharacter(node* current, string code){
    if(code.length()==1){
       string val;
       if(code=="0"){
            val=current->left->getData();
       }
       else{
            val=current->left->getData();
       }
       if (val=="-"){
        cout<<"\n ERROR DID NOT FIND VALUE"<<endl;
       }
       else{
        cout<<val;
       }

    }else{
        if (code.at(0)=='0'){
            printCharacter(current->left,code.substr(1));
        }
        else{
            printCharacter(current->right,code.substr(1));
        }
    }
}*/
void deleteTree(node* t){
    if (t == NULL) return;  
    deleteTree(t->left);  
    deleteTree(t->right);  
    free(t); 
}
void insertPrefix(node* t, string path, string character){
    if (path.length()==1){
        node* newinsert= new node(character);
        if (path=="0"){
            t->left=newinsert;
        }
        else{
            t->right=newinsert;
        }
    }
    else{
        if (path.at(0)=='0'){
            if (t->left==NULL){
                node* newinsert= new node();
                t->left=newinsert;
            }
            insertPrefix(t->left,path.substr(1),character);
        }
        else{
            if (t->right==NULL){
                node* newinsert= new node();
                t->right=newinsert;
            }
            insertPrefix(t->right,path.substr(1),character);
        }
    }
}
