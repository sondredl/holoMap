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
  latLonPos start{};
  start.lat = 0.0000;
  start.lon = 0.0100;

  latLonPos end{};
  end.lat = 0.0100;
  end.lon = 0.0000;
}
