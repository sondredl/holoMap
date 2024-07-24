#include <iostream>
#include <filesystem>

struct latLonPos
{
  double Lat{};
  double Lon{};
};

struct metricVector
{
  double XDelta;
  double YDelta;
  double ZDelta;
};

double CalcDiffLat(double fromLat, double toLat)
{
  return fromLat - toLat;
}

double CalcDiffLon(double fromLon, double toLon)
{
  return fromLon - toLon;
}

int main()
{
  latLonPos start{};
  start.Lat = 0.0000;
  start.Lon = 0.0100;

  latLonPos end{};
  end.Lat = 0.0100;
  end.Lon = 0.0000;
}
