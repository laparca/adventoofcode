#include <iostream>
#include <vector>
#include <algorithm>

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

	unsigned long long  total_distance = 0;
	for (int i = 0; i < left.size(); ++i) {
		total_distance += std::abs(left[i] - right[i]);
	}

	std::cout << "There where " << left.size() << " lines" << std::endl;
	std::cout << "The distance is " << total_distance << std::endl;

	return 0;
}
