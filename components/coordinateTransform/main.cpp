#include <iostream>
#include <filesystem>

constexpr int ONE_DEGRE_OF_LATITUDE_IN_METERS = 111000;

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

double DegreesToMeters(double deltaDegrees)
{
  return deltaDegrees * ONE_DEGRE_OF_LATITUDE_IN_METERS;
}

int main()
{
  latLonPos start{};
  start.Lat = 8.5748;
  start.Lon = 0.0100;

  latLonPos end{};
  end.Lat = 8.5747;
  end.Lon = 0.0000;

  std::cout << "delta Lat degrees = " << CalcDiffLat(start.Lat, end.Lat) << std::endl;
  std::cout << "delta Lat meters = " << degreesToMeters(CalcDiffLat(start.Lat, end.Lat)) << std::endl;
}
