#include <iostream>
#include <math.h>
#include <time.h>
#include <vector>
#include <random>
#include <algorithm>
#include <omp.h>
#include <fstream>
using namespace std;

int main(){
  int num_threads = 7;
  int N = 1000;
  int numOnes = N/6;
  float mu = 1;
  float jj = 10;
  float gc = 10;

  vector<int> W;
  W.resize(N,0);
  random_device rd;
  mt19937 gen(rd());
  uniform_int_distribution<> distrib(0, N-1);

  for (int i = 0; i < numOnes; i++) {
      int index = distrib(gen);
      while (W[index] == 1) {
          // if the selected index is already 1, choose another one
          index = distrib(gen);
      }
      W[index] = 1;  // set the selected element to 1
  }

  vector<float> Vm;
  Vm.resize(N,0.0);

  vector<float> Vm_tmp;
  Vm_tmp.resize(N,0.0);

  vector<int> state;
  state.resize(N,0);
  int steps = 10000;

  std::ofstream outfile("results.txt");
  std::poisson_distribution<> distr(3);
  // outfile.open();

  for (int i = 0; i < steps; i++){
    int n_input = distr(gen);
    for (int h = 0; h < n_input; h++){
      int index = distrib(gen);
      state[index] = 1;
    }
    // std::cout << "\n";

    #pragma omp parallel for num_threads(num_threads)
    for (int j = 0; j < N-1; j++){
      float cons = mu*Vm[j];
      float sum = 0;
      for (int k = 0; k < N-1; k++){ 
        int mul = 1;
        if (k == j){ 
          mul = 0;
        }
        sum = sum + (jj*W[k] - jj*gc*(1 - W[k]))*state[k]*mul;
      }
      Vm_tmp[j] = (cons + sum) * (1 - state[j]);
    }
    std::swap(Vm, Vm_tmp);
    for (int j = 0; j < N-1; j++){
      if (Vm[j] > 1){
        state[j] = 1;
      }
      else{
        state[j] = 0;
      }
    }
    // for (int j = 0; j < 50; j++){
    //   std::cout << state[j] << " ";
    // }
    for (int j = 0; j < N-1; j++){
      outfile << state[j] << ",";
    }
    outfile << n_input;
    outfile << "\n";

  }
  outfile.close();
  

}

  

  








