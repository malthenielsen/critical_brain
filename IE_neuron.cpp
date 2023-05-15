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
  int numOnes = N/5;
  float mu = 0.01;
  float jj = 10;
  float gc = 3.5;
  float drive = 0.01/(float)N;

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
  int steps = 50000;

  // std::ofstream outfile("results.txt");
  std::ofstream outFile("results.bin", std::ios::binary | std::ios::app);
  std::uniform_real_distribution<float> uni(0.0, 1.0);
  // outfile.open();

  for (int i = 0; i < steps; i++){


    for (int h = 0; h < N-1; h++){
      float prob = uni(gen);
      // std::cout << prob << "  " << drive << std::endl;
      if (prob < drive){
        state[h] = 1;
        
      }
    }
      
    #pragma omp parallel for num_threads(num_threads)
    for (int j = 0; j < N-1; j++){
      float cons = mu*Vm[j];
      float sum = 0;
      for (int k = 0; k < N-1; k++){ 
        int mul = 1;
        if (k == j){ 
          mul = 0;
        }
        sum = sum + (jj*(1 - W[k])/(float)N - jj*gc/(float)N*W[k])*state[k]*mul;
      }
      Vm_tmp[j] = (cons + sum) * (1 - state[j]);
      // std::cout << (1 - state[j]) << std::endl;
    }
    std::swap(Vm, Vm_tmp);
    for (int j = 0; j < N-1; j++){
      float prob = uni(gen);
      // std::cout << Vm[j] << "   ";
      if (Vm[j] > prob){
        state[j] = 1;
      }
      else{
        state[j] = 0;
      }
    }
    // for (int j = 0; j < 50; j++){
    //   std::cout << state[j] << " ";
    // }
    outFile.write(reinterpret_cast<const char*>(state.data()), state.size() * sizeof(int));
    // for (int j = 0; j < N-1; j++){
      // outfile << state[j] << ",";
    // }
    // outfile << "\n";

  }
  // outfile.close();
  outFile.close();
  

}

  

  








