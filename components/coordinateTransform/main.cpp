#include <iostream>
#include <filesystem>

struct latLonPos
{
  double lat{};
  double lon{};
};

double calcDiffLat(double fromLat, double toLat)
{
  return fromLat - toLat;
}

double calcDiffLon(double fromLon, double toLon)
{
  return fromLon - toLon;
}

int main()
{
  std::cout << "hello holoWorld" << std::endl;
}
