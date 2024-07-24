#include <iostream>
#include <filesystem>
#include <math.h>

// constexpr int ONE_DEGRE_OF_LATITUDE_IN_METERS = 111000;
constexpr int ONE_DEGRE_OF_LATITUDE_IN_METERS = 111320;

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

double CalcDiffLon(double fromLat, double toLat)
{
  return fromLat - toLat;
}

double CalcDiffLat(double fromLon, double toLon)
{
  return fromLon - toLon;
}

double DegreesToMeters(double deltaDegrees)
{
  return deltaDegrees * ONE_DEGRE_OF_LATITUDE_IN_METERS;
}

double DegreesToRadians(double degrees)
{
  return (degrees * (std::numbers::pi / 180));
}

double MetricDistanceGivenLat(double avgLatRad, double deltaLon)
{
  double distance = deltaLon * std::cos(avgLatRad) * ONE_DEGRE_OF_LATITUDE_IN_METERS;
  std::cout << "delta Lon: " << deltaLon << std::endl;
  std::cout << "cos(lat): " << std::cos(avgLatRad) << std::endl;
  std::cout << "meters/degree: " << ONE_DEGRE_OF_LATITUDE_IN_METERS << std::endl;
  return distance;
}

int main()
{
  latLonPos start{};
  start.Lat = 60.5902;
  start.Lon = 8.5733;

  latLonPos end{};
  end.Lat = 60.5902;
  end.Lon = 8.5732;

  auto diffLonDeg    = CalcDiffLon(start.Lon, end.Lon);
  auto diffLonMeters = DegreesToMeters(diffLonDeg);

  std::cout << "delta Lon degrees = " << diffLonDeg << std::endl;
  std::cout << "delta Lon meters = " << diffLonMeters << std::endl;

  // std::cout << "cos(60.5902): " << std::cos(DegreesToRadians(60.5902)) << std::endl;
  auto distanceAtLatitude = MetricDistanceGivenLat(DegreesToRadians(start.Lat), diffLonDeg);
  std::cout << "distance at lat: " << distanceAtLatitude << std::endl;
  // auto radiansNorth = DegreesToRadians(start.Lat);
}
