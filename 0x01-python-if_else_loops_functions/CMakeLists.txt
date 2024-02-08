cmake_minimum_required(VERSION 3.27)
project(0x01_python_if_else_loops_functions C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(0x01_python_if_else_loops_functions
        13-insert_number.c
        lists.h
        13-main.c
        linked_lists.c
)
