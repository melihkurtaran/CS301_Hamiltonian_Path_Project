#include <iostream>
#include <string.h>
#include <algorithm>
#include <list>
#include<stdio.h>
#include<fstream>
#include<vector>
#include<sstream>
#include<chrono>
#include<cmath>
int n;
using namespace std;
 
class Hamiltonian
{
	int *path,v,x;
	public:
		Hamiltonian(int n){ v = 0; x = 0; path = new int[n]; }
		bool isSafe(bool graph[][25], int pos);
		bool hamCycleUtil(bool graph[][25], int pos, int i);
		bool hamCycle(bool graph[][25]);
		void printSolution();
};

bool Hamiltonian::isSafe(bool graph[][25], int pos)
{
    if (graph [ path[pos-1] ][ v ] == 0)
        return false;
 
     for (int i = 0; i < pos; i++)
        if (path[i] == v)
            return false;
 
    return true;
}
 
bool Hamiltonian::hamCycleUtil(bool graph[][25], int pos, int i)
{
    if (pos == n)
    {
        if ( graph[ path[pos-1] ][ path[0] ] == 1 )
        {
        	//cout<<"Hamiltonian cycle exists\n";
        	x = 1;return true;
    	}
        else
         return true;
    }
 
    for (v = 0; v < n; v++)
    {
    	if(v == i)
    		continue;
        if (isSafe(graph, pos))
        {
            path[pos] = v;
 
            if (hamCycleUtil (graph, pos+1, i) == true)
                return true;
 
            path[pos] = -1;
        }
    }
 
    return false;
}
 
bool Hamiltonian::hamCycle(bool graph[][25])
{
    for (int i = 0; i < n; i++)
        path[i] = -1;

    for(int i=0;i < n; i++)
    {
	path[0] = i;
    if ( hamCycleUtil(graph, 1,i) == true )
    {
		//printSolution();
    	return true;
    }
	}
   // cout<<"\nNo Hamiltonian path or cycle exist";
    return false; 

}
 
void Hamiltonian::printSolution()
{
    for (int i = 0; i < n - 1; i++)
        cout << path[i] << "-" << path[i + 1] << " ";
        
 	if(x == 1)
    	cout << path[n - 1] << "-" << path[0];
    cout<<"\n";
}


int main()
{
	int i,j;
    //n = 5; 
	int arr_vertexnum[8] = {5, 6, 7, 8, 9, 10, 15, 20};
	int arr_graphnum[5] = {100, 1000, 3000, 5000, 10000};
	for(i = 0; i <8; i++){
		for(j = 0; j < 5; j++){
			int vertex_num = arr_vertexnum[i];
			int graph_num = arr_graphnum[j];
			n = vertex_num;
			int num_tot = 0;
			ifstream infile;
			string line;
			double time_tot = 0;
			double time_avg = 0;
			string v_num = static_cast<ostringstream*>( &(ostringstream() << vertex_num) )->str();
			string g_num = static_cast<ostringstream*>( &(ostringstream() << graph_num) )->str();
			string file_name = "vertex" + v_num + "graph" + g_num + "3.txt";
			infile.open(file_name);
			while(getline(infile, line))
			{
				bool graph1[25][25];
				for(int x=1;x<=n;x++)
  				for(int y=1;y<=n;y++)
   					graph1[x][y]=0;
				Hamiltonian g2(n);
				string graph = line;
				int edge_length = line.length();
				istringstream iss(line);
				int num, num2;
				int num_Edges = 0; 
				while(iss >> num >> num2){
					graph1[num + 1][num2 + 1]=1;
  					graph1[num2 + 1][num + 1]=1;			
				} auto start = chrono::steady_clock::now();
				if(g2.hamCycle(graph1) == true)num_tot++;auto end = chrono::steady_clock::now();

				time_tot =  time_tot + chrono::duration_cast<std::chrono::microseconds>(end - start).count();
			}
			time_avg = double(time_tot / (graph_num * pow(10.0, 6.0)));
			cout << "Number of Hamiltonian Paths in Test: " << "Number of Vertices = " << vertex_num << " Number of Graphs = " << graph_num << " Amount of Success: " << num_tot <<" Average Time Taken: "<< time_avg << "\n";
		}
	}}
 
