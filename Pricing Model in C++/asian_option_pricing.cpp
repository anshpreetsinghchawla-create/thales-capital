#include <iostream>
// monte carlo pricer for arithematic asian options

double S0; // initial stock price
double K;  // strike price
double r = 0.03;  // risk free rate
double vol; // volatility   
double T;  // time to maturity
int N;    // number of time steps
int paths; // number of monte carlo paths

int main(){

    std::cout << "Enter Strike Price (K)    : ";
    std::cin >> K;
    std::cout << "Enter Time to Maturity (T)    : ";
    std::cin >> T;
    std::cout << "Enter number of time steps (N)    : ";
    std::cin >> N;
    std::cout << "Enter number of monte carlo paths    : ";
    std::cin >> paths;




}