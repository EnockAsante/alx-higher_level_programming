cmake_minimum_required(VERSION 3.27)
project(0x03_python_data_structures C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(0x03_python_data_structures
        13-is_palindrome.c
        13-main.c
        "cat linked_lists.c"
        lists.h)
