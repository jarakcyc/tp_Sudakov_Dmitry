cmake_minimum_required(VERSION 2.8)

project(task)

find_package(PythonInterp 3 REQUIRED)
set(py_cmd "preparing.py")
#message("${PYTHON_EXECUTABLE}")
execute_process(
                  COMMAND ${PYTHON_EXECUTABLE} ${py_cmd}
                  WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}/A"
               )

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

set(SOURCE_EXE C/main.cpp)

include_directories(.)

add_executable(main ${SOURCE_EXE})

add_subdirectory(B)

target_link_libraries(main car_lib)
