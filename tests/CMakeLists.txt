
add_subdirectory(./googletest)
include_directories( ${OpenCV_INCLUDE_DIRS} )

set(target "out_test")
set(LIBRARIES test pthread)

add_executable(${target} test.cpp ../srcs/my_lib.cpp ../srcs/my_lib.h)

target_link_libraries(${target} gtest gtest_main ${TORCH_LIBRARIES} ${OpenCV_LIBS} ${EIGEN3_LIBS})



