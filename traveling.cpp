//Annie Zhu
//acz2npn
//4.23.2020
#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

#include "middleearth.h"

float computeDistance(MiddleEarth me, const string& start, vector<string> dests);
void printRoute(const string& start, const vector<string>& dests);
/**
* @brief the main method
* @details This program runs a brute force search for the least costly 
* that travels to each destination generated for the itinerary in Middle Earth.
* @param argc the number of arguments
* @param **argv the user input, which should contain the x-size, y-size, number of cities, random seed, and the number of cities to visit
*/
int main(int argc, char** argv) {
    // check the number of parameters
    if (argc != 6) {
        cout << "Usage: " << argv[0] << " <world_height> <world_width> "
             << "<num_cities> <random_seed> <cities_to_visit>" << endl;
        exit(0);
    }

    // we'll assume the parameters are all well-formed
    int width = stoi(argv[1]);
    int height = stoi(argv[2]);
    int num_cities = stoi(argv[3]);
    int rand_seed = stoi(argv[4]);
    int cities_to_visit = stoi(argv[5]);

    // create the world, and select your itinerary
    MiddleEarth me(width, height, num_cities, rand_seed);
    vector<string> dests = me.getItinerary(cities_to_visit);
    vector<string> minimum_dests=dests;
    float minimum=computeDistance(me, dests[0], dests);
    sort(dests.begin()+1, dests.end());
    while(next_permutation(dests.begin()+1, dests.end())){
        float temp=computeDistance(me, dests[0], dests);
        if (temp<minimum){
            minimum=temp;
            minimum_dests=dests;
        }
    }
    cout<<"Minimum path has distance "<<minimum<<":"<<endl; 
    printRoute(minimum_dests[0],minimum_dests);

    return 0;
}
/**
* @brief Return the total distance traveled in the cycle
* @details This method will compute the full distance of the cycle that starts at the 
* 'start' parameter, goes to each of the cities in the dests
* vector in order, and ends back at the 'start' parameter.
* @param me our middle earth
* @param start our starting destination
* @param dests our vector of destinations in the itinerary 
* @return the distance traveled in the ordered cycle as a float
*/

float computeDistance(MiddleEarth me, const string& start, vector<string> dests) {
    float total=0.0;
    for(int i=0;i<dests.size()-1;i++){
        total+=me.getDistance(dests[i], dests[i+1]);
    }
    total+=me.getDistance(dests.back(),start);
    return total;
}
/**
 * @brief method that prints out a route
 *
 * @details This method takes in a list of destinations and will print the entire route in the desired
 * format. It will start at the beginning of the vector and then loop back around for the starting destination.
 *
 * @param start the starting destination
 * @param dests a vector containing all cities in the itinerary
 */
// This method will print the entire route, starting and ending at the
// 'start' parameter.
// The output should be similar to:
// Erebor -> Khazad-dum -> Michel Delving -> Bree -> Cirith Ungol -> Erebor
void printRoute(const string& start, const vector<string>& dests) {
    for (int i=0; i<dests.size(); i++) {
        cout << dests[i] << " -> ";
    }
    //cout<<dests.front()<<endl;
    cout<<start<<endl;
}









