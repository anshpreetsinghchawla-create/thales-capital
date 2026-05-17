#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>
#include <cstdlib>

// pricing asian option (also called an average-rate option) - exotic option
// types - arithmetic and geomatric average Asian options
// payoff = max(S-K, 0), S is average price & K is strike price

int main(){
double S0 = 100; // initial stock price
double K; // strike price
double r = 0.06; //risk free rate
double vol = 0.5; //volatility
double T = 1; //time to maturity
int steps = 100; //number of time steps per path
int sims = 1000; // number of simulations
double dt = T/steps;

std::vector<double> prices(steps + 1);
prices[0] = S0;
for(int i = 1; i <= steps; i++){

// using Box-Muller transformation 
double u1 = (double) rand() / RAND_MAX;
double u2 = (double) rand() / RAND_MAX;
double Z = sqrt(-2.0 * log(u1)) * cos(2.0 * M_PI * u2);
// for fat tails, which are visible in real world returns

// assuming there is no option of eaarly exerice

prices[i] = prices[i-1] * exp((r - 0.5*vol*vol)*dt + vol*(sqrt(dt)*Z));

 }




return 0;
}
 

