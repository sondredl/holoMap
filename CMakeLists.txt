cmake_minimum_required(VERSION 3.14)

# Set the project name and version
project(CoordinateTransform VERSION 1.0 LANGUAGES CXX)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_EXTENSIONS OFF)

# Add the executable
add_executable(CoordinateTransform components/coordinateTransform/main.cpp)

# Include directories (if needed)
# target_include_directories(CoordinateTransform PRIVATE include)

# Link libraries (if needed)
# target_link_libraries(CoordinateTransform PRIVATE some_library)

