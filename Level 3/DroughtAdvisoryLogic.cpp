#include <iostream>
using namespace std;

int main() {

    float rainfall;
    float temperature;

    cout << "Enter rainfall amount (mm): ";
    cin >> rainfall;

    cout << "Enter temperature (C): ";
    cin >> temperature;

    if(rainfall < 200) {
        cout << "Irrigation Required";
    }
    else if(rainfall >= 200 && temperature > 30) {
        cout << "Monitor Soil";
    }
    else {
        cout << "Normal Conditions";
    }

    return 0;
}