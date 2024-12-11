#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

int main(void) {
	std::vector<int> left, right;
	do {
		int pleft, pright;
		std::cin >> pleft;
		if (std::cin.eof()) break;
		std::cin >> pright;
		if (std::cin.eof()) break;
		left.push_back(pleft);
		right.push_back(pright);
	} while(not std::cin.eof());

	std::sort(left.begin(), left.end());
	std::sort(right.begin(), right.end());


	std::map<int, int> right_processed;

	for (auto const& v : right) {
		right_processed[v] ++;
	}

	unsigned long long  total_distance = 0;
	for (auto const& v : left) {
		total_distance += v * right_processed[v];
	}

	std::cout << "There where " << left.size() << " lines" << std::endl;
	std::cout << "The distance is " << total_distance << std::endl;

	return 0;
}
