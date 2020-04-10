#include <fstream>
#include <string>
#include <iostream>
#include <time.h>
#include <random>
#include <vector>

struct edge {
	int V1;
	int V2;
	edge(int x, int y) : V1(x), V2(y){}
};

bool indexExists(std::vector<int> edgeIndexes, int index) {
	for (unsigned int i = 0; i < edgeIndexes.size(); i++) {
		if (edgeIndexes[i] == index)
			return true;
	}
	return false;
}

//generates n graphs with V vertices each and writes them to file f
void generateGraph(int V, int n, std::string f) {
	//open file
	std::ofstream output;
	output.open(f);
	if (output.fail()) {
		std::cout << "File cannot open!";
		return;
	}

	//generate all the possible edges
	std::vector<edge> graph;
	for (int i = 0; i < V; i++) {
		for (int j = i + 1; j < V; j++) {
			edge e(i, j);
			graph.push_back(e);
		}
	}
	int totalNumEdges = graph.size();

	//create n different graphs
	for (int i = 0; i < n; i++) {
		//select at least V many at most all edges
		//int numEdges = rand() % (totalNumEdges - V + 1) + V;
		int numEdges = rand() % totalNumEdges + 1;

		//select edges randomly
		std::vector<int> edgeIndexes;
		for (int j = 0; j < numEdges; j++) {
			int index = rand() % totalNumEdges;
			if (indexExists(edgeIndexes, index))
				j--;
			else
				edgeIndexes.push_back(index);
		}

		//create the random graph
		std::vector<edge> randomGraph;
		for (int j = 0; j < numEdges; j++)
			randomGraph.push_back(graph[edgeIndexes[j]]);

		//write the graph into the txt file
		for (int j = 0; j < numEdges; j++)
			output << randomGraph[j].V1 << " " << randomGraph[j].V2 << " ";
		output << "\n";

		//clear the vectors
		edgeIndexes.clear();
		randomGraph.clear();
	}

	//close file
	output.close();
}


int main() {
	srand(time(0));

	//parameters
	int numVertices[8] = { 5, 6, 7, 8, 9, 10, 15, 20 };
	int numGraphs[5] = { 100, 1000, 3000, 5000, 10000 };

	//create txt files
	for (int i = 0; i < 8; i++) {
		std::string vertexNum = std::to_string(numVertices[i]);
		for (int j = 0; j < 5; j++) {
			std::string graphNum = std::to_string(numGraphs[j]);
			std::string fileName = "vertex" + vertexNum + "graph" + graphNum + "3.txt";
			generateGraph(numVertices[i], numGraphs[j], fileName);
			std::cout << numVertices[i] << " vertex " << numGraphs[j] << " graph --- DONE!\n";
		}
	}

	std::cin.get();
	std::cin.ignore();
	return 0;
}