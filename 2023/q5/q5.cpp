#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <limits>
#include "../../../../../usr/include/c++/11/bits/stream_iterator.h"

unsigned long long find_lowest_location(unsigned long long seed, const std::vector<std::vector<std::vector<std::string>>> &layers)
{

    unsigned long long curr = seed;
    for (const auto &layer : layers)
    {
        for (const auto &range_map : layer)
        {
            unsigned long long destination_range = std::stoll(range_map[0]);
            unsigned long long source_range = std::stoll(range_map[1]);
            unsigned long long length_range = std::stoll(range_map[2]);
            if (curr >= source_range && curr < source_range + length_range)
            {
                curr = (curr - source_range) + destination_range;
                break;
            }
        }
    }
    return curr;
}

int main(void)
{
    std::string filename = "q5.txt";
    std::ifstream FILE(filename);

    // Lines
    std::vector<std::vector<std::string>> lines;
    std::vector<std::string> curr;
    std::string line;

    while (std::getline(FILE, line))
    {
        if (line.empty())
        {
            lines.push_back(curr);
            curr.clear();
        }
        else
        {
            curr.push_back(line);
        }
    }
    if (!curr.empty())
    {
        lines.push_back(curr);
    }

    // Seeds
    std::vector<std::string> seeds;
    std::string seed_line = lines[0][0].substr(lines[0][0].find(": ") + 2);
    std::istringstream seed_stream(seed_line);
    std::string seed;
    while (seed_stream >> seed)
    {
        seeds.push_back(seed);
    }

    std::vector<std::vector<std::vector<std::string>>> layers;
    for (size_t i = 1; i < lines.size(); ++i)
    {
        std::vector<std::vector<std::string>> layer;
        for (size_t j = 1; j < lines[i].size(); ++j)
        {
            std::istringstream iss(lines[i][j]);
            std::vector<std::string> parts(std::istream_iterator<std::string>{iss}, std::istream_iterator<std::string>());
            layer.push_back(parts);
        }
        layers.push_back(layer);
    }

    unsigned long long ans = std::numeric_limits<unsigned long long>::max();

    for (size_t i = 0; i < seeds.size(); i += 2)
    {
        unsigned long long start = std::stoll(seeds[i]);
        unsigned long long length = std::stoll(seeds[i + 1]);
        for (unsigned long long seed = start; seed < start + length; ++seed)
        {
            ans = std::min(ans, find_lowest_location(seed, layers));
            std::cout << ans << "\n";
        }
    }

    std::cout << ans << std::endl;
}