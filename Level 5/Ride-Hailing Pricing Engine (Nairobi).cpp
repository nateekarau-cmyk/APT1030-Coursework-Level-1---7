#include <iostream>
using namespace std;

int main(){

    float distance;
    float fare;

    cout << "Enter distance (km): ";
    cin >> distance;

    fare = 200 + (distance * 50);

    cout << "Total Fare: " << fare;

    return 0;
}