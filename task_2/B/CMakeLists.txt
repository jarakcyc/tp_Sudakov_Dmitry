cmake_minimum_required(VERSION 2.8)

project(car)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

set(SOURCE_LIB lib.cpp)

add_library(car_lib STATIC ${SOURCE_LIB})
